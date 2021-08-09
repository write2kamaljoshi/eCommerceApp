from selenium import webdriver


class LoginPage:

    # Identify and write the locators for every element on page
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[text()='Log in']"
    link_logout_linktext = "Logout"

    # To initialize the driver, we need to create one constructor.
    # Constructor is invoked at the time of object creation
    # It will accept driver as parameter from test case
    def __init__(self, driver):
        self.driver = driver

    # Implement action method for every locator
    def enterEmail(self, email):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)

    def enterPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()

