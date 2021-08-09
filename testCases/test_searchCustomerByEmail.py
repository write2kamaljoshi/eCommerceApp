import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddNewCustomer import AddNewCustomer
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest


class Test_004_SearchCustomerByEmail:

    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("******************* Test_004_SearchCustomerByEmail ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info("******************* Trying to login ********************")
        self.lp = LoginPage(self.driver)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******************* Login successful ********************")

        self.logger.info("******************* Starting test_searchCustomerByEmail ********************")
        self.add_cust = AddNewCustomer(self.driver)

        self.add_cust.clickOnCustomerMenu()
        time.sleep(3)
        self.add_cust.clickOnCustomerSubMenu()

        self.logger.info("******************* Searching customer by email ********************")
        search_cust = SearchCustomerPage(self.driver)
        search_cust.setEmail("victoria_victoria@nopCommerce.com")
        search_cust.clickSearch()
        time.sleep(5)
        status = search_cust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.driver.close()
        self.logger.info("******************* End of Test_004_SearchCustomerByEmail ********************")

