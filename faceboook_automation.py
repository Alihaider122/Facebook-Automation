# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:00:17 2019

@author: AliHaider
"""

faceBookEmail = "your_facebook_email@example.com"
faceBookPassword = "xxxxxxxxx"
Auto_Reply_Message = "Auto Reply Message"
URL_List = list()

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def messageSender(URL):
    print(URL)
    #following handels the alertbox exception
    try:
        userTargetUrl = URL
        browser.get(userTargetUrl)
        alert = browser.switch_to_alert()
        alert.accept()
    except:
        pass
    
    
    # wait for page load completely
    wait = WebDriverWait(browser,10)
    
    # following handles the element location presence exception
    try:
        wait.until(ec.visibility_of_element_located((By.XPATH,"//div[@aria-label='Messages']/div[@id='js_2']/div[last()]")))
        messages = browser.find_element_by_xpath("//div[@aria-label='Messages']/div[@id='js_2']/div[last()]")
        inboxTitle = browser.find_element_by_xpath("//div[@class='_673w']/div/div/h2/span")
    except:
        wait.until(ec.visibility_of_element_located((By.XPATH,"//div[@aria-label='Messages']/div[@id='js_2']/div[last()]")))
        messages = browser.find_element_by_xpath("//div[@class='_4_j4']/div/div/div[@class='uiScrollableAreaWrap scrollable']/div/div/div/div[@id='js_2']/div[last()]")
        wait.until(ec.element_to_be_clickable((By.XPATH,"//div[@class='_673w _1_fz']/div/div/h2/span")))
        inboxTitle = browser.find_element_by_xpath("//div[@class='_673w _1_fz']/div/div/h2/span")
        
    # following handles message text area presence expception
    try:
        if '' in inboxTitle.text: # condition to check something special in username string
            if "" in messages.text: # condtion to check something in the last inbox message from a specific user 
                element = browser.find_element_by_xpath("//div[@aria-autocomplete='list']")
                element.send_keys(Auto_Reply_Message)
                element.send_keys(Keys.RETURN)
                print("Message Send Successfully")
                time.sleep(1)
            else:
                print("Keyword Conditions are not Satisfied")
        else:
             print("Name:", inboxTitle.text)
             print("Message:",messages.text)
    except:
        print("Some Error")
       
    
#in the string/Quotation marks enter the path to where you downloaded the chromedriver.
browser = webdriver.Chrome("chromedriver")

#navigates you to the facebook page.
browser.get('https://www.facebook.com/')

# find email field and enter the email in it
username = browser.find_elements_by_css_selector("input[name=email]")
username[0].send_keys(faceBookEmail) 

#find the password field and enter the password password.
password = browser.find_elements_by_css_selector("input[name=pass]")
password[0].send_keys(faceBookPassword) # password of facebook account

#find the login button and click it.
loginButton = browser.find_elements_by_css_selector("input[type=submit]")
loginButton[0].click()

browser.get("https://www.facebook.com/messages/")

# find and scroll the conversation list of the messenger
try:
    element = browser.find_element_by_xpath("//ul[@aria-label='Conversation List']")
except:
    element = browser.find_element_by_xpath("//ul[@role='grid']")

for i in range(0,7): # no. of iterations to scroll down in a contacts list of messenger
    browser.execute_script("arguments[0].scrollIntoView(false);",element)
    time.sleep(2)
time.sleep(3)

# find all unreader messages
elements = element.find_elements_by_xpath("//li[@role='row']")
print(len(elements))
count = 1
# all URL getting
for i in elements:
    get = i.find_element_by_css_selector("div a").get_attribute("data-href")
    URL_List.append(get)
    
# message sending
for k in URL_List:
    print(count)
    messageSender(k)
    count = count + 1