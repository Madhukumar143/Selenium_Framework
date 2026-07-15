import time

from Pages.basePage import basePage
from selenium.webdriver.common.keys import Keys


class HomePage(basePage):
    # Locator(s) - names must end with _xpath

    def __init__(self, driver):
        super().__init__(driver)

    searchbar_xpath = "//input[@placeholder='Search']"
    product_caption_links_xpath = "//div[@class='caption']//a"
    #button_id = "button_id"
    macbook_xpath = "//a[normalize-space()='MacBook']"
    imac_xpath = "//a[normalize-space()='iMac']"
    add_to_cart_xpath = "//button[@id='button-cart']"
    added_to_cart_confirmation_xpath = "//div[@class='alert alert-success alert-dismissible']"
    shopping_cart_xpath = "//span[normalize-space()='Shopping Cart']"
    product_code_xpath = "//li[contains(text(),'Product Code')]"

    def search_for(self, text):
        """Type text into the search bar and submit the search using basePage helpers."""
        # Use basePage helper to type into element (click, clear, send keys)
        self.type_into_element(text, "searchbar_xpath", self.searchbar_xpath)
        # Press Enter on the search input to submit
        elem = self.get_element("searchbar_xpath", self.searchbar_xpath)
        if elem:
            elem.send_keys(Keys.ENTER)
        self.logger.info(f"Searched for '{text}' in the search bar.")

    def get_search_results_texts(self):
        """Return a list of visible product title texts from search results."""
        elements = self.get_elements(self.product_caption_links_xpath) # mac m1 , mac m2
        for el in elements:
            print(el.text)
        self.logger.info("Searched successfully")
        return [el.text for el in elements if el and el.text]

    def click_on_product(self):
        self.element_click("imac_xpath",self.imac_xpath)
        self.logger.info("Clicked on the MacBook product link.")

    def click_add_to_cart(self):
        self.element_click("add_to_cart_xpath", self.add_to_cart_xpath)
        self.logger.info("Clicked on the Add to Cart button for MacBook.")

    def retrieve_product_code(self):
        # extract product code from here
        product_code = self.retrieve_element_text("product_code_xpath", self.product_code_xpath)
        actual_product_code = product_code.split(":")[1]
        return actual_product_code

    def confirm_added_to_cart(self):
        if self.check_display_status("added_to_cart_confirmation_xpath",self.added_to_cart_confirmation_xpath):
            self.logger.info("Product was successfully added to the cart, confirmation message is displayed.")
            return True
        else:
            self.logger.error("Product was not added to the cart, confirmation message is not displayed.")
            return False

    def navigate_to_shopping_cart(self):
        self.element_click("shopping_cart_xpath", self.shopping_cart_xpath)
        self.logger.info("Navigated to the shopping cart page.")

    def verify_product_in_cart(self,product_code):
        # include dynamic product code in xpath
        product_code_xpath = f"//td[normalize-space()='{product_code}']"
        if self.check_display_status("product_code_xpath", product_code_xpath):
            self.logger.info("Product with code is present in the cart.")
            return True
        else:
            self.logger.error("Product with code is not present in the cart.")
            return False
