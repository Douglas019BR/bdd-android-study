import time
from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy

@given("the Contacts app is open")
def step_given_contacts_app_open(context):
    # Assume que o setup já abriu o aplicativo de contatos
    pass

@given('a contact with the name "{name}" exists')
def step_given_contact_exists(context, name):
    # Verifica se o contato já existe
    contacts = context.driver.find_elements(AppiumBy.XPATH, f"//android.widget.TextView[@text='{name}']")
    if not contacts:
        # Adiciona o contato se ele não existir
        step_when_add_contact(context, name, "123456789")


@when("I add a new contact with the name {name} and phone number {phone}")
def step_when_add_contact(context, name, phone):
    time.sleep(5)
    context.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Create contact").click()
    context.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='First name']").send_keys(name.split()[0])
    context.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Last name']").send_keys(name.split()[1])
    context.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Phone']").send_keys(phone)
    context.driver.find_element(AppiumBy.ID, "com.google.android.contacts:id/editor_menu_save_button").click()
    time.sleep(3)

@then("the contact list should include a contact with the name {name}")
def step_then_verify_contact_added(context, name):
    time.sleep(3)
    contacts = context.driver.find_elements(AppiumBy.XPATH, f"//android.widget.TextView[@text='{name}']")
    assert len(contacts) > 0, f"Contact with name {name} not found"

@when("I delete the contact with the name {name}")
def step_when_delete_contact(context, name):
    time.sleep(2)
    contact = context.driver.find_element(AppiumBy.XPATH, f"//android.widget.TextView[@text='{name}']")
    contact.click()
    context.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "More options").click()
    context.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Delete']").click()
    context.driver.find_element(AppiumBy.ID, "android:id/button1").click()
    time.sleep(3)

@then("the contact list should not include a contact with the name {name}")
def step_then_verify_contact_deleted(context, name):
    time.sleep(3)
    contacts = context.driver.find_elements(AppiumBy.XPATH, f"//android.widget.TextView[@text='{name}']")
    assert len(contacts) == 0, f"Contact with name {name} was not deleted"