# Example Project of Using Behave with Android
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)  [![Appium](https://img.shields.io/badge/Appium-2.0.0-blue?logo=appium)](https://appium.io/docs/en/latest/)  [![Behave](https://img.shields.io/badge/Behave-1.2.6-green?logo=python)](https://behave.readthedocs.io/en/latest/)  [![Android Studio](https://img.shields.io/badge/Android%20Studio-2021.1.1-green?logo=android)](https://developer.android.com/?hl=pt-br)



## Install Project Dependencies:

```sh
pip install -r requirements.txt
```

## Create an Emulator in Android Studio

I used Android 15, but you can use any version. Replace the device name and platform version in `behave.ini` with your emulator's name and Android version.


## Install Appium and Start the Server

[Appium installation](https://appium.io/docs/en/2.1/quickstart/install/)
```sh
appium -pa /android
```

## Running Tests

Run the tests with the command:
```sh
behave
```
