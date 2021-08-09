import random
import string
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddNewCustomer import AddNewCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest


class Test_003_AddCustomer:

    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("******************* Test_003_AddCustomer ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info("******************* Trying to login ********************")
        self.lp = LoginPage(self.driver)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******************* Login successful ********************")

        self.logger.info("******************* Starting test_addCustomer ********************")
        self.add_cust = AddNewCustomer(self.driver)

        self.add_cust.clickOnCustomerMenu()
        time.sleep(3)
        self.add_cust.clickOnCustomerSubMenu()
        self.add_cust.clickOnAddNew()

        self.logger.info("******************* Providing customer info ********************")
        self.email = random_generator() + "@gmail.com"
        self.add_cust.setEmail(self.email)
        self.add_cust.setPassword("password123")
        self.add_cust.setFirstName("Kamal")
        self.add_cust.setLastName("Joshi")
        self.add_cust.setGender("Male")
        self.add_cust.setDob("4/2/1990")
        self.add_cust.setCompanyName("Quovantis")
        self.add_cust.setCustomerRoles("Guests")
        self.add_cust.setManagerOfVendor("Vendor 1")
        self.add_cust.setAdminContent("Testing")
        self.add_cust.clickSave()
        self.logger.info("****************** Saving customer info  ******************")

        self.logger.info("****************** Add customer validation started ******************")
        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if "The new customer has been added successfully." in self.msg:
            assert True
            self.logger.info("******************* test_addCustomer passed ********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_addCustomer.png")
            self.logger.info("******************* test_addCustomer failed ********************")
            assert False

        self.driver.close()
        self.logger.info("******************* End of Test_003_AddCustomer ********************")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
