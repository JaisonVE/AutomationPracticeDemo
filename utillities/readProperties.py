import configparser


config = configparser.RawConfigParser()
config.read("C:\\Users\\user\\PycharmProjects\\AutomationPracticeDemo\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url