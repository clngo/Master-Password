import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import getpass

class master_pass:
    """
    The master password is used to create a very special key. The special
    key is used to encrypt and decrypt the other passwords stored in a text file.
    """
    
    def __init__(self):
        self.fer = None
        
    def change_master(self):
        """
        First, decrypt the previous passwords through view(). 
        Then, change the key using master_write_key, asking for 
        a new master password.
        Lastly, encrypt the previous passwords with the new key.
        """
        newname = []
        newpass = []

        filelist = self.read()
        if not filelist:
            print("No passwords stored")
            return 
        
        for line in filelist:
            data = line.rstrip()
            name, pswrd = data.split("|")
            name, pswrd = name.encode(), pswrd.encode()
            pswrd = self.fer.decrypt(pswrd).decode() 
            name = self.fer.decrypt(name).decode()
            newname.append(name)
            newpass.append(pswrd)

        self.master_write_key()

        with open("password.txt", "w") as file:
            for i in range(len(newname)):
                title = newname[i].encode()
                pswrd = newpass[i].encode()
                file.write(self.fer.encrypt(title).decode() + "|" + self.fer.encrypt(pswrd).decode() + "\n")
        newname = []
        newpass = []
        file.close()
        

    def master_write_key(self): 
        """
        Creates the key for the master password. 
        """
        master = getpass.getpass("master: ")
        master = master.encode()
        salt = b"5"
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
            )
        key = base64.urlsafe_b64encode(kdf.derive(master))
        self.fer = Fernet(key)

    def check_key(self):
        """
        The file tries to decrypt a line in the txt file. 
        If the encyrption works, then the key (from masterpassword) is correct.
        If the encryption doesn't work, the key (and the masterpassword) is incorrect.
        If there is nothing in the text file to read, create a new master password. 
        """
        try:
            with open("password.txt", "r") as file:
                line = file.readline()
        except FileNotFoundError:
            file = open("password.txt", "w")
        with open("password.txt", "r") as file:
                line = file.readline()
        file.close()
        if line:
            name, pswrd = line.split("|")
            pswrd = pswrd.encode()
            try:
                pswrd = self.fer.decrypt(pswrd).decode()
            except:
                print("Invalid password")
                return 
        else: 
            print("New master password created")
            print("IMPORTANT: Add 1 password to save master password")
        return True

    def read(self):
        """
        Reads the text file and puts each line into a list. 
        """
        with open("password.txt", "r") as file:
            filelist = file.readlines()
        file.close()

        return filelist
    
    def view(self):
        """
        Decrypts each line from the text file and prints out the name and the password respectively. 
        """
        filelist = self.read()
        if not filelist:
            print("No passwords stored")
            return 
        
        for line in filelist:
            data = line.rstrip()
            name, pswrd = data.split("|")
            name, pswrd = name.encode(), pswrd.encode()
            pswrd = self.fer.decrypt(pswrd).decode()
            name = self.fer.decrypt(name).decode()
            print(f"{name} | {pswrd}")    
        

    def add(self):
        """
        Asks for the name corresponding to the password as string. 
        The password (but not the name) gets encrypted and written (appended)
        to the text file.
        """
        title = input("input username: ")
        pswrd = getpass.getpass("input password: ")
        title, pswrd = title.encode(), pswrd.encode()

        with open("password.txt", "a") as file:
            file.write(self.fer.encrypt(title).decode() + "|" + self.fer.encrypt(pswrd).decode() + "\n")
        file.close()


    def delete(self):
        """
        Asks for the name corresponding to a password to remove.
        """
        linelist = self.read()
        
        for line in linelist:
            data = line.rstrip()
            name, pswrd = data.split("|")
            name = name.encode()
            name = self.fer.decrypt(name).decode()
            print(name)

        title = input("Input username to delete: ")
        if not title:
            print("deleting cancelled")
            return
        lentitle = len(title)
        
        exists = False
        for i in range(len(linelist)):
            decrypted = linelist[i].encode()
            decrypted = self.fer.decrypt(decrypted).decode()
            if decrypted[:lentitle] == title:
                dline = i
                exists = True
                break

        if not exists:      
            print("doesn't exist")
        else:
            linelist[dline] = ""
            print(f"deleted {title}")

        with open("password.txt", "w") as file:
            for line in linelist:
                file.write(line)
        file.close()
        

def main():
    unlocked = False
    while not unlocked:
        master = master_pass()
        master.master_write_key()
        unlocked = master.check_key()

    while unlocked:
        print("""
        (1) Add
        (2) View
        (3) Delete
        (4) Change Master Password
        (5) Quit
        """)

        mode = input()
        if mode == "5":
            master.key = None
            exit()
        elif mode == "1":
            master.add()
        elif mode == "2":
            master.view()
        elif mode == "3":
            master.delete()
        elif mode == "4":
            master.change_master()
        else:
            print("Invalid input")
            continue

if __name__ == "__main__":
    main()
