import os
import pathlib
import random
import sched
import shutil
import threading
import time
import unittest

import pyautogui
import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from PageObjects.hrPortal_PageObjects import HRPortal_PageObjects
from Pages.Employee import Employee_LeaveManagement
from Pages.HrportalDB import HrportalDB
from Pages.Supervisor import Supervisor_LeaveManagement
from Utilities.Commonfunctions import Commonfunctions
from Utilities.customLogger import Log
from Utilities.readProperties import ReadConfig


class Base():
    baseURL = ReadConfig.getApplicationURL()
    excelname = ReadConfig.getExcelName()
    sheetname = ReadConfig.getExcelSheet()
    sheetname2 = ReadConfig.getExcelSheet2()
    mailid = ReadConfig.getEmailNames()

    # def __init__(self):
    #     self.login = Employee_LeaveManagement(self.driver)
    #     self.supervisor = Supervisor_LeaveManagement(self.driver)
    #     self.db = HrportalDB()

    @classmethod
    def setUpClass(self):
        path = pathlib.Path().absolute()
        rmpath = os.path.join(path, "Reports", "")
        rmpath2 = os.path.join(path, "TestEvidence", "")
        for file_name in os.listdir(rmpath):
            # construct full file path
            file = rmpath + file_name
            if os.path.isfile(file):
                print('Deleting file:', file)
                os.remove(file)

        for file_name in os.listdir(rmpath2):
            # construct full file path
            file = rmpath2 + file_name
            if os.path.isfile(file):
                print('Deleting file:', file)
                os.remove(file)


        try:
            print("browser launch")
            if ReadConfig.getBrowser() == 'chrome':
                options = webdriver.ChromeOptions()
                options.add_argument('--ignore-ssl-errors=yes')
                options.add_argument('--ignore-certificate-errors')
                self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=options)
                print("Launching Chrome browser*************")
            if ReadConfig.getBrowser() == 'firefox':
                self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
                print("Launching FireFox browser*************")
            if ReadConfig.getBrowser() == 'edge':
                self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
                print("Launching Edge browser*************")

        except:

            path = pathlib.Path().absolute()
            chromepath = os.path.join(path, "Driver", "")
            print("chorm", chromepath)
            print(chromepath + 'chromedriver.exe')
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-ssl-errors=yes')
            options.add_argument('--ignore-certificate-errors')
            self.driver = webdriver.Chrome(executable_path=chromepath+'chromedriver.exe',options=options)
            print("Launching Chrome browser*************")

        # self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get(ReadConfig.getApplicationURL())

        # self.empobjects = HRPortal_PageObjects(self.driver)

        # chrome_driver = os.getcwd() + "\chromedriver.exe"
        # chrome_options = Options()
        # chrome_options.add_experimental_option("debuggerAddress", "localhost:8800")
        # self.driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        self.login = Employee_LeaveManagement(self.driver)
        self.supervisor = Supervisor_LeaveManagement(self.driver)
        self.db = HrportalDB()
        s = sched.scheduler(time.time, time.sleep)

        # #
        def takeANap():
            def do_something(sc):
                # for z in range(1, 2):
                #     x = random.randint(0, 500)
                #     y= random.randint(0, 500)
                #     pyautogui.moveTo(x, y)
                pyautogui.press('capslock')
                pyautogui.press('capslock')

                s.enter(60, 0.25, do_something, (sc,))

            s.enter(1, 0.25, do_something, (s,))

            s.run()

        threadObj = threading.Thread(target=takeANap)
        threadObj.daemon = True
        threadObj.start()
