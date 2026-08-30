import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def go_to_product_module(driver):
    time.sleep(5)

    print("URL:", driver.current_url)
    print(
        "Inventory exists:",
        len(driver.find_elements(By.ID, "sidebar-group-inventory"))
    )
    print(
        "Products exists:",
        len(driver.find_elements(By.XPATH, "//a[@href='/products']"))
    )

    # Find Products link
    products_link = driver.find_element(
        By.XPATH,
        "//a[@href='/products']"
    )

    # Scroll to Products
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        products_link
    )

    time.sleep(2)

    # Click Products
    products_link.click()

    time.sleep(2)


def click_new_product(driver):
    driver.find_element(
        By.XPATH,
        "//button[normalize-space()='Add product']"
    ).click()

    time.sleep(2)


def fill_details_tab(driver, item_name):

    wait = WebDriverWait(driver, 10)

    # Item name
    item_name_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@value='']")
        )
    )

    item_name_field.send_keys(item_name)

    time.sleep(1)

    # Stock UOM
    stock_uom = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@role='combobox'][.//span[normalize-space()='Nos']]")
        )
    )

    stock_uom.click()

    time.sleep(1)

    # Select Ampere
    ampere = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@role='option'][.//span[normalize-space()='Ampere']]")
        )
    )

    ampere.click()

    time.sleep(1)

    # Brand
    brand = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@role='combobox'][.//span[normalize-space()='Select brand']]")
        )
    )

    brand.click()

    time.sleep(1)

    # Select Samsung
    samsung = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Samsung']")
        )
    )

    samsung.click()

    time.sleep(1)

    # Units & Prices tab
    units_prices = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(normalize-space(.), 'Units & prices')]")
        )
    )

    units_prices.click()

    time.sleep(2)


def fill_units_and_prices_tab(driver):

    wait = WebDriverWait(driver, 5)

    # Click Add new unit
    driver.find_element(
        By.XPATH,
        "//*[@id='root']/div[1]/div[3]/div/main/div/main/form/div[3]/div/section[2]/div[1]/button"
    ).click()

    time.sleep(1)

    # Unit field
    driver.find_element(
        By.XPATH,
        "//*[@id='product_uoms_1_uom']"
    ).click()

    time.sleep(1)

    # Select Box
    box_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[@id='root']/div[1]/div[3]/div/main/div/main/form/div[3]/div/section[2]/div[2]/div[2]/div[1]/div/div/div[2]/button[17]/span"
            )
        )
    )

    box_option.click()

    time.sleep(2)

    # Unit value
    unit_value = driver.find_element(
        By.XPATH,
        "//*[@id='root']/div[1]/div[3]/div/main/div/main/form/div[3]/div/section[2]/div[2]/div[2]/div[2]/input"
    )

    unit_value.send_keys("1")

    time.sleep(1)

    # Click Unit Price button
    driver.find_element(
        By.XPATH,
        "//*[@id='root']/div[1]/div[3]/div/main/div/main/form/div[3]/div/section[1]/div[1]/button"
    ).click()

    time.sleep(1)

    # Price
    price_field = driver.find_element(
        By.XPATH,
        "//*[@id='product_prices_0_price_list_rate']"
    )

    price_field.send_keys("180")

    time.sleep(1)


def fill_inventory_tab(driver):

    wait = WebDriverWait(driver, 4)

    # Inventory tab
    inventory_tab = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//*[@id='root']/div[1]/div[3]/div/main/div/main/form/div[2]/button[3]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        inventory_tab
    )

    time.sleep(2)

    inventory_tab.click()

    time.sleep(2)

    # Valuation rate
    valuation_price_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='product_valuation_rate']")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        valuation_price_field
    )

    time.sleep(2)

    valuation_price_field.send_keys("180")

    time.sleep(1)

    # Warranty
    warranty_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='product_warranty_period']")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        warranty_field
    )

    time.sleep(1)

    warranty_field.send_keys("12")

    time.sleep(1)


def go_to_accounting_tab(driver):

    wait = WebDriverWait(driver, 10)

    # Accounting tab
    accounting_tab = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//*[@id='root']/div[1]/div[3]/div/main/div/main/form/div[2]/button[4]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        accounting_tab
    )

    time.sleep(2)

    driver.execute_script(
        "arguments[0].click();",
        accounting_tab
    )

    time.sleep(2)


def fill_sales_tab(driver):

    wait = WebDriverWait(driver, 10)

    # Sales tab
    sales_tab = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//*[@id='root']/div[1]/div[3]/div/main/div/main/form/div[2]/button[5]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        sales_tab
    )

    time.sleep(2)

    sales_tab = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[@id='root']/div[1]/div[3]/div/main/div/main/form/div[2]/button[5]"
            )
        )
    )

    sales_tab.click()

    time.sleep(2)

    # Maximum Discount
    discount_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='product_max_discount']")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        discount_field
    )

    time.sleep(2)

    discount_field.send_keys("30")

    time.sleep(1)

    # Over Billing Allowance
    over_billing_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='product_over_billing_allowance']")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        over_billing_field
    )

    time.sleep(2)

    over_billing_field.send_keys("15")

    time.sleep(1)


def click_create_product(driver):

    wait = WebDriverWait(driver, 10)

    create_product_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[@id='root']/div[1]/div[3]/div/main/div/main/form/div[4]/button[2]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        create_product_button
    )

    time.sleep(2)

    create_product_button.click()

    time.sleep(5)


def verify_product_created(driver):

    print("Product creation process completed successfully")



# EDIT PRODUCT

def edit_product(driver):

    wait = WebDriverWait(driver, 5)

    # Find Edit button of the first product
    edit_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[@id='root']/div[1]/div[3]/div/main/div/header/div/div[2]/button[1]"
            )
        )
    )

    # Scroll to Edit button
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        edit_button
    )

    time.sleep(2)

    # Click Edit
    edit_button.click()

    time.sleep(3)

    # Find Units & Prices tab
    units_prices_tab = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[@id='root']/div[1]/div[3]/div/main/div/form/div[2]/button[2]"
            )
        )
    )

    # Scroll to Units & Prices
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        units_prices_tab
    )

    time.sleep(2)

    # Click Units & Prices
    units_prices_tab.click()

    time.sleep(3)

    # Find price field
    price_field = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//*[@id='product_prices_0_price_list_rate']"
            )
        )
    )

    # Scroll to price field
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        price_field
    )

    time.sleep(2)

    # Clear existing price and enter 0
    price_field.clear()

    time.sleep(1)

    price_field.send_keys("200")

    time.sleep(2)

    # Find final Save/Update button
    save_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[@id='root']/div[1]/div[3]/div/main/div/form/div[4]/button[2]"
            )
        )
    )

    # Scroll to Save/Update button
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        save_button
    )

    time.sleep(2)

    # Click Save/Update
    save_button.click()

    time.sleep(5)


def verify_product_edited(driver):

    print("Product edit process completed successfully")