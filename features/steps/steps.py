import time
from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from features.steps.maps import ACCESSIBILITY_ID_MAPPING, XPATH_MAPPING, ID_MAPPING
from features.steps.helpers import contact_was_added, find_contact
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("the Contacts app is open")
def step_given_contacts_app_open(context):
    # the app was open because the driver was initialized in the environment.py file
    pass


@when("I add a new contact with the name {name} and phone number {phone}")
def step_when_add_contact(context, name, phone):
    name = name.replace('"', "")
    phone = phone.replace('"', "")
    context.driver.find_element(
        AppiumBy.ACCESSIBILITY_ID, ACCESSIBILITY_ID_MAPPING["Create contact button"]
    ).click()
    first_name_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, XPATH_MAPPING["First name"]))
    )
    first_name_element.send_keys(name.split()[0])
    context.driver.find_element(AppiumBy.XPATH, XPATH_MAPPING["Last name"]).send_keys(
        name.split()[1]
    )
    context.driver.find_element(AppiumBy.XPATH, XPATH_MAPPING["Phone"]).send_keys(phone)
    context.driver.find_element(AppiumBy.ID, ID_MAPPING["Save button"]).click()
    time.sleep(1)
    back_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, ACCESSIBILITY_ID_MAPPING["Back button"])
        )
    )
    back_button.click()


@then("the contact list should include a contact with the name {name}")
def step_then_verify_contact_added(context, name):
    name = name.replace('"', "")
    assert contact_was_added(context, name)


@given('a contact with the name "{name}" exists')
def step_given_contact_exists(context, name):
    name = name.replace('"', "")
    if not contact_was_added(context, name):
        step_when_add_contact(context, name, "123456789")


@when("I delete the contact with the name {name}")
def step_when_delete_contact(context, name):
    name = name.replace('"', "")
    contact = find_contact(context, name)
    contact.click()
    more_options_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, ACCESSIBILITY_ID_MAPPING["More options"])
        )
    )
    more_options_button.click()
    delete_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(
            (AppiumBy.XPATH, XPATH_MAPPING["Delete contact"])
        )
    )
    delete_button.click()
    confirm_delete_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(
            (AppiumBy.ID, ID_MAPPING["Confirm delete button"])
        )
    )
    confirm_delete_button.click()
    time.sleep(3)


@then("the contact list should not include a contact with the name {name}")
def step_then_verify_contact_deleted(context, name):
    name = name.replace('"', "")
    contact = find_contact(context, name)
    assert not contact, f"Contact with name {name} was not deleted"
