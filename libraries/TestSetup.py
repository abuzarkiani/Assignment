import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__))))
from Base import Base
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

class TestSetup(Base):

    def initialize_and_open_browser_with_url(self):
        """Opens browser with robot -d results tests/web_automation.robot given URL specified by parameters"""
        options = Options()
        options.add_argument('--headless')
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome("/Users/abuzar/Downloads/chromedriver")
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000")

    def close_browser(self):
        """Close active browser"""
        self.selenium_lib.driver.close()  
