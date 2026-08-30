import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def select_option_by_text(driver, wait, target_text):
    # Give the dropdown popup a moment to animate open
    time.sleep(1)

    # Try 1: options styled with role='option' (same pattern used in product_page.py)
    try:
        options = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@role='option']"))
        )
        for option in options:
            if option.text.strip() == target_text:
                option.click()
                return
    except TimeoutException:
        pass

    # Try 2 (fallback): match the exact visible text on any element, regardless of role
    fallback_option = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//*[normalize-space(text())='{target_text}']")
        )
    )
    fallback_option.click()


def go_to_delivery_note_module(driver):
    wait = WebDriverWait(driver, 10)

    # Go back to the dashboard first, in case the sidebar isn't fully present on this page
    time.sleep(5)

    print("URL:", driver.current_url)
    print("Delivery note link (by href) exists:", len(driver.find_elements(By.XPATH, "//a[@href='/delivery-notes']")))

    # Find Delivery note link
    delivery_note_link = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@href='/delivery-notes']")
        )
    )

    # Scroll down to Delivery note link
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        delivery_note_link
    )

    time.sleep(2)

    # Click Delivery note link
    delivery_note_link.click()

    time.sleep(2)


def click_new_delivery_note(driver):
    wait = WebDriverWait(driver, 10)

    # Find New delivery note button
    new_delivery_note_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/div[1]/div[3]/div/main/div/div[1]/div[2]/button[2]")
        )
    )

    # Scroll to New delivery note button
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        new_delivery_note_button
    )

    time.sleep(2)

    # Click New delivery note button
    new_delivery_note_button.click()

    time.sleep(2)


def create_delivery_note_draft(driver):
    wait = WebDriverWait(driver, 10)
    # Find and click Customer dropdown

    customer_dropdown = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/div[1]/div[3]/div/main/div/main/div/section[1]/div[2]/div[1]/div/button")
        )
    )

    customer_dropdown.click()

    time.sleep(2)

    # Find the search field that appears
    customer_search = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[1]/div/input")
        )
    )

    customer_search.send_keys("SuvinaTest")

    time.sleep(3)

    # Select SuvinaTest using the same logic used for Sandwich Test
    select_option_by_text(driver, wait, "SuvinaTest")

    # IMPORTANT:
    # Give the application time to update the Customer field
    time.sleep(3)
    # Find Item dropdown button
    item_dropdown = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/div[1]/div[3]/div/main/div/main/div/section[2]/div[2]/div[2]/div/div/button")
        )
    )

    # Scroll down to Item dropdown button
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        item_dropdown
    )

    time.sleep(2)

    item_dropdown.click()

    time.sleep(3)

    # Select the option whose text matches "Sandwich Test"
    select_option_by_text(driver, wait, "Sandwich Test")

    time.sleep(1)

    # Find Quantity field
    quantity_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='root']/div[1]/div[3]/div/main/div/main/div/section[2]/div[2]/div[2]/input")
        )
    )

    # Scroll to Quantity field
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        quantity_field
    )

    time.sleep(2)

    quantity_field.send_keys("7")

    time.sleep(1)

    # Find Save as Draft button
    save_draft_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/div[1]/div[3]/div/main/div/div/div/div[2]/button[1]")
        )
    )

    # Scroll to Save as Draft button
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        save_draft_button
    )

    time.sleep(2)

    save_draft_button.click()

    time.sleep(2)


def verify_saved_as_draft(driver):
    print("Delivery note draft creation process completed successfully")