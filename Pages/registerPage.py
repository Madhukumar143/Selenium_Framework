import time

from Pages.basePage import basePage
from selenium.webdriver.common.keys import Keys


class registerPage(basePage):
    # Locator(s) - names must end with _xpath

    def __init__(self, driver):
        super().__init__(driver)


    my_account_xpath = "//span[normalize-space()='My Account']"
    register_option_xpath = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Register']"

    #Register form Xpath's
    first_name_xpath = "//input[@id='input-firstname']"
    last_name_xpath = "//input[@id='input-lastname']"
    email_xpath = "//input[@id='input-email']"
    telephone_xpath = "//input[@id='input-telephone']"
    password_xpath = "//input[@id='input-password']"
    confirm_password_xpath = "//input[@id='input-confirm']"
    subscribe_yes_xpath = "//input[@name='newsletter' and @value='1']"
    subscribe_no_xpath = "//input[@name='newsletter' and @value='0']"
    privacy_policy_checkbox_xpath = "//input[@name='agree']"
    continue_button_xpath = "//input[@value='Continue']"

    def navigate_to_register_page(self):
        """Click on the register option to navigate to the register page."""
        self.element_click("my_account_xpath",self.my_account_xpath)
        self.element_click("register_option_xpath", self.register_option_xpath)
        self.logger.info("Navigated to the register page.")

    def register_page_confirmation(self):
        """Confirm that the register page is displayed by checking for a unique element."""
        # This is a placeholder. Replace with an actual locator for an element unique to the register page.
        if self.get_title()=="Register Account":
            self.logger.info("Register page is displayed.")
            return True
        else:
            self.logger.error("Register page is not displayed.")
            return False

    def register(self, first_name, last_name, email, telephone, password, subscribe):
        self.logger.info(f"Attempting to register")
        self.type_into_element(first_name, "first_name_xpath", self.first_name_xpath)
        self.type_into_element(last_name, "last_name_xpath", self.last_name_xpath)
        self.type_into_element(email, "email_xpath", self.email_xpath)
        self.type_into_element(telephone, "telephone_xpath", self.telephone_xpath)
        self.type_into_element(password, "password_xpath", self.password_xpath)
        self.type_into_element(password, "confirm_password_xpath", self.confirm_password_xpath)

        if subscribe.lower() == 'yes':
            self.element_click("subscribe_yes_xpath", self.subscribe_yes_xpath)
        else:
            self.element_click("subscribe_no_xpath", self.subscribe_no_xpath)

        self.element_click("privacy_policy_checkbox_xpath", self.privacy_policy_checkbox_xpath)
        self.element_click("continue_button_xpath", self.continue_button_xpath)
        self.logger.info("Registration form submitted.")
        time.sleep(3)

    def registration_confirmation(self):
        """Confirm that the registration was successful by checking for a unique element on the post-registration page."""
        # This is a placeholder. Replace with an actual locator for an element unique to the post-registration page.
        if self.get_title()=="Your Account Has Been Created!":
            self.logger.info("Registration successful, confirmation element is displayed.")
            return True
        else:
            self.logger.error("Registration failed, confirmation element is not displayed.")
            return False