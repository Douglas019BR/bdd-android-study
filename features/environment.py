from appium import webdriver
from appium.options.android import UiAutomator2Options
from configparser import ConfigParser


config = ConfigParser()
config.read("behave.ini")
userdata = config["behave.userdata"]


def before_all(context):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = userdata.get("platform_version", "15.0")
    options.device_name = userdata.get("device", "Pixel_7_Pro_API_35")
    options.app_package = "com.google.android.contacts"
    options.app_activity = "com.android.contacts.activities.PeopleActivity"
    options.no_reset = True
    context.options = options


def before_scenario(context, scenario):
    try:
        context.driver = webdriver.Remote(
            "http://localhost:4723/android", options=context.options
        )
    except Exception as e:
        print(f"Erro ao inicializar o driver: {e}")
        raise


def after_all(context):
    if hasattr(context, "driver"):
        try:
            context.driver.terminate_app("com.google.android.contacts")
            context.driver.quit()
        except Exception as e:
            print(f"Error closing the driver: {e}")
    else:
        print("driver not found")
        print(f"context attr : {context.__dict__}")
