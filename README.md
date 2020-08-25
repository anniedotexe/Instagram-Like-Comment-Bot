# Simple Instagram Like & Comment Bot :heart::speech_balloon:

[![Python 3.6 | 3.7 | 3.8](https://img.shields.io/badge/python-3.6%20|%203.7%20|%203.8-yellowgreen)](https://www.python.org/downloads/release/python-385/)
![selenium](https://img.shields.io/badge/selenium-3.141.0-green)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)
<span class="badge-buymeacoffee"><a href="https://www.buymeacoffee.com/awu2303" title="Donate to this project using Buy Me A Coffee"><img src="https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg" alt="Buy Me A Coffee donate button" /></a>
</span>

An Instagram bot written in Python using Selenium on Google Chrome. It will go through posts in hashtag(s) and like and comment on them.

---

### Table of Contents

- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
- [Instructions](#instructions)
    - [File Structure](#file-structure)
- [Demo](#demo)
- [Creator / Maintainer](#creator-maintainer)
- [Additional Information](#additional-information)

---

## Getting Started

Please be aware of [Instagram's daily limits](https://socialpros.co/instagram-daily-limits#Instagram%E2%80%99s_Daily_Limits_in_2020) for likes and comments to avoid getting your account banned.

### Prerequisites

- [Python 3](https://www.python.org/downloads/)
- [Pip](https://pypi.org/project/pip/) - a python package manager
    - Download [this file](https://bootstrap.pypa.io/get-pip.py), open a command prompt and navigate to the folder containing the `get-pip.py` installer, and run `python get-pip.py` to install
    - Run `pip --version` to check if it has installed correctly
- [ChromeDriver](https://chromedriver.chromium.org/downloads) - a WebDriver for Chrome
    - See [Additional Information](#additional-information) for more details on installing
- [Selenium](https://pypi.org/project/selenium/) - a python package used to automate web browser interaction
    `pip install -U selenium`

## Instructions

1. Download [ChromeDriver](https://chromedriver.chromium.org/downloads) and extract the file.
    - Check the version of your Google Chrome and download the matching ChromeDriver version

![Check Chrome Version](https://media.giphy.com/media/UWP6UbIKLFcEH1bd1B/giphy.gif)

2. In `config.py` change the **chromedriver_path** to the local path of where your ChromeDriver executable file is located

```
chromedriver_path = "C:/local/path/to/chromedriver.exe"
```

3. Adjustments you can make in `config.py` to tweak the bot to your liking. *(Please be aware of [Instagram's daily limits](https://socialpros.co/instagram-daily-limits#Instagram%E2%80%99s_Daily_Limits_in_2020) for likes and comments to avoid getting banned.)*
    - **hashtag_list** - List of hashtags to go through
    - **comments_list** - List of comments to be randonmly chosen from
    - **number_of_posts** - Number of posts to go through per hashtag
    - **chance_to_comment** - Chance of commenting on photo
    - **wait_between_posts** - Time to wait in between instagram posts in seconds
    - **wait_to_comment** - Time to wait in between liking a post and commenting on it in seconds


4. Create a file named `credentials.py` to hold your account login information using the format below.
    - See [File Structure](#file-structure) for where the file should be placed.

```
USERNAME = "xxx"
PASSWORD = "xxx"
```

5. Run the script. Enjoy your Instagram bot!
```
python insta-bot.py
```

### File Structure

```
Twitter-Retweet-Bot
 |-- config.py
 |-- credentials.py
 |-- insta-bot.py
```

---

## Demo

![Demo](https://media.giphy.com/media/S8fLGEDnWACMJOswye/giphy.gif)

---

### Creator / Maintainer

Annie Wu ([anniewu2303](https://github.com/anniewu2303))

This project was created for educational purposes and for personal and open-source use.

If you like my content or find this code useful, give it a :star: or support me by buying me a coffee :coffee::grinning:

<a href="https://www.buymeacoffee.com/awu2303" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

---

## Additional Information

- [Installing Selenium and Chromedriver on Windows](https://medium.com/@patrick.yoho11/installing-selenium-and-chromedriver-on-windows-e02202ac2b08)
