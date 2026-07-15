from Pages.basePage import basePage

class LoginPage(basePage):
    # Locator(s) - names must end with _xpath

    def __init__(self, driver):
        super().__init__(driver)

    # navigation Xpath's
    my_account_menu_xpath = "//span[normalize-space()='My Account']"
    login_option_xpath = "//ul[@class='dropdown-menu dropdown-menu-right']/descendant::a[contains(.,'Login')]"

    # login details Xpath's
    email_xpath = "//input[@id='input-email']"
    password_xpath = "//input[@id='input-password']"
    login_button_xpath = "//input[@value='Login']"
    logout_option_xpath = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Logout']"
    logout_confirmation_xpath = "//h1[normalize-space()='Account Logout']"

    login_confirmation_xpath = "//a[normalize-space()='Edit your account information']"

    def navigate_to_login_page(self):
        """Click on the login option to navigate to the login page."""
        self.element_click("my_account_menu_xpath",self.my_account_menu_xpath)
        self.element_click("login_option_xpath", self.login_option_xpath)
        self.logger.info("Navigated to the login page.")

    def login_page_confirmation(self):
        """Confirm that the login page is displayed by checking for a unique element."""
        # This is a placeholder. Replace with an actual locator for an element unique to the login page.
        if self.get_title()=="Account Login":
            self.logger.info("Login page is displayed.")
            return True
        else:
            self.logger.error("Login page is not displayed.")
            return False

    def login(self, email, password):
        self.logger.info(f"Attempting to login")
        self.type_into_element(email, "email_xpath", self.email_xpath)
        self.type_into_element(password, "password_xpath", self.password_xpath)
        self.element_click("login_button_xpath", self.login_button_xpath)
        self.logger.info("Login form submitted.")

    def login_confirmation(self):
        """Confirm that the login was successful by checking for a unique element on the post-login page."""
        # This is a placeholder. Replace with an actual locator for an element unique to the post-login page.
        if self.check_display_status("login_confirmation_xpath",self.login_confirmation_xpath):
            self.logger.info("Login successful, confirmation element is displayed.")
            return True
        else:
            self.logger.error("Login failed, confirmation element is not displayed.")
            return False

    def logout(self):
        """Log out of the account."""
        self.element_click("my_account_menu_xpath", self.my_account_menu_xpath)
        # This is a placeholder. Replace with actual steps to log out.
        self.element_click("logout_option_xpath", self.logout_option_xpath)
        self.logger.info("Logged out of the account.")

    def logout_confirmation(self):
        if self.check_display_status("logout_confirmation_xpath",self.logout_confirmation_xpath):
            self.logger.info("Logout successful, confirmation element is displayed.")
            return True
        else:
            self.logger.error("Logout failed, confirmation element is not displayed.")
            return False