import time

from selenium.webdriver.support.ui import Select


class AddNewCustomer:

    link_customerMenu_xpath = "//i[@class='nav-icon far fa-user']/following-sibling::p[contains(text(),'Customers')]"
    link_customerSubMenu_xpath = "//p[text()=' Customers']"
    btn_addNew_xpath = "//a[@class='btn btn-primary']"

    textbox_email_id = "Email"
    textbox_password_id = "Password"
    textbox_firstName_id = "FirstName"
    textbox_lastName_id = "LastName"
    rdbtn_genderMale_id = "Gender_Male"
    rdbtn_genderFemale_id = "Gender_Female"
    text_dob_id = "DateOfBirth"
    text_company_id = "Company"
    text_customerRoles_xpath = "//ul[@id='SelectedCustomerRoleIds_taglist']//parent::div[@class='k-multiselect-wrap k-floatwrap']"
    listItem_administrators_xpath = "//li[text()='Administrators']"
    listItem_forumModerators_xpath = "//li[text()='Forum Moderators']"
    listItem_guests_xpath = "//li[text()='Guests']"
    listItem_registered_xpath = "//li[text()='Registered']"
    listItem_vendors_xpath = "//li[text()='Vendors']"
    dropdown_managerOfVendor_id = "VendorId"
    textbox_adminComment_name = "AdminComment"
    btn_save_name = "save"


    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.link_customerMenu_xpath).click()

    def clickOnCustomerSubMenu(self):
        self.driver.find_element_by_xpath(self.link_customerSubMenu_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btn_addNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element_by_id(self.textbox_firstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_id(self.textbox_lastName_id).send_keys(lname)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element_by_id(self.rdbtn_genderMale_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.rdbtn_genderFemale_id).click()
        else:
            self.driver.find_element_by_id(self.rdbtn_genderMale_id).click()

    def setDob(self, dob):
        self.driver.find_element_by_id(self.text_dob_id).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element_by_id(self.text_company_id).send_keys(comname)

    # User can be a registered or guest (only one)
    def setCustomerRoles(self, role):
        if role == "Registered":
            pass
        else:
            self.driver.find_element_by_xpath(self.text_customerRoles_xpath).click()
            if role == "Forum Moderators":
                self.listItem = self.driver.find_element_by_xpath(self.listItem_forumModerators_xpath)
            elif role == "Vendors":
                self.listItem = self.driver.find_element_by_xpath(self.listItem_vendors_xpath)
            elif role == "Administrators":
                self.listItem = self.driver.find_element_by_xpath(self.listItem_administrators_xpath)
            elif role == "Guests":
                self.driver.find_element_by_xpath("// span[ @ title = 'delete']").click()
                self.driver.find_element_by_xpath(self.text_customerRoles_xpath).click()
                self.listItem = self.driver.find_element_by_xpath(self.listItem_guests_xpath)
            else:
                self.listItem = self.driver.find_element_by_xpath(self.listItem_guests_xpath)

            # self.listItem.click()
            self.driver.execute_script("arguments[0].click();", self.listItem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_id(self.dropdown_managerOfVendor_id))
        drp.select_by_visible_text(value)

    def setAdminContent(self, content):
        self.driver.find_element_by_name(self.textbox_adminComment_name).send_keys(content)

    def clickSave(self):
        self.driver.find_element_by_name(self.btn_save_name).click()
