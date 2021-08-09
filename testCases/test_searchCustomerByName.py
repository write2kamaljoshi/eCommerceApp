import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddNewCustomer import AddNewCustomer
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest


class Test_005_SearchCustomerByName:

    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("******************* Test_005_SearchCustomerByName ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info("******************* Trying to login ********************")
        self.lp = LoginPage(self.driver)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******************* Login successful ********************")

        self.logger.info("******************* Starting test_searchCustomerByName ********************")
        self.add_cust = AddNewCustomer(self.driver)

        self.add_cust.clickOnCustomerMenu()
        time.sleep(3)
        self.add_cust.clickOnCustomerSubMenu()

        self.logger.info("******************* Searching customer by name ********************")
        search_cust = SearchCustomerPage(self.driver)
        search_cust.setFirstName("Victoria")
        search_cust.setLastName("Terces")
        search_cust.clickSearch()
        time.sleep(5)
        status = search_cust.searchByName("Victoria Terces")
        assert True == status
        self.driver.close()
        self.logger.info("******************* End of Test_005_SearchCustomerByName ********************")
