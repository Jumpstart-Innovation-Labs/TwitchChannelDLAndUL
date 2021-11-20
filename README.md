<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<h3 align="center">Twitch Channel Download & Uploading Script</h3>

  <p align="center">
    <br />
    <a href="https://github.com/Jumpstart-Innovation-Labs/TwitchChannelDLAndUL/issues">Report Bug</a>
    ·
    <a href="https://github.com/Jumpstart-Innovation-Labs/TwitchChannelDLAndUL/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This python script allows you to download all VODs from a specified list of Twitch Channels. Once complete, you can also configure the script to FTP upload the files to an FTP server for long term archiving. If you don't need the FTP archiving feature, check out our parent repo that has that part removed. 

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email`, `email_client`, `project_title`, `project_description`

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Here is how to get started! Please note this has only been tested on Linux. It may work on windows, with some additional modifications to the script

### Prerequisites

Required software to get this script setup. Instrcutions are for Ubuntu-based machines.
* python3
  ```sh
  sudo apt-get install python3 -y
  ```
* pip
  ```sh
  sudo apt-get install python3-pip -y
  ```
* git
  ```sh
  sudo apt-get install git -y
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Jumpstart-Innovation-Labs/TwitchChannelDLAndUL.git
   ```
2. Install PIP packages
   ```sh
   sudo pip3 install -r requirements.txt
   ```
4. Enter all your Twitch channels in `channels.txt`
   ```sh
   LinusTech
   MichaelReeves
   Pokimane
   LilyPichu
   ```
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This script is very useful for automating the downloading of VODs. We use this as a way to Archive VOD's of our favourite channel to a storage server, and then we use Plex to serve these videos to our family and friends! It's expecially useful since VODs on Twitch do not stay on Twitch forever!

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Initial Launch
- [] Docker Option
- [] Release Packages (via Github)
    - [] Python/Apt Package????

See the [open issues](https://github.com/Jumpstart-Innovation-Labs/TwitchChannelDLAndUL/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/brandonaxtmann) - opensource@jumpstartlabs.co

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Jumpstart-Innovation-Labs/TwitchChannelDLAndUL.svg?style=for-the-badge
[contributors-url]: https://github.com/Jumpstart-Innovation-Labs/TwitchChannelDLAndUL/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Jumpstart-Innovation-Labs/TwitchChannelDLAndUL.svg?style=for-the-badge
[forks-url]: https://github.com/Jumpstart-Innovation-Labs/TwitchChannelDLAndUL/network/members
[stars-shield]: https://img.shields.io/github/stars/Jumpstart-Innovation-Labs/TwitchChannelDLAndUL.svg?style=for-the-badge
[stars-url]: https://github.com/Jumpstart-Innovation-Labs/TwitchChannelDLAndUL/stargazers
[issues-shield]: https://img.shields.io/github/issues/Jumpstart-Innovation-Labs/TwitchChannelDLAndUL.svg?style=for-the-badge
[issues-url]: https://github.com/Jumpstart-Innovation-Labs/TwitchChannelDLAndUL/issues
[license-shield]: https://img.shields.io/github/license/Jumpstart-Innovation-Labs/TwitchChannelDLAndUL.svg?style=for-the-badge
[license-url]: https://github.com/Jumpstart-Innovation-Labs/TwitchChannelDLAndUL/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/brandonaxtmann
