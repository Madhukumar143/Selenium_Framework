from Pages.login_page import LoginPage
from Tests.baseTest import baseTest
from Pages.homePage import HomePage
import Variables as var

class TestSearch(baseTest):
    def test_search_mac(self,logger):
        # rely on self.driver provided by baseTest's fixtures
        loginpage = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        loginpage.navigate_to_login_page()
        loginpage.login(var.login_user_1_email,var.password_user_1)
        homepage.search_for("mac")
        search_results = homepage.get_search_results_texts()#["Mac m1" , "mac m2"]
        assert search_results, "No search results were returned"
        assert any('mac' in r.lower() for r in search_results), f"No product with 'mac' found. Results: {results}"

    def test_add_to_cart(self,logger):
        homepage = HomePage(self.driver)
        homepage.search_for("mac")
        homepage.click_on_product()
        product_code = homepage.retrieve_product_code()
        homepage.click_add_to_cart()
        assert homepage.confirm_added_to_cart(),"Failed to confirm that product was added to cart."
        homepage.navigate_to_shopping_cart()
        assert homepage.verify_product_in_cart(product_code), "Product with code 43 was not found in the cart."