import os
from Base import Base
from PageObjects.locators import *
from selenium.webdriver.common.by import By
import os.path
import subprocess
filename = "/Users/abuzar/Downloads/Invoice.csv"




class WebKeywords(Base):

    def validate_page_loads(self):
        """
        Open xml2csv converter app
        """
        try:
            self.selenium_lib.wait_until_element_is_visible(PAGE_URL)

        except:
            raise AssertionError(f"Could not load page: {PAGE_URL}")


    def upload_xml_file(self):
        """
        Upload the XML File
        """

        try:

            choose_file = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/form/input[1]')
            choose_file.send_keys("/Users/abuzar/assignment/xml2csv-converter/input/Invoice.xml")

        except:
         raise AssertionError("Could not upload the XML file")


    def csv_conversion(self):
        """
        XML file is converted to CSV
        """
        try:
            convert = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/form/input[2]")
            convert.click()

        except:
            raise AssertionError("Could not convert to CSV file")


    def file_downloads(self):
        """
        CSV file is downloaded to User Computer
        """
        try:
            print(os.path.exists("/Users/abuzar/Downloads/Invoice.csv"))

        except:
            raise AssertionError("Could not download the CSV file")

    def open_csv_file(self):
        """
        Open the downloaded CSV file
        """
        try:
            subprocess.call(['open', filename])
        except:
            raise AssertionError("Could not open file")
