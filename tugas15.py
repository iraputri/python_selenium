import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        

    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        browser.find_element(By.ID,"shopping_cart_container").is_displayed


    def test_b_invalid_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys("secret_sauces") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.CSS_SELECTOR,".error-message-container").text 
        self.assertEqual(response_message, 'Epic sadface: Username and password do not match any user in this service')


    def test_c_invalid_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "user-name").send_keys("standard_users") # isi email
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.CSS_SELECTOR,".error-message-container").text 
        self.assertEqual(response_message, 'Epic sadface: Username and password do not match any user in this service')


    def test_d_logout(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.ID,"react-burger-menu-btn").click() # klik tombol menu
        time.sleep(1)
        browser.find_element(By.ID,"logout_sidebar_link").click() # klik tombol logout
        time.sleep(1)

        # validasi
        browser.find_element(By.CSS_SELECTOR,".login_logo").is_displayed
    

    def test_e_locked_out_user(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "user-name").send_keys("locked_out_user") # isi email
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.CSS_SELECTOR,".error-message-container").text 
        self.assertEqual(response_message, 'Epic sadface: Sorry, this user has been locked out.')
        

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()