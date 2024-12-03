from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
import pandas as pd


def load_cookies(driver, pickle_file):
    with open(pickle_file, 'rb') as handle:
        cookies = pickle.load(handle)
    return cookies

      
class search_followers:
    def __init__(self, skill):
        self.skill = skill
    def find(self):
        nb_followers = 0
        max_followers = 30
        driver.get(
            f"https://www.linkedin.com/search/results/people/?keywords={self.skill}%20top%20voices&origin=CLUSTER_EXPANSION"
        )

        while nb_followers<max_followers:
            

            follow_connect_buttons = WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME,"artdeco-button artdeco-button--2 artdeco-button--secondary ember-view"))
            )

            print(f"Number of follow buttons found: {len(follow_buttons)}")
            for button in follow_buttons:
                if button.text == "Follow":

                    try:
                        if driver.find_element(By.CLASS_NAME, "entity-result__badge-icon"):
                            nb_followers += 1
                            button.click()
                            time.sleep(1)
                    except Exception as e:
                        continue    
                else:        
                    continue

            try:
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.CLASS_NAME, "artdeco-pagination__button--next")
                    )
                )
                next_button.click()
                time.sleep(2)
            except Exception as next_error:
                break
  
        


if __name__ == "__main__":
    

    skills_df = pd.read_csv("skills.csv")
    fieds=skills_df.columns
    i=1
    for fied in fieds:
        print(f"{i}:{fied}")
        i+=1
    n= int(input("enter number for fieds:"))
    print("\n")
    print(f"Skills in this fied are: {skills_df.iloc[:, n-1]}")
    i=int(input("enter a number for skills:"))
    skill=skills_df.iloc[i,n-1]
    print("\n")
    print(f"searched skill is: {skill}")
    print("\n")
    driver = webdriver.Chrome()
    linkedin_url = "https://www.linkedin.com/feed"
    cookies = load_cookies(driver,'Cookies.pkl')
    driver.get(linkedin_url)
    driver.maximize_window()
    
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()  
    time.sleep(1)
    
    search = search_followers(skill+" Top Voices")
    search.find()

    



    
    
    
    


