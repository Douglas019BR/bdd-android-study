ACCESSIBILITY_ID_MAPPING = {
    "Contacts App": "Contacts",
    "Create contact button": "Create contact",
    "Back button": "Navigate up",
    "Search contacts": "Search",
    "More options": "More options",
}

XPATH_MAPPING = {
    "First name": "//android.widget.EditText[@text='First name']",
    "Last name": "//android.widget.EditText[@text='Last name']",
    "Phone": "//android.widget.EditText[@text='Phone']",
    "Search contacts text": '//android.widget.TextView[@resource-id="com.google.android.contacts:id/open_search_bar_text_view"]',
    "Delete contact": '//android.widget.TextView[@resource-id="com.google.android.contacts:id/title" and @text="Delete"]',
}

ID_MAPPING = {
    "Contacts list": "android:id/list",
    "Save button": "toolbar_button",
    "Confirm delete button": "android:id/button1",
}
