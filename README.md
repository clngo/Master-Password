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

A unique encryption key is created from the master password. No other key will ever be the same unless it is created from the master password. This encryption key is able to encrypt and decrypt other passwords. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Optimizations

As stated earlier, I arbitrarily chose a constant EAR value as the threshold to close the eye. To be more accurate, I could calculate the average slope produced (visually shown in the figure/graph) and keep track of when the change in EAR is drastically slow as an indicate of a blink. This is far more accurate as an indicator of a blink isn't precisely on a constant value, but a sudden change. 
Furthermore, the glare from my glasses interferes with accurate eye landmarks and so it incorrectly counts more blinks than actuality. 

### Lessons Learned

I had so much fun creating this project. Flipping on my camera and look at my face be covered in green made me forget the hours I struggled coding. Although it wasn't necessary, I wanted to plot down the data for myself. I learned that csv files were the best way of storing sensory data. So now I have a Python file on creating a csv file and how to animate a plot in real time. It was like a second mini project on top of the eye detection. 

### Built With
* [![Python][Python.js]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites
* pyca/cryptography includes both high level recipes and low level interfaces to common cryptographic algorithms such as symmetric ciphers, message digests, and key derivation functions. 
  ```sh
  pip install cryptography
  ```


### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/clngo/Master-Password.git
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Run bleenk.py to start the program.

It will first provide a list of options to choose from.
You can enable face landmarks, eye landmarks, or even an indicator of which eye you wink at. 
To turn off the program from any of these options enabled, press ESC. Otherwise, CTRL+C.
The last option to enable stats will produce a graph that plots the eye aspect ratio (EAR) over time.
Disabling all of the functions will not disable the program from counting the number of blinks and the cartoon blinking sound effect if the number of blinks is below 25 within 60 seconds. 

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
