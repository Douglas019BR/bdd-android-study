from appium import webdriver
from appium.options.android import UiAutomator2Options

def before_all(context):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "15.0"
    options.device_name = "Pixel_Fold_API_35"
    context.options = options

def before_scenario(context, scenario):
    context.options.app_package = "com.google.android.contacts"
    context.options.app_activity = "com.android.contacts.activities.PeopleActivity"
    context.options.no_reset = True

    try:
        context.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=context.options)
    except Exception as e:
        print(f"Erro ao inicializar o driver: {e}")
        raise

def after_scenario(context, scenario):
    driver = getattr(context, 'driver', None)
    if driver:
        driver.quit()

def after_all(context):
    driver = getattr(context, 'driver', None)
    if driver:
        driver.quit()