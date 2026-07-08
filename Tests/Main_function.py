import time
from Pages.basePage import basePage

class Common_functions(basePage):

    def __init__(self, driver):
        super().__init__(driver)

    profile_xpath = "//div[@class='gi-header-icon']"
    logout_option_xpath = "//span[normalize-space()='Logout']"
    goto_prev_month_button_xpath = "//button[@aria-label='Previous Month']"
    goto_next_month_button_xpath = "//button[@aria-label='Next Month']"
    present_month_xpath = "//button[@aria-label='Choose Month']"
    present_year_xpath = "//button[@aria-label='Choose Year']"

    def date_picker_from_calendar_popUp(self,date,Actual_month,Actual_year):
        Month_dictionary = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
                            "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
        time.sleep(2)
        initial_month = self.retrieve_element_text("present_month_xpath",self.present_month_xpath)
        initial_year = self.retrieve_element_text("present_year_xpath",self.present_year_xpath)
        while True:
            time.sleep(2)
            year = self.retrieve_element_text("present_month_xpath",self.present_year_xpath)
            Month = self.retrieve_element_text("present_year_xpath",self.present_month_xpath)
            if int(initial_year) > Actual_year:
                if (int(year) != Actual_year):
                    self.element_click("goto_prev_month_button_xpath",self.goto_prev_month_button_xpath)
                    #time.sleep(2)
                else:
                    if (Month) != Actual_month:
                        self.element_click("goto_prev_month_button_xpath", self.goto_prev_month_button_xpath)
                        #time.sleep(2)
                    else:
                        break
            elif int(initial_year) < Actual_year:
                if (int(year) != Actual_year):
                    self.element_click("goto_next_month_button_xpath",self.goto_next_month_button_xpath)
                    #time.sleep(2)
                else:
                    if (Month) != Actual_month:
                        self.element_click("goto_next_month_button_xpath", self.goto_next_month_button_xpath)
                        #time.sleep(2)
                    else:
                        break
            else:
                if Month_dictionary[initial_month] > Month_dictionary[Actual_month]:
                    if Month != Actual_month:
                        self.element_click("goto_prev_month_button_xpath", self.goto_prev_month_button_xpath)
                        #time.sleep(2)

                    else:
                        break
                elif Month_dictionary[initial_month] < Month_dictionary[Actual_month]:
                    if Month != Actual_month:
                        self.element_click("goto_next_month_button_xpath", self.goto_next_month_button_xpath)
                        #time.sleep(2)
                    else:
                        break
                else:
                    break

        date_xpath = "(//span[normalize-space()="+str(date)+"])[1]"
        time.sleep(1)
        self.element_click("date_xpath", date_xpath)










