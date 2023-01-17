import requests
import urllib.request
import re
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def yelp_login(email, password):

    CHROMEDRIVER_PATH = "/path/to/chromedriver"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    service = ChromeService(executable_path=CHROMEDRIVER_PATH)

    url = "https://www.yelp.com/login"
    driver = webdriver.Chrome(service=service, options=options)

    #LOGS INTO YELP
    driver.get(url)
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div[1]/form/input[2]").send_keys(email)
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div[1]/form/input[3]").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div[1]/form/button").click()
    print("LOGGED IN!")
    sleep(4)

    #NAVIGATES TO 'yelp.com/collections/user' TO GET 'my-bookmarks' URL
    driver.get("https://yelp.com/collections/user")
    print("At the Collections page!")

    my_bookmarks = driver.find_element(By.LINK_TEXT, "My Bookmarks")
    bookmarks_page = (my_bookmarks.get_attribute("href") + "/My-Bookmarks?sort_by=alpha")
    print(bookmarks_page)

    #GETS LINKS TO RESTAURANTS IN 'MY BOOKMARKS'
    driver.get(bookmarks_page)
    elems = driver.find_elements(By.CSS_SELECTOR,"a.biz-name.js-analytics-click")
    links = [elem.get_attribute('href') for elem in elems]
    print(links)

    ### GRABS RESTAURANT NAME FROM BOOKMARKS###
    global restaurants
    restaurants = []
    for restaurant in links:
        restaurant = str(restaurant)
        restaurant = restaurant.split("biz/",1)[1]
        restaurant = restaurant.replace("-", " ").title()
        restaurants.append(restaurant)
    print(restaurants)   

    ### GRABS THE WAIT TIME FROM RESTAURANT PAGE###
    global listed_waits
    listed_waits = []
    def waitgrabber(biz):
        
        driver.get(biz)
        try:
            waitlist = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.css-uuks25")))
        except:
            waitlist = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.css-1sb02f4")))
        
        if waitlist.is_displayed() == True:
            listed_waits.append(waitlist.text)
        elif waitlist.is_displayed() != True:
            listed_waits.append("Waitlist Unavailable")    
            
    for restaurant in links:
        waitgrabber(restaurant)
        
    print(listed_waits)

    driver.quit()


#for 5 bookmarks process takes 25 seconds#