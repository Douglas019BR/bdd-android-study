import time
from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from features.steps.maps import ACCESSIBILITY_ID_MAPPING ,XPATH_MAPPING, ID_MAPPING
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("the Contacts app is open")
def step_given_contacts_app_open(context):
    # wait = WebDriverWait(context.driver, 10)
    # element = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, ACCESSIBILITY_ID_MAPPING["Contacts App"])))
    # element.click()
    pass

# @given('a contact with the name "{name}" exists')
# def step_given_contact_exists(context, name):
#     contacts = context.driver.find_elements(AppiumBy.XPATH, f"//android.widget.TextView[@text='{name}']")
#     if not contacts:
#         step_when_add_contact(context, name, "123456789")


@when("I add a new contact with the name {name} and phone number {phone}")
def step_when_add_contact(context, name, phone):
    name = name.replace('"', '')
    phone = phone.replace('"', '')
    context.driver.find_element(AppiumBy.ACCESSIBILITY_ID, ACCESSIBILITY_ID_MAPPING["Create contact button"]).click()
    first_name_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, XPATH_MAPPING["First name"]))
    )
    first_name_element.send_keys(name.split()[0])
    context.driver.find_element(AppiumBy.XPATH, XPATH_MAPPING["Last name"]).send_keys(name.split()[1])
    context.driver.find_element(AppiumBy.XPATH, XPATH_MAPPING["Phone"]).send_keys(phone)
    context.driver.find_element(AppiumBy.ID, ID_MAPPING["Save button"]).click()
    time.sleep(1)
    back_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, ACCESSIBILITY_ID_MAPPING["Back button"]))
    )
    back_button.click()

@then("the contact list should include a contact with the name {name}")
def step_then_verify_contact_added(context, name):
    contacts = context.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, ACCESSIBILITY_ID_MAPPING["Search contacts"]).click()
    name = name.replace('"', '')
    context.driver.find_element(AppiumBy.ID, ID_MAPPING["Search contacts text"]).send_keys(name)
    contacts = context.driver.find_elements(AppiumBy.ID, ID_MAPPING["Contacts list"])
    print(f"contacts: {contacts}")
    assert len(contacts) > 0, f"Contact with name {name} not found"


# @when("I delete the contact with the name {name}")
# def step_when_delete_contact(context, name):
#     contact = context.driver.find_element(AppiumBy.XPATH, f"//android.widget.TextView[@text='{name}']")
#     contact.click()
#     context.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "More options").click()
#     context.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Delete']").click()
#     context.driver.find_element(AppiumBy.ID, "android:id/button1").click()
#     time.sleep(2)

# @then("the contact list should not include a contact with the name {name}")
# def step_then_verify_contact_deleted(context, name):
#     contacts = context.driver.find_elements(AppiumBy.XPATH, f"//android.widget.TextView[@text='{name}']")
#     assert len(contacts) == 0, f"Contact with name {name} was not deleted"