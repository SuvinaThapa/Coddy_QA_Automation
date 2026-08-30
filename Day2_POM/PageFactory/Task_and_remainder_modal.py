import time
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def select_second_valid_option(select_element):
    # Skips the blank placeholder, then picks the SECOND real option
    select = Select(select_element)
    valid_count = 0
    for option in select.options:
        if option.get_attribute("value"):
            valid_count += 1
            if valid_count == 2:
                option.click()
                break


def select_tomorrow_date(driver, wait):
    # NOTE: verify this locator - assumes the calendar's day cells are buttons
    # whose visible text is just the day number (e.g. "15"). Common for Radix/shadcn
    # calendars, but confirm with SelectorsHub before trusting this on a month boundary.
    tomorrow = datetime.now() + timedelta(days=1)
    day_number = str(tomorrow.day)

    day_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//button[normalize-space(text())='{day_number}']")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        day_button
    )

    time.sleep(2)

    day_button.click()

    time.sleep(1)


def go_to_task_module(driver):
    wait = WebDriverWait(driver, 10)

    # Go back to the dashboard first, in case the sidebar isn't fully present on this page
    driver.get("https://demo.coddypro.com/dashboard")
    time.sleep(5)

    print("URL:", driver.current_url)
    print("Task link (by href) exists:", len(driver.find_elements(By.XPATH, "//a[@href='/tasks']")))

    # Find Task & Reminder link
    task_link = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@href='/tasks']")
        )
    )

    # Scroll up to Task & Reminder link
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        task_link
    )

    time.sleep(2)

    # Click Task & Reminder link
    task_link.click()

    time.sleep(2)


def click_new_task(driver):
    wait = WebDriverWait(driver, 10)

    # Find Add task button
    add_task_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='root']/div[1]/div[3]/div/main/div/header/div[2]/button[2]")
        )
    )

    # Scroll to Add task button
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        add_task_button
    )

    time.sleep(2)

    # Click Add task button
    add_task_button.click()

    time.sleep(2)


def create_task(driver):
    wait = WebDriverWait(driver, 10)

    # Wait for the modal to open
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='radix-:r4k:']")
        )
    )

    time.sleep(1)

    # Find Title field
    title_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='radix-:r4k:']/div[2]/div/section[1]/div[2]/input")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        title_field
    )

    time.sleep(2)

    title_field.send_keys("AutomationSuv Task")

    time.sleep(1)

    # Find Description field
    description_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='radix-:r4k:']/div[2]/div/section[1]/div[3]/textarea")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        description_field
    )

    time.sleep(2)

    description_field.send_keys("i have complete 3 module and now trying this task module")

    time.sleep(1)

    # Find Task type dropdown
    task_type_dropdown = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='radix-:r4k:']/div[2]/div/section[1]/div[4]/div[1]/select")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        task_type_dropdown
    )

    time.sleep(2)

    select_second_valid_option(task_type_dropdown)

    time.sleep(1)

    # Find Status dropdown
    status_dropdown = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='radix-:r4k:']/div[2]/div/section[1]/div[4]/div[2]/select")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        status_dropdown
    )

    time.sleep(2)

    select_second_valid_option(status_dropdown)

    time.sleep(1)

    # Find Due date button
    due_date_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='radix-:r4k:']/div[2]/div/section[2]/div[4]/button[2]")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        due_date_button
    )

    time.sleep(2)

    due_date_button.click()

    time.sleep(1)

    # Select tomorrow's date in the calendar that opens
    select_tomorrow_date(driver, wait)

    # Find Add reminder button
    add_reminder_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='radix-:r4k:']/div[2]/div/section[3]/div/button")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        add_reminder_button
    )

    time.sleep(2)

    add_reminder_button.click()

    time.sleep(1)

    # Find Schedule dropdown
    schedule_dropdown = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='radix-:r4k:']/div[2]/div/section[3]/div[2]/div[1]/div[1]/select")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        schedule_dropdown
    )

    time.sleep(2)

    select_second_valid_option(schedule_dropdown)

    time.sleep(1)

    # Find Send before number field
    send_before_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='radix-:r4k:']/div[2]/div/section[3]/div[2]/div[2]/div[1]/input")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        send_before_field
    )

    time.sleep(2)

    send_before_field.send_keys("2")

    time.sleep(1)

    # Find Unit dropdown (Hour/Day/etc.)
    unit_dropdown = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='radix-:r4k:']/div[2]/div/section[3]/div[2]/div[2]/div[2]/select")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        unit_dropdown
    )

    time.sleep(2)

    select_second_valid_option(unit_dropdown)

    time.sleep(1)

    # Find final Create/Save button
    create_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='radix-:r4k:']/div[3]/button[2]")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        create_button
    )

    time.sleep(2)

    create_button.click()

    time.sleep(2)


def verify_task_created(driver):
    print("Task creation process completed successfully")