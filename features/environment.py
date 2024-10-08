from appium import webdriver
from appium.options.android import UiAutomator2Options

def before_all(context):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "15.0"
    options.device_name = "Android Emulator"
    options.app_package = "com.google.android.contacts"
    options.app_activity = ".activities.PeopleActivity"
    options.no_reset = True

    try:
        context.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
    except Exception as e:
        print(f"Erro ao inicializar o driver: {e}")
        raise
