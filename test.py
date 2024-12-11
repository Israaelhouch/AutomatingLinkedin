from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
import pandas as pd



class search_profiles:
    
    def __init__(self, skill=None, action=None):
        self.skill = skill
        self.action = action
        
    def choose_skill(self):
        skills_df = pd.read_csv("skills.csv")
        fields=skills_df.columns

        print("available fields are:\n ")
        for i, field in enumerate(fields, start=0 ):
            print(f"{i}: {field}")
            
        n = int(input("\nEnter number for the field: "))
        while n < 1 or n > len(fields):
            n = int(input("Invalid number, please enter again:\n"))
            
        print(f"\nSkills in this field are:\n {skills_df.iloc[:, n-1]}")
        
        i = int(input("\nenter a number for skills:"))
        while i < 0 or i > len(skills_df):
            i = int(input("\nInvalid number, please enter again: "))
        
        self.skill = skills_df.iloc[i, n-1]
        print(f"\nYou are looking for {self.skill} skill.\n")
        
        print("action to choose:\n1- follow\n2- connect\n3- follow & connect")
        nb=int(input("enter the number: "))
        if nb==1:
            self.action ="Follow"
        elif nb==2:
            self.action="Connect"
        else:
            self.action="Follow & Connect"

        
    def load_cookies(self, driver, cookie_file):
        with open(cookie_file, 'rb') as f:
            cookies = pickle.load(f)
        
        driver.get("https://www.linkedin.com")
        time.sleep(2)
        
        for cookie in cookies:
            driver.add_cookie(cookie) 
    
    
    def connect(self, driver, profiles_list):
        buttons = driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'More actions')]")
        for button in buttons:
            if button.text in ["More","Plus"]:
                button.click()
                time.sleep(1)
                
                try:
                    button_connect = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@aria-label, 'Invite') and contains(@aria-label, 'to connect')]//span[text()='Connect']")))
                    print("Number of 'Connect' buttons found:", len(button_connect))
                    for button in button_connect:
                        print(button.text)
                        if button.text == "Connect":
                            profile_name = driver.find_element(By.TAG_NAME, 'h1').text
                            button.click()
                            print(profile_name)
                            profiles_list.append(profile_name)

                            break
                except Exception as e:
                    print("No button connect", e)
               
                  
    def find(self):
        driver = webdriver.Chrome()
        self.load_cookies(driver, 'Cookies.pkl')
        max_profiles = 8
        profiles_list = []
        i = 1 

        try:
            while len(profiles_list) < max_profiles:

                url = f"https://www.linkedin.com/search/results/people/?keywords={self.skill}%20top%20voices&origin=CLUSTER_EXPANSION&page={i}&sid=MaO"
                driver.get(url)
                driver.maximize_window()
                time.sleep(1)


                profiles = WebDriverWait(driver, 15).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "linked-area"))
                )
                print(f"Number of profiles found on page {i}: {len(profiles)}")


                links = [profile.find_element(By.TAG_NAME, 'a').get_attribute('href') for profile in profiles]

                for link in links:
                    if len(profiles_list) >= max_profiles:
                        break


                    driver.get(link)
                    time.sleep(2)

                    try:
                        badge1 = driver.find_element(By.CLASS_NAME, "pv-top-voice-badge--button")
                        if badge1:
                            self.connect(driver, profiles_list)   
    
                    except Exception:
                        print("No badge1 found.")
                        try:
                            badge2 = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located(
                                    (By.XPATH, '//*[@id="profile-content"]/div/div[2]/div/div/main/section[1]/div[2]/div[1]/div[2]/div/span')))
                            if badge2:
                                self.connect(driver, profiles_list)

                        except Exception:
                            print("No badge2 found.")
                            try:
                                engagement = self.engagement(driver)
                                if engagement:
                                    self.connect(driver, profiles_list)
                            except Exception:
                                print("No engagement found.")
                                continue
                i += 1  
                

        except Exception as e:
            print(f"Error occurred: {e}")

        finally:
            driver.quit()
            print(f"Total profiles followed or connected: {len(profiles_list)}")
            print(f"List of followed or connected profiles: {profiles_list}")


if __name__ == "__main__":
    

    searcher = search_profiles()

    searcher.find()
    
    
    
"""def find(self):
        driver = webdriver.Chrome()
        linkedin_url = "https://www.linkedin.com/feed"
        
        self.load_cookies(driver, 'Cookies.pkl')
        
        driver.get(linkedin_url)
        driver.maximize_window()
        time.sleep(3)
        
        max_profiles = 8
        profiles_list = []
        i=1
        url = f"https://www.linkedin.com/search/results/people/?keywords={self.skill}%20top%20voices&origin=CLUSTER_EXPANSION&page={i}&sid=MaO"
        driver.get(url)

        
        while len(profiles_list) <= max_profiles:

            profiles = WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "linked-area")))
            print(f"Number of profiles found on this page: {len(profiles)}")
            
            links = [profile.find_element(By.TAG_NAME, 'a').get_attribute('href') for profile in profiles]
     
            for link in links:
                if len(profiles_list) >= max_profiles:
                    break
                    
                driver.get(link)
                time.sleep(2)
                
                try:
                    badge1 = driver.find_element(By.CLASS_NAME, "pv-top-voice-badge--button")
                    if badge1:
                        if self.action=="Follow":
                            self.follow(driver, profiles_list) 
                        elif self.action=="Connect":
                            self.connect(driver, profiles_list)   
                        else:
                            self.follow(driver, profiles_list)
                            self.connect(driver, profiles_list)
 
                except Exception as e:
                    print("No badge1 found")
                    try:                   
                        badge2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="profile-content"]/div/div[2]/div/div/main/section[1]/div[2]/div[1]/div[2]/div/span')))
                        if badge2:
                            if self.action=="Follow":
                                self.follow(driver, followers_list) 
                            elif self.action=="Connect":
                                self.connect(driver, connected_list)   
                            else:
                                self.follow(driver, followers_list)
                                self.connect(driver, connected_list)
                    except Exception as e:
                        print("No badge2 found")
                        try:
                            engagement = self.engagement(driver)
                            if engagement:
                                if self.action=="Follow":
                                    self.follow(driver, followers_list) 
                                elif self.action=="Connect":
                                    self.connect(driver, connected_list)   
                                else:
                                    self.follow(driver, followers_list)
                                    self.connect(driver, connected_list)
                        except Exception as e:
                            print("No engagement found")
                            continue
                    """