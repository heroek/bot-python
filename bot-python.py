
#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests, os
from random import randint
from random import shuffle
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from requests.exceptions import ConnectionError
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def checkcaptcha():
    try:
        browser.find_element_by_xpath("//*[@id='recaptcha-warp']").is_displayed()
        return True
        pass
    except NoSuchElementException:
        print "\033[32m\033[1mNo Captcha found!!!\033[0m"
        return False
        pass

def solvecaptcha():
    API_KEY = "YOUR 2 CAPTCHA API KEY"
    
    site_key = "6Lc-5yUTAAAAAIGyNiFQ0vi8Mgaz2AU_dAbUqw5r"
    url = browser.current_url
    s = requests.Session()
    captcha_id = s.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(API_KEY, site_key, url)).text.split('|')[1]
    print captcha_id
    recaptcha_answer = s.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id)).text
    print("solving ref captcha...")
    while 'CAPCHA_NOT_READY' in recaptcha_answer:
        sleep(5)
        recaptcha_answer = s.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id)).text
    solvecaptcha.answer = recaptcha_answer.split('|')[1]
    print solvecaptcha.answer
    print "\033[32m\033[1mCAPTCHA SUCCESFULLY SOLVED!\033[0m"

def submitcaptcha():
    sleep((randint(2200, 3700) / 1000))
    browser.execute_script("document.getElementById('g-recaptcha-response').removeAttribute('style', 'display: None');")
    sleep((randint(2200, 3700) / 1000))
    cap = browser.find_element_by_xpath("//*[@id='g-recaptcha-response']")
    cap.click()
    cap.send_keys(solvecaptcha.answer)
    sleep((randint(2200, 3700) / 1000))
    browser.find_element_by_xpath("//*[@id='go-submit-captcha']").click()
    sleep((randint(6200, 8700) / 1000))
    print "\033[32m\033[1mCAPTCHA SUBMITTED!\033[0m"

def waitpageload():
    rt1 = randint(9000,10500)
    rt2 = randint(10501,13000)
    t1 = randint(rt1,rt1)
    t2 = randint(rt2,rt2)
    s = sleep((randint(t1, t2) / 1000.0)*(t1 / 9200.0))
    print "\033[32m\033[1mWaiting for page to load! This took some seconds...\033[0m"

def checknewtab():
    if len(browser.window_handles) != 1:
        if len(str(browser.current_url.split("/")[2])) == 10:
            print "\033[32m\033[1m"+browser.current_url.split("/")[2]
            return True
        else:
            print "\033[32m\033[1m"+browser.current_url.split("/")[2]
            return False

def delpopupwindow():
    if len( browser.window_handles ) != 1 and len( str( browser.current_url.split( "/" )[2] ) ) != 10:
        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)
        browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.LEFT_SHIFT +'w')
        print "\033[32m\033[1mPopUpWindow closed...\033[0m"


def checkdone():
    try:
        browser.find_element_by_xpath("//*[@id='go-submit' and text() = 'Done']").is_displayed()
        return True
        pass
    except NoSuchElementException:
        return False
        pass

def submitdone():
    sleep((randint(2200, 3700) / 1000))
    browser.find_element_by_xpath("//*[@id='go-submit' and text() = 'Done']").submit()
    sleep((randint(6200, 8700) / 1000))
    print "\033[32m\033[1mDONE BUTTON CLICKED!\033[0m"

def linkscrape():
    sleep((randint(4340, 7000) / 1000))
    browser.execute_script("window.scrollTo(0, 0);")
    sleep((randint(4340, 7000) / 1000))
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep((randint(4340, 7000) / 1000))
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep((randint(4040, 6000) / 1000))
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep((randint(4340, 7000) / 1000))
    browser.execute_script("window.scrollTo(0, 0);")
    sleep((randint(4200, 8700) / 1000))
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep((randint(4200, 10000) / 1000))
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep((randint(4200, 8700) / 1000))


def checklogin_needed():
    try:
        browser.find_element_by_partial_link_text("Sign in")
        print "\033[32m\033[1mFound SignIn Form and Button\033[0m"
    except NoSuchElementException:
        pass

def my():
    profile = webdriver.FirefoxProfile(ppath)
    my.browser = webdriver.Firefox(profile)
    my.browser.get(homeurl)


def mainloop():
    linkscrape()
    element = browser.find_elements_by_xpath("//*[@class='m-bts link-click']")
    shuffle(element)
    counter = 0
    while True:
        for nx in element:
            try:
                nx.click()
                waitpageload()
                if checknewtab() is True:
                    print "\033[32m\033[1mFOUND\033[0m A NEW TAB"
                    sleep((randint(6200, 8700) / 1000))
                    new_window = browser.window_handles[1]
                    browser.switch_to.window(new_window)
                    print "\033[32m\033[1mCurrent URL is: " + browser.current_url
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    if checkcaptcha() is not False:
                        try:
                            solvecaptcha()
                        except ConnectionError:
                            browser.find_element_by_tag_name('body').send_keys(Keys.F5)
                            mainloop()
                            pass
                        submitcaptcha()
                    sleep((randint(21000, 27000) / 1000))
                    if checkdone() is not False:
                        submitdone()
                    try:
                        browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.LEFT_SHIFT +'w')
                        old_window = browser.window_handles[0]
                        browser.switch_to.window(old_window)
                        counter += 1
                        print "\033[32m\033[1mWindow Closed.\033[0m"
                        sleep(2.5)
                        cls()
                        print "\033[31m\033[1mYou have clicked: \033[32m\033[1m"+str(counter)+"\033[31m\033[1m news articles!\033[0m"
                        print "\033[31m\033[1mEarned Money so far: \033[32m\033[1m"+"\033[32m\033[1m"+browser.find_element_by_xpath("//*[@class='user_balance']").text
                        print "\033[31m\033[1mArticles to read: \033[32m\033[1m"+browser.find_element_by_xpath("//*[@class='h-item-value']").text.split(" ")[0]
                        sleep((randint(2200, 3700) / 1000))
                        browser.find_element_by_tag_name('body').send_keys(Keys.F5)    
                        sleep((randint(2200, 3700) / 1000))
                        linkscrape()
                        if counter <= browser.find_element_by_xpath("//*[@class='h-item-val").text.split(" ")[0]:
                            print "Platzhalter für stopscript oder changeuser oder so"
                    except ElementNotVisibleException:
                        browser.find_element_by_tag_name('body').send_keys(Keys.F5)
                        mainloop()
                        pass
                    except StaleElementReferenceException:
                        browser.find_element_by_tag_name('body').send_keys(Keys.F5)
                        mainloop()
                        pass
                    except WebDriverException:
                        browser.find_element_by_tag_name('body').send_keys(Keys.F5)
                        mainloop()
                        pass
            except StaleElementReferenceException:
                browser.find_element_by_tag_name('body').send_keys(Keys.F5)
                mainloop()
                pass
            except WebDriverException:
                browser.find_element_by_tag_name('body').send_keys(Keys.F5)
                mainloop()
                pass
            except ElementNotVisibleException:
                browser.find_element_by_tag_name('body').send_keys(Keys.F5)
                mainloop()
                pass
            counter += 1
##--------------------------------------------------------------------------------------------------------------------##


USERNAME = "YOUR_ADIPHY_USERNAME"
PASSWORD = "YOUR_ADAIPHY_PASSWORD"

ppath = "PATH TO FIREFOX PROFILE"

homeurl = "http://adiphy.com/"
loginurl = "http://adiphy.com/auth/signin/"

my()

browser = my.browser

if browser.current_url == loginurl:
    ## LOGIN USER_FORM
    WebDriverWait(browser, 17).until(lambda s: s.find_element_by_id("username")).is_displayed()
    uf = browser.find_element_by_id("username")
    uf.click()
    uf.send_keys(USERNAME)

    ## LOGIN PASSWORD_FORM
    pf = browser.find_element_by_id("password")
    pf.click()
    pf.send_keys(PASSWORD)

    ## SUBMIT LOGIN BTN
    lb = browser.find_element_by_css_selector("button.btn")
    lb.submit()
    sleep(range(2,7))

try:
    mainloop()
except StaleElementReferenceException:
    browser.find_element_by_tag_name('body').send_keys(Keys.F5)
    mainloop()
    pass
except WebDriverException:
    browser.find_element_by_tag_name('body').send_keys(Keys.F5)
    mainloop()
    pass
except ElementNotVisibleException:
    browser.find_element_by_tag_name('body').send_keys(Keys.F5)
    mainloop()
    pass