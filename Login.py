from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle


def pkl_file(data, filename):
    with open(filename, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


def login(email, password, url):
    cookies=[]
    try:
        driver.get(url)
        email_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username")))
        email_box.send_keys(email)
        
        
        password_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password")))
        password_box.send_keys(password)
        
        
        login_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[4]/button')
        login_button.click()
        
        time.sleep(10)

        cookies = driver.get_cookies()
             
    except Exception as e:
        print(f"An error occurred: {e}")
        
    return(cookies)



if __name__ == "__main__":
    
    driver = webdriver.Chrome()
    linkedin_url = "https://www.linkedin.com/feed/?trk=guest_homepage-basic_nav-header-signin"
    
    email = "Anasjibi@outlook.com"
    password = 'anesanes12'

    cookies = login(email, password, linkedin_url)
    time.sleep(20)
    pkl_file(cookies, "Cookies.pkl")
    print("DONE")
    driver.quit()
