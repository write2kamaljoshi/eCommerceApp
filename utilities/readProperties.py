import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:

    # using below annotation, we can access this method directly using class name without creating any object
    @staticmethod
    def getApplicationURL():
        url = config.get('pre-requisites', 'baseURL')
        return url

    @staticmethod
    def getEmail():
        email = config.get('pre-requisites', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('pre-requisites', 'password')
        return password
