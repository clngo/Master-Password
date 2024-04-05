<a name="readme-top"></a>

[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#how-it-works">How it Works</a></li>
        <li><a href="#optimizations">Optimizations</a></li>
        <li><a href="#lessons-learned">Lessons Learned</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

It's safer to have a unique password for every account that we have. But, it's hard to keep track of all those passwords. So instead, just remember one password to keep track of all the passwords. 

**Welcome to the master pass!**

By first inputting master password, you could organize a list of passwords for any account you have. It will encrypt every password listed and decrypt all passwords besides the master password. 

### How it Works

A unique encryption key is created from the master password. No other key will ever be the same unless it is created from the master password. This encryption key is able to encrypt and decrypt stored passwords. When a user enters a master password, the program will create an encryption key from it, and try to decrypt a password inside the text file. If the password did not get decrypted, then the encryption key is incorrect, and therefore, the master password is incorrect. If the password did get decrypted, then the encryption key is correct, and therefore, the master password is correct. This is why storing at least one person is important. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Optimizations

The stored passwords (not the master password) is stored in a text file. Although the passwords stored in the text file is encrypted, having access to the text file makes it vulnerable to deletion or manipulation, losing the stored passswords. Perhaps looking into other ways of storing the passwords will keep it from being manipulated. Nonetheless, the passwords are unable to be seen and the data remains hidden.

### Lessons Learned

My initial problem was storing the encryption key somewhere safe without it being reused easily. Instead, I demanded the user to create the encryption key themselves through the master password. This way, the only way to get the correct encryption key wasn't to store it, but to create one that matches. 

### Built With
* [![Python][Python.js]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites
To install packages, run the command:
```sh
pip install -r requirements.txt
```

* pyca/cryptography includes both high level recipes and low level interfaces to common cryptographic algorithms such as symmetric ciphers, message digests, and key derivation functions. 

* [Fernet](https://cryptography.io/en/latest/fernet/) is an implementation of symmetric (aka "secret key") authenticated cryptography. 


### Installation
1. Clone the repo
  ```sh
  git clone https://github.com/clngo/Master-Password.git
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

First, input your master password to store all the passwords. Since there are no stored passwords on first use, the master password comes first. Once a master password is created, you must add at least 1 password into the text file to save the master password. Leaving an empty or nonexistent text file for the program to read will not save the master password (why keep a master password that saves 0 passwords). 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Colin Ngo - [https://www.linkedin.com/in/colin-ngo654](https://www.linkedin.com/in/colin-ngo654) - cngo27@calpoly.edu

Project Link: [https://github.com/clngo/bleenk](https://github.com/clngo/bleenk)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [Best README Template](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/colin-ngo654
[Python-url]: https://www.python.org/
[Python.js]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
