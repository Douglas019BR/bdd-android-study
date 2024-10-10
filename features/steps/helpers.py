from appium.webdriver.common.appiumby import AppiumBy
from features.steps.maps import ID_MAPPING

def contact_was_added(context, name):
    contacts_list = context.driver.find_element(AppiumBy.ID, ID_MAPPING["Contacts list"])
    for contact in contacts_list.find_elements(AppiumBy.XPATH, "//android.widget.TextView"):
        if contact.text == name:
            return True
    return False