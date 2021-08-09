from selenium import webdriver
import pytest
# package - pageObjects , module - LoginPage, class -  LoginPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_loginPageTitle(self, setup):
        self.logger.info("*************** Test_001_Login started ****************")
        self.logger.info("*************** test_loginPageTitle started ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*************** test_loginPageTitle passed ****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_loginPageTitle.png")
            self.driver.close()
            self.logger.info("*************** test_loginPageTitle failed ****************")
            assert False


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*************** test_login started ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*************** test_login passed ****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            self.driver.close()
            self.logger.info("*************** test_login failed ****************")
            assert False


