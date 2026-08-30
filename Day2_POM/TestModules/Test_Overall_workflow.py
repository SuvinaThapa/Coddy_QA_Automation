import sys
import os
import time

# Let this file find the PageFactory and TestSetups folders
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "PageFactory"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "TestSetups"))

import setup
import login_page
import customer_page
import product_page
import delivery_note_modal
import Task_and_remainder_modal

# Step 1: Initialize WebDriver
driver = setup.get_driver()

# Step 2: Login
login_page.open_login_page(driver)
login_page.login(driver, "testingforcoddy15@gmail.com", "Testingcoddy@123")
login_page.verify_login_success(driver)

# Step 3: Create Product - fill each tab (matches your actual product_page.py)
product_page.go_to_product_module(driver)
product_page.click_new_product(driver)
product_page.fill_details_tab(driver, item_name="Sandwich Test")
product_page.fill_units_and_prices_tab(driver)
product_page.fill_inventory_tab(driver)
product_page.go_to_accounting_tab(driver)
product_page.fill_sales_tab(driver)
product_page.click_create_product(driver)
product_page.verify_product_created(driver)

# Step 4: Add Customer (details filled inside create_customer)
customer_page.go_to_customer_module(driver)
customer_page.click_new_customer(driver)
customer_page.create_customer(driver)
customer_page.verify_customer_created(driver)

# Step 5: Create Delivery Note as Draft
delivery_note_modal.go_to_delivery_note_module(driver)
delivery_note_modal.click_new_delivery_note(driver)
delivery_note_modal.create_delivery_note_draft(driver, customer="Suvina", item="Sandwich", quantity=6)
delivery_note_modal.verify_saved_as_draft(driver)

# Step 6: Create Task
Task_and_remainder_modal.go_to_task_module(driver)
Task_and_remainder_modal.click_new_task(driver)
Task_and_remainder_modal.create_task(driver, title="Complete Report", priority="Medium")

# Step 7: Edit the task and add a reminder (Before task is due, send before 2)
Task_and_remainder_modal.open_task_for_edit(driver, "Complete Report")
Task_and_remainder_modal.add_reminder_before_due(driver, send_before=2)

# Step 8: Delete the task (with confirmation popup)
Task_and_remainder_modal.delete_task(driver, "Complete Report")
Task_and_remainder_modal.verify_task_deleted(driver, "Complete Report")

time.sleep(2)

# Step 9: Close Browser
driver.quit()