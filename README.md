This repository contains a Selenium-based web automation framework using the Page Object Model (POM) design pattern with Pytest as the test runner. 
The goal is to provide a scalable and easy-to-maintain structure for test automation projects.

Project Setup:

    Prerequisite:
        Python is installed on the machine, # "https://qaautomation.expert/2023/03/20/how-to-install-python-on-windows-11/"
        PyCharm or other Python Editor is installed on the machine, # "https://qaautomation.expert/2023/03/24/how-to-install-pycharms-on-windows-11/"
        Downoad the chromedriver matching with your browser version, #https://googlechromelabs.github.io/chrome-for-testing/
        
What is Page Object Model?:
    
    The Page Object Model (POM) is a design pattern used in test automation, particularly in web application testing. It aims to enhance the test automation framework’s 
    maintainability, readability, and reusability by encapsulating the behavior of web pages or user interfaces into separate classes or modules called Page Objects.
    
    1. Create Page Objects: Define a separate class for each page of your web application. Each class should encapsulate the elements and actions of the corresponding 
       page.
    2. Write Test Cases: Implement your test cases as pytest test functions or methods. These test functions should interact with the page objects to perform actions and 
       assertions.
    3. Use Fixtures for Setup and Teardown: Utilize pytest fixtures for setup and teardown operations such as initializing the browser, navigating to URLs, and closing 
       the browser.
        
Project Structure:

<img width="256" alt="image" src="https://github.com/user-attachments/assets/648cf989-7134-4ff4-a1a0-8364e8069de3" />


Implementation Steps

    Step 1 – Install pytest
          Use the below command to install PyTest on your machine.
          "pip install pytest"
    Step 2 - Install selenium
          Use the below command to install Selenium on your machine.
          "pip install Selenium"
    Step 3: install supporting plugins for running the tests.
          Use the below command to install Selenium on your machine.
          "pip install pynput"
          "pip install openpyxl"
          "pip install allure-pytest"
          "pip install pyautogui"
          
How to create new Tests :

    Adding New Page
       1. Create a new file in the Pages directory.
       2. Define page elements using locators.
       3. Implement methods to interact with the elements.
       
    Adding New Test
       1. Create a new file in the Tests directory.
       2. Use pytest fixtures from conftest.py.
       3. Implement test methods with assertions.
       
