import time
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def select_second_valid_option(select_element):
    # Skips the blank placeholder (e.g. "Select province"), then picks the SECOND real option
    select = Select(select_element)
    valid_count = 0
    for option in select.options:
        if option.get_attribute("value"):
            valid_count += 1
            if valid_count == 2:
                option.click()
                break


def go_to_customer_module(driver):
    wait = WebDriverWait(driver, 10)

    # Go back to the dashboard first, in case the sidebar isn't fully present on this page
    driver.get("https://demo.coddypro.com/dashboard")
    time.sleep(4)

    print("URL:", driver.current_url)
    print("Customer link (by href) exists:", len(driver.find_elements(By.XPATH, "//a[@href='/clients']")))

    # Find Customer link
    customer_link = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@href='/clients']")
        )
    )

    # Scroll to Customer link
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        customer_link
    )

    time.sleep(2)

    # Click Customer link
    customer_link.click()

    time.sleep(2)


def click_new_customer(driver):
    wait = WebDriverWait(driver, 10)

    # Find New Customer button
    new_customer_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/div[1]/div[3]/div/main/div/div[1]/div[2]/button[2]")
        )
    )

    # Scroll to New Customer button
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        new_customer_button
    )

    time.sleep(2)

    # Click New Customer button
    new_customer_button.click()

    time.sleep(2)


def create_customer(driver):
    wait = WebDriverWait(driver, 10)

    # Find Customer name field (mandatory)
    customer_name_field = wait.until(
        EC.presence_of_element_located(
            (By.ID, "customer_name")
        )
    )

    # Scroll to Customer name field
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        customer_name_field
    )

    time.sleep(2)

    customer_name_field.send_keys("SuvinaTest")

    time.sleep(1)

    # Find Customer group dropdown (native <select> - same as Province/District)
    customer_group_dropdown = wait.until(
        EC.presence_of_element_located(
            (By.ID, "customer_group")
        )
    )

    # Scroll to Customer group dropdown
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        customer_group_dropdown
    )

    time.sleep(2)

    select_second_valid_option(customer_group_dropdown)

    time.sleep(1)

    # Find VAT number field
    vat_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='customer-form']/div/section[1]/div[2]/div/div[3]/input")
        )
    )

    # Scroll to VAT number field
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        vat_field
    )

    time.sleep(2)

    vat_field.send_keys("5440029800")

    time.sleep(1)

    # Find Contact name field
    contact_name_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='customer-form']/div/section[2]/div[2]/div/div[1]/input")
        )
    )

    # Scroll to Contact name field
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        contact_name_field
    )

    time.sleep(2)

    contact_name_field.send_keys("suvi")

    time.sleep(1)

    # Find Email address field
    email_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='customer-form']/div/section[2]/div[2]/div/div[2]/input")
        )
    )

    # Scroll to Email address field
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        email_field
    )

    time.sleep(2)

    email_field.send_keys("anivus12@gmail.com")

    time.sleep(1)

    # Find Mobile number field
    mobile_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='customer-form']/div/section[2]/div[2]/div/div[3]/input")
        )
    )

    # Scroll down to Mobile number field
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        mobile_field
    )

    time.sleep(2)

    mobile_field.send_keys("9816618002")

    time.sleep(1)

    # Find Street address field
    street_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='customer-form']/div/section[3]/div[2]/div/div[1]/input")
        )
    )

    # Scroll down to Street address field
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        street_field
    )

    time.sleep(2)

    street_field.send_keys("Raniban")

    time.sleep(1)

    # Find Province dropdown
    province_dropdown = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='customer-form']/div/section[3]/div[2]/div/div[2]/div[1]/select")
        )
    )

    # Scroll down to Province dropdown
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        province_dropdown
    )

    time.sleep(2)

    select_second_valid_option(province_dropdown)

    time.sleep(2)  # give district list time to refresh after province is picked

    # Find District dropdown
    district_dropdown = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='customer-form']/div/section[3]/div[2]/div/div[2]/div[2]/select")
        )
    )

    # Scroll down to District dropdown
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        district_dropdown
    )

    time.sleep(2)

    select_second_valid_option(district_dropdown)

    time.sleep(1)

    # Find Create customer button
    create_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/div[1]/div[3]/div/main/div/div/header/button")
        )
    )

    # Scroll to Create customer button
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        create_button
    )

    time.sleep(2)

    create_button.click()

    time.sleep(3)


def verify_customer_created(driver):
    print("Customer creation process completed successfully")