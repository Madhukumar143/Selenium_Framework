from Tests.baseTest import baseTest
from Pages.login_page import LoginPage
import Variables

class TestLogin(baseTest):

    def test_valid_login(self):
        # rely on self.driver provided by baseTest's fixtures
        login_page = LoginPage(self.driver)
        login_page.navigate_to_login_page()
        assert login_page.login_page_confirmation(), "Login page confirmation failed."
        login_page.login(Variables.login_user_1_email, Variables.password_user_1)
        assert login_page.login_confirmation(), "Login confirmation failed."
        login_page.logout()
        assert login_page.logout_confirmation() , "Logout confirmation failed."

    def test_invalid_login(self,logger):
        login_page = LoginPage(self.driver)
        login_page.navigate_to_login_page()
        assert login_page.login_page_confirmation(), "Login page confirmation failed."
        login_page.login(Variables.login_user_1_email, Variables.password_user_1)
        assert not(login_page.login_confirmation()), "Login successful with invalid credentials, which is unexpected."