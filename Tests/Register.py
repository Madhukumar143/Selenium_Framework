from Tests.baseTest import baseTest
from Pages.registerPage import registerPage
import Variables as var
from utils.logger import Logger

class TestLogin(baseTest):

    def test_register_user(self,logger):
        # rely on self.driver provided by baseTest's fixtures
        register_page = registerPage(self.driver)
        register_page.navigate_to_register_page()
        logger.info("Logout Completed")
        assert register_page.register_page_confirmation(), "Register page confirmation failed."
        register_page.register(var.first_name, var.last_name,var.generate_email(), var.telephone,var.password, var.subscribe)
        assert register_page.registration_confirmation(), "Registration confirmation failed."