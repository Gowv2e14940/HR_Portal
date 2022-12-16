import configparser
import os
import pathlib

config = configparser.RawConfigParser()
path1 = pathlib.Path().absolute()
print("path is",path1)
path2 = os.path.join(path1,"Configurations","config.ini")
print("path2 is",path2)
config.read(path2)
excel = os.path.join(path1,"TestData","")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getBrowser():
        browser = config.get('common info', 'browser')
        return browser

    @staticmethod
    def getExcelName():
        excelname = excel+config['common info']['excelName']
        return excelname

    @staticmethod
    def getExcelSheet():
        excelsheet = config.get('common info', 'sheetname')
        return excelsheet

    @staticmethod
    def getExcelSheet2():
        excelsheet2 = config.get('common info', 'sheetname2')
        return excelsheet2

    @staticmethod
    def getEmailNames():
        emailid = config.get('common info', 'emailid')
        return emailid

