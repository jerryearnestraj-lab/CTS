from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SimpleFormPage(BasePage):

    MESSAGE_INPUT = (By.ID, "user-message")

    SUBMIT_BUTTON = (By.ID, "showInput")

    DISPLAY_MESSAGE = (By.ID, "message")


    def enter_message(self, text):

        element = self.wait_for_element(self.MESSAGE_INPUT)

        element.clear()

        element.send_keys(text)


    def click_submit(self):

        button = self.wait_for_element(self.SUBMIT_BUTTON)

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )


    def get_displayed_message(self):

        return self.wait_for_element(
            self.MESSAGE_INPUT
        ).get_attribute("value")