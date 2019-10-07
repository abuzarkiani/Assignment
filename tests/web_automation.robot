*** Settings ***
Library    ../libraries/PyKeywords.py
Variables  ../libraries/PageObjects/locators.py

Suite Setup    Initialize
Suite Teardown   Run Keyword And Ignore Error  Suite shutdown
*** Variables ***


*** Test Cases ***
Validate whether the URL "localhost:3000" loads
    Validate Page Loads

Validate whether the user is able to upload the XML by clicking the'Choose file' button
    Upload XML file

Validate whether the CSV file gets downloaded when the 'Convert to CSV' button is clicked
    CSV Conversion

Validate whether the converted CSV file gets saved in the download folder
    File downloads

Validate whether the user is able to open the CSV file with the valid data

    Open CSV file



*** Keywords ***
Initialize
    Initialize and open browser with url

Teardown
    Close browser