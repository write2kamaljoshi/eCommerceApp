from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture()
def setup(browser): # passing the browser name to setup method
    if browser == 'ie':
        driver = webdriver.Ie(IEDriverManager().install())
        print("Launching Internet Explorer Browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("Launching Firefox Browser.........")
    elif browser == 'edge':
        # driver = webdriver.Edge("msedgedriver.exe")
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching Edge Browser.........")
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching Chrome Browser.........")
    return driver

# hook
def pytest_addoption(parser):   # This will get the browser name from CLI
    parser.addoption("--browser")   # getting the browser name

@pytest.fixture()
def browser(request):   # This will return the browser name to setup method
    return request.config.getoption("--browser")


################## Pytest HTML Report ####################

# It is a hook for adding environment info to HTML report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'eCommerceApp'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'Kamal Joshi'
#
#
# # It is a hook for deleting/modifying environment info to HTML report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
#
#
