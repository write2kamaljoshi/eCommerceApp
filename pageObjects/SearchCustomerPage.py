class SearchCustomerPage:

    textbox_email_id = "SearchEmail"
    textbox_firstName_id = "SearchFirstName"
    textbox_lastName_id = "SearchLastName"
    button_search_id = "search-customers"

    # table_searchResults_xpath = "//table[@role = 'grid']"
    table_xpath = "//table[@id = 'customers-grid']"
    tableRows_xpath = "//table[@id = 'customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id = 'customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).click()

    def setFirstName(self, fname):
        self.driver.find_element_by_id(self.textbox_firstName_id).clear()
        self.driver.find_element_by_id(self.textbox_firstName_id).click()

    def setLastName(self, lname):
        self.driver.find_element_by_id(self.textbox_lastName_id).clear()
        self.driver.find_element_by_id(self.textbox_lastName_id).click()

    def clickSearch(self):
        self.driver.find_element_by_id(self.button_search_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("//table[@id = 'customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//table[@id = 'customers-grid']//tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag
