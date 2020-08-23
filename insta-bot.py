"""
An Instagram bot written in Python using Selenium on Google Chrome. 
It will go through posts in hashtag(s) and like and comment on them.
"""

# Built-in/Generic Imports
from time import sleep
import logging
import sys
from random import randint

# Library Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Own modules
from credentials import *
from config import *

__author__ = 'Annie Wu'
__version__ = '1.0.0'
__maintainer__ = 'Annie Wu'
__email__ = 'anniewu2303@gmail.com'
__status__ = 'Dev'

logging.basicConfig(format='%(levelname)s [%(asctime)s] %(message)s', datefmt='%m/%d/%Y %r', level=logging.INFO)
logger = logging.getLogger()

def initialize_browser():

    # Do this so we don't get DevTools and Default Adapter failure
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Initialize chrome driver and set chrome as our browser
    browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)

    return browser


def login_to_instagram(browser):
    browser.get('https://www.instagram.com/')
        
    sleep(2)

    # Get the login elements and type in your credentials
    username = browser.find_element_by_name('username')
    username.send_keys(USERNAME)
    password = browser.find_element_by_name('password')
    password.send_keys(PASSWORD)

    sleep(2)

    # Click the login button
    browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()

    # If login information is incorrect, program will stop running
    try:
        if browser.find_element_by_xpath("//*[@id='slfErrorAlert']"):
            browser.close()
            sys.exit('Error: Login information is incorrect')
        else:
            pass
    except:
        pass

    browser.implicitly_wait(5)

    logger.info(f'Logged in to {USERNAME}')

    # Save your login info? Not now
    browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
    browser.implicitly_wait(5)

    # Turn on notifications? Not now
    browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
    browser.implicitly_wait(5)

def automate_instagram(browser):
    # Keep track of how many you like and comment
    likes = 0
    comments = 0

    # Index for tags in hashtag list
    tag_index = 0

    for hashtag in hashtag_list:
        browser.get(f'https://www.instagram.com/explore/tags/{hashtag_list[tag_index]}/')
        logger.info(f'Exploring #{hashtag}')
        sleep(randint(1,2))

        # Click first thumbnail to open
        first_thumbnail = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]")
        first_thumbnail.click()

        sleep(randint(1,2))

        # Go through x number of photos per hashtag
        for post in range(1,number_of_posts):

            # Check if the post is already liked
            try:
                browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/*[@aria-label='Unlike']")
                logger.info("Already liked this post previously")
            except:
                # Like
                browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/*[@aria-label='Like']").click()
                logger.info("Liked")
                likes += 1

                sleep(randint(2,4))

                # Comment
                try:
                    browser.find_element_by_xpath("//form").click()
                    # Random chance of commenting
                    do_i_comment = randint(1,chance_to_comment)
                    if do_i_comment == 1:
                        
                            comment = browser.find_element_by_xpath("//textarea")

                            sleep(wait_to_comment)

                            rand_comment_index = randint(0,len(comments_list))
                            comment.send_keys(comments_list[rand_comment_index])
                            comment.send_keys(Keys.ENTER)
                            logger.info(f"Commented '{comments_list[rand_comment_index]}'")
                            sleep(wait_between_posts)
                            comments += 1

                except Exception:
                    # Continue to next post if comments section is limited or turned off
                    continue
            
            # Go to next post
            browser.find_element_by_link_text('Next').click()
            logger.info('Getting next post')
            sleep(wait_between_posts)    
        
        # Go to the next index in hashtags_list
        tag_index += 1

    logger.info(f'Liked {likes} posts')
    logger.info(f'Commented on {comments} posts')

    # Close browser when done
    logger.info('Closing chrome browser...')
    browser.close()

if __name__ == "__main__":
    browser = initialize_browser()
    login_to_instagram(browser)
    automate_instagram(browser)
