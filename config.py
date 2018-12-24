android_desired_caps = {
    'platformName': 'android',
    'deviceName': 'Android Emulator',
    'appPackage': 'com.auth0sample',
    'appActivity': 'com.auth0sample.MainActivity',
    'chromeOptions': {
        'androidPackage': 'com.android.chrome'
    }
}

ios_desired_caps = {
    "platformName": "iOS",
    "platformVersion": "11.0",
    "deviceName": "iPhone 7",
    "automationName": "XCUITest",
    "app": "/path/to/my.app"
}

login_user = "asdasd"
login_password = "asdasd"
