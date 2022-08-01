from cgitb import text
from telnetlib import EC
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        

    def test_b_success_add_reportingmethod(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.ID, "txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        browser.get("https://opensource-demo.orangehrmlive.com/index.php/core/viewDefinedPredefinedReports/reportGroup/3/reportType/PIM_DEFINED") # buka halaman
        browser.find_element(By.ID, "search_search").send_keys("Employee") # isi value
        browser.find_element(By.ID, "search_search").send_keys("\n") # enter
        browser.find_element(By.CLASS_NAME,"searchBtn").click() # klik tombol save
        time.sleep(1)
        # validasi
        welcome_act = browser.find_element(By.ID,"resultTable").text
        welcome_exp = 'Employee'
        self.assertIn(welcome_exp, welcome_act)


    def tearDown(self): 
        self.browser.close() 
        

if __name__ == "__main__": 
    unittest.main()