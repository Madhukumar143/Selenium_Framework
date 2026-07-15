from Tests.baseTest import baseTest
from Pages.login_page import LoginPage
import Variables as var

class TestLogin(baseTest):

    def test_valid_login(self):
        loginpage = LoginPage(self.driver)
        loginpage.navigate_to_login_page()
        self.logger.info("Logged in")
        assert loginpage.login_page_confirmation(), "Login page navigation failed"
        loginpage.login(var.login_user_1_email,var.password_user_1)
        assert loginpage.login_confirmation() , "Login failed with valid  credentials"
        loginpage.logout()
        assert loginpage.logout_confirmation(),"Logout failed"

    def test_invalid_login(self):
        loginpage = LoginPage(self.driver)
        loginpage.navigate_to_login_page()
        assert loginpage.login_page_confirmation(), "Navigation to login page failed"
        loginpage.login(var.login_user_1_email,var.password)
        assert not(loginpage.login_confirmation()) , "Logged in with invalid credentials"


