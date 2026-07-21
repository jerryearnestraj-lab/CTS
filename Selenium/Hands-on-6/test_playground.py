import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# -------------------------------------------------------
# Task 42 & 45
# -------------------------------------------------------

@pytest.mark.parametrize(
    "message",
    [
        "Hello",
        "Hi",
        "CTS"
    ]
)
def test_simple_form_submission(driver, base_url, message):

    driver.get(base_url + "simple-form-demo")

    textbox = driver.find_element(By.ID, "user-message")

    textbox.clear()
    textbox.send_keys(message)

    button = driver.find_element(By.ID, "showInput")

    driver.execute_script(
        "arguments[0].scrollIntoView(true);",
        button
    )

    time.sleep(1)

    driver.execute_script(
        "arguments[0].click();",
        button
    )

    time.sleep(2)

    output = driver.find_element(By.ID, "message").text.strip()

    print("\nExpected :", message)
    print("Actual   :", output)

    assert output == message


# -------------------------------------------------------
# Task 43
# -------------------------------------------------------

def test_checkbox_demo(driver, base_url):

    driver.get(base_url + "checkbox-demo")

    checkbox = driver.find_element(
        By.XPATH,
        "(//input[@type='checkbox'])[1]"
    )

    checkbox.click()
    assert checkbox.is_selected()

    checkbox.click()
    assert not checkbox.is_selected()


# -------------------------------------------------------
# Task 49
# -------------------------------------------------------

def test_dropdown_selection(driver, base_url):

    driver.get(base_url + "select-dropdown-demo")

    dropdown = Select(
        driver.find_element(
            By.ID,
            "select-demo"
        )
    )

    dropdown.select_by_visible_text("Wednesday")

    assert dropdown.first_selected_option.text == "Wednesday"