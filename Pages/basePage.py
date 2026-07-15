import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import Logger


class basePage:

    def __init__(self,driver):
        self.driver = driver
        self.logger = Logger.get_logger()

    #this function will return the list of window_id's of windows opened
    def get_window_handles(self):
        window_ids = self.driver.window_handles
        return window_ids

    def is_overlay_present(self):
        """Returns True if an overlay is present, else False"""
        try:
            overlays = self.driver.find_elements(By.CLASS_NAME, "loading-dots")  # Adjust locator if needed
            return any(overlay.is_displayed() for overlay in overlays)  # Check if any overlay is visible
        except:
            return False

    def explicit_wait(self, locator_value):
        try:
            # Wait for overlay to disappear
            WebDriverWait(self.driver, 20).until_not(lambda driver: self.is_overlay_present())
            # Wait for element to be clickable
            return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, locator_value)))
        except:
            return None  # Return None if element is not found or not clickable


    #use this instead of explicit wait1 for waiting to a toast message
    def explicit_wait_for_toast(self,locator_value):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator_value)))

    # to switch to particular windows using window_id
    def switch_to_any_window(self,window_id):
        self.driver.switch_to.window(window_id)
        #time.sleep(3)
        #print(3)

    # to switch to iframe
    def switch_to_any_iframe(self, element):
        self.driver.switch_to.frame(element)

    #this function will return the present page title
    def get_title(self):
        return self.driver.title

    #Used to switch to particular frame using frame_id
    def switch_to_frame(self,id):
        self.driver.switch_to.frame(id)

    #to type into particular field
    #locator_name = searchbar_xpath , locator_value = "//input[@placeholder='Search']" , text = mac
    def type_into_element(self,text,locator_name,locator_value):
        time.sleep(2)
        element = self.get_element(locator_name,locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def upload_file(self, file_path, locator_name, locator_value):
        upload_element = self.get_element(locator_name, locator_value)
        upload_element.send_keys(file_path)
        self.logger.info(f"Uploaded file: {file_path}")

    def goto_nextline(self):
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    #used to click on a particular element
    def element_click(self,locator_name,locator_value):
        self.explicit_wait(locator_value)
        element = self.get_element(locator_name,locator_value)
        element.click()


    #to check the element is enable or not and return true or false
    def check_element_is_enable_or_disable(self,locator_name,locator_value):
        a = self.get_element(locator_name, locator_value).is_enabled()
        return a

    #check element is present or not
    def check_display_status(self,locator_name,locator_value):
        if self.get_element(locator_name, locator_value):
            return True
        else:
            return False

    #to extract completed text from the element
    def retrieve_element_text(self,locator_name,locator_value):
        self.explicit_wait(locator_value)
        element = self.get_element(locator_name,locator_value)
        return element.text

    def close_pop_up(self):
        actions = ActionChains(self.driver)
        actions.move_by_offset(10, 10).click().perform()

    # this method will return the particular element based on locator name and value
    #    locator_name = group_tab_xpath , locator_value =  "//span[contains(text(),'Group')]"

    def get_element(self, locator_name, locator_value):
        try:
            if locator_name.__contains__("_id"):
                element = self.driver.find_element(By.ID, locator_value)
                if element.is_displayed():
                    return element
                else:
                    return False
            elif locator_name.__contains__("_xpath"):
                element = self.driver.find_element(By.XPATH, locator_value)
                if element.is_displayed():
                    return element
                else:
                    return False
            elif locator_name.__contains__("link_text"):
                element = self.driver.find_element(By.LINK_TEXT, locator_value)
                if element.is_displayed():
                    return element
                else:
                    return False
            elif locator_name.__contains__("_class_name"):
                element = self.driver.find_element(By.CLASS_NAME, locator_value)
                if element.is_displayed():
                    return element
                else:
                    return False
            elif locator_name.__contains__("_css"):
                element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
                if element.is_displayed():
                    return element
                else:
                    return False
            return None
        except NoSuchElementException:
            return False

    #this method will return list of elements
    def get_elements(self,locator_value):
        self.explicit_wait(locator_value)
        elements = self.driver.find_elements(By.XPATH, locator_value)
        return elements

    #to refresh the current page
    def page_refresh(self):
        self.driver.refresh()

    #To hover on element
    def hover_on_element(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

    #To scroll the page
    # def page_scroll_by(self,locator_name,locator_value):
    #     element = self.get_element(locator_name,locator_value)
    #     self.driver.execute_script("arguments[0].scrollIntoView();", element)
    #     time.sleep(3)

    def scroll_to_element(self,locator_name,locator_value):
        try:
            # Wait for the element to be present in the DOM
            element = self.get_element(locator_name,locator_value)
            # Scroll until the element is in view
            self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
        except Exception as e:
            print(f"An error occurred: {e}")