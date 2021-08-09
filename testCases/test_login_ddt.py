import time

from selenium import webdriver
import pytest
# package - pageObjects , module - LoginPage, class -  LoginPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:

    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login__ddt(self, setup):
        self.logger.info("*************** Test_002_DDT_Login started ****************")
        self.logger.info("*************** test_login started ****************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("No. of rows in excel: ", self.rows)
        lst_status = []

        for r in range(2, self.rows+1):
            self.email = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.expected = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.enterEmail(self.email)
            self.lp.enterPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.expected == "Pass":
                    self.logger.info("*************** Passed ****************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.expected == "Fail":
                    self.logger.info("*************** Failed ****************")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.expected == "Pass":
                    self.logger.info("*************** Failed ****************")
                    lst_status.append("Fail")
                elif self.expected == "Fail":
                    self.logger.info("*************** Passed ****************")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("*************** test_login__ddt Passed ****************")
            self.logger.info("*************** Test_002_DDT_Login Passed ****************")
            self.driver.close()
            assert True
        else:
            self.logger.info("*************** test_login__ddt Failed ****************")
            self.logger.info("*************** Test_002_DDT_Login Failed ****************")
            self.driver.close()
            assert False

        self.logger.info("*************** Test_002_DDT_Login Completed ****************")
