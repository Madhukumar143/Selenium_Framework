from Tests.baseTest import baseTest
from Pages.homePage import HomePage


class TestSearch(baseTest):
    def test_search_mac(self,logger):
        # rely on self.driver provided by baseTest's fixtures
        homepage = HomePage(self.driver)
        homepage.search_for("mac")
        # Wait for results to appear using basePage's explicit_wait
        homepage.explicit_wait(homepage.product_caption_links_xpath)
        results = homepage.get_search_results_texts()  # ["mac m1 " , "mac m2"]
        assert results, "No search results were returned"
        assert any('mac' in r.lower() for r in results), f"No product with 'mac' found. Results: {results}"

    def test_add_to_cart(self,logger):
        homepage = HomePage(self.driver)
        homepage.search_for("mac")
        homepage.click_on_product()
        product_code = homepage.retrieve_product_code()
        homepage.click_add_to_cart()
        assert homepage.confirm_added_to_cart(),"Failed to confirm that product was added to cart."
        homepage.navigate_to_shopping_cart()
        assert homepage.verify_product_in_cart(product_code), "Product with code 43 was not found in the cart."