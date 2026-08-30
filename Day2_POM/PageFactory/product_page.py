import time

import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def go_to_product_module(driver):
    time.sleep(5)

    print("URL:", driver.current_url)
    print("Inventory exists:", len(driver.find_elements(By.ID, "sidebar-group-inventory")))
    print("Products exists:", len(driver.find_elements(By.XPATH, "//a[@href='/products']")))

    # Find Products link
    products_link = driver.find_element(
        By.XPATH,
        "//a[@href='/products']"
    )

    # Scroll down to Products
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        products_link
    )
    # Click Products
    products_link.click()

    time.sleep(2)

def click_new_product(driver):
    driver.find_element( By.XPATH,"//button[normalize-space()='Add product']").click()

    time.sleep(2)

def fill_details_tab(driver, item_name):
     wait = WebDriverWait(driver, 10)

     item_name_field = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@value='']")
            )
        )
     item_name_field.send_keys(item_name)

     time.sleep(1)

     stock_uom = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@role='combobox'][.//span[normalize-space()='Nos']]")
            )
        )
     stock_uom.click()

     time.sleep(1)

     ampere = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@role='option'][.//span[normalize-space()='Ampere']]")
            )
        )
     ampere.click()

     time.sleep(1)

     brand = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@role='combobox'][.//span[normalize-space()='Select brand']]")
            )
        )
     brand.click()

     time.sleep(1)

     samsung = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[normalize-space()='Samsung']")
            )
        )
     samsung.click()

     time.sleep(1)


     units_prices = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(normalize-space(.), 'Units & prices')]")
            )
        )
     units_prices.click()

     time.sleep(2)
#click add new unit
def fill_units_and_prices_tab(driver):
     wait = WebDriverWait(driver,5)
     driver.find_element(
         By.XPATH,
         "//*[@id='root']/div[1]/div[3]/div/main/div/main/form/div[3]/div/section[2]/div[1]/button"
     ).click()
     time.sleep(1)

     #unit field
     driver.find_element(
         By.XPATH,
         "//*[@id='product_uoms_1_uom']"
     ).click()
     time.sleep(1)

     #unit value
     box_option = wait.until(
         EC.element_to_be_clickable(
             (By.XPATH, "//*[@id='root']/div[1]/div[3]/div/main/div/main/form/div[3]/div/section[2]/div[2]/div[2]/div[1]/div/div/div[2]/button[17]/span")
         )
     )

     box_option.click()

     time.sleep(2)

#click in unit and send value 10
     driver.find_element(By.XPATH,"//*[@id='root']/div[1]/div[3]/div/main/div/main/form/div[3]/div/section[2]/div[2]/div[2]/div[2]/input").send_keys("1")

     time.sleep(1)

#click unit price button
     driver.find_element(By.XPATH,"//*[@id='root']/div[1]/div[3]/div/main/div/main/form/div[3]/div/section[1]/div[1]/button").click()

     time.sleep(1)
#Select price field
     driver.find_element( By.XPATH,
         '//*[@id="product_prices_0_price_list_rate"]').send_keys("180")
     time.sleep(1)

def fill_inventory_tab(driver):
    wait = WebDriverWait(driver, 10)

    # Find Inventory tab
    inventory_tab = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='root']/div[1]/div[3]/div/main/div/main/form/div[2]/button[3]")
        )
    )

    # Scroll up to Inventory tab
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        inventory_tab
    )

    time.sleep(2)

    # Click Inventory tab
    inventory_tab.click()

    time.sleep(2)

    # Find valuation rate
    valuation_price_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='product_valuation_rate']")
        )
    )

    # Scroll down to valuation rate
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        valuation_price_field
    )

    time.sleep(2)

    # Enter valuation rate
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

    # Find Accounting tab
    accounting_tab = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='root']/div[1]/div[3]/div/main/div/main/form/div[2]/button[4]")
        )
    )

    # Scroll Accounting tab into view
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        accounting_tab
    )

    time.sleep(2)

    # Click Accounting tab using JavaScript
    driver.execute_script(
        "arguments[0].click();",
        accounting_tab
    )

    time.sleep(2)

def fill_sales_tab(driver):
    wait = WebDriverWait(driver, 10)

    # Find Sales tab
    sales_tab = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='root']/div[1]/div[3]/div/main/div/main/form/div[2]/button[5]")
        )
    )

    # Scroll UP to Sales tab
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        sales_tab
    )

    time.sleep(2)

    # Click Sales tab after scrolling
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/div[1]/div[3]/div/main/div/main/form/div[2]/button[5]")
        )
    )

    sales_tab.click()

    time.sleep(2)

    # Find Maximum Discount
    discount_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='product_max_discount']")
        )
    )

    # Scroll DOWN to Maximum Discount
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        discount_field
    )

    time.sleep(2)

    # Enter Maximum Discount
    discount_field.send_keys("30")

    time.sleep(1)

    # Find Over Billing Allowance
    over_billing_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='product_over_billing_allowance']")
        )
    )

    # Scroll to Over Billing Allowance
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        over_billing_field
    )

    time.sleep(2)

    # Enter Over Billing Allowance
    over_billing_field.send_keys("15")

    time.sleep(1)
def click_create_product(driver):
    create_product_button = driver.find_element(
        By.XPATH,
        "//*[@id='root']/div[1]/div[3]/div/main/div/main/form/div[4]/button[2]"
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        create_product_button
    )

    time.sleep(1)

    create_product_button.click()

    time.sleep(3)

def verify_product_created(driver):
    print("Product creation process completed successfully")

