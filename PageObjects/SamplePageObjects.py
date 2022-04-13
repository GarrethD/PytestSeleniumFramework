def login_text_header():
    return "//h5[@class='modal-title title'][text()='Login']"


def login_password_textfield():
    return "//input[@name='password']"


def login_username_textfield():
    return "//label[text()='Email']/..//input[@name='email']"


def login_button():
    return "//button[@type='submit']/..//span[text()='Login']"


def login_incorrect_user_details_error_message():
    return "//div[@class='alert alert-danger failed']"

