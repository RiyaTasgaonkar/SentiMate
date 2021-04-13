from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import json
import pandas

from credentials import username,password
posts_scraped = []

class fb_bot():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        self.driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)


    def login(self,username,password):        
        self.driver.get("https://mbasic.facebook.com")
        #target username
        uname = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
        pword = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

        #enter username and password
        uname.clear()
        uname.send_keys(username)
        pword.clear()
        pword.send_keys(password)

        #target the login button and click it
        button = self.driver.find_element_by_name("login").click()


    def post_scraping(self):
        self.driver.get("https://mobile.facebook.com/profile.php?v=photos")
        upload = self.driver.find_element_by_class_name("content")
        upload.click()

        for j in range(0,5):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            
        links = self.driver.find_elements_by_class_name("_39pi")
        links = [a.get_attribute('href') for a in links]

        post = [] 
        for i in links:
            self.driver.get(i)
            po = self.driver.find_element_by_class_name("msg")
            element = self.driver.find_element_by_class_name('actor')
            self.driver.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, element)
            post.append(po.text)
        
        return post
    
    def remove_blank(self,post):
        nb = [string for string in post if string != ""]
        return nb

    def convert_to_json(self,post):   
        data = post
        # save the data
        with open('my_data.json', 'w') as out_f:
            json.dump(data, out_f)

    def convert_to_csv(self,post):
        list1 = [i+1 for i in range(len(post))]
        df = pandas.DataFrame(data={"col1": list1, "col2": post})
        df.to_csv("./file.csv", sep=',',index=False)


bot = fb_bot()
bot.login(username,password)
posts_scraped = bot.post_scraping()
posts_scraped = bot.remove_blank(posts_scraped)
bot.convert_to_json(posts_scraped)
bot.convert_to_csv(posts_scraped)
