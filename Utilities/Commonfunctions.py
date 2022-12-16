import os
import pathlib

import pyodbc
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Commonfunctions():

    @staticmethod
    def Waitvisible(driver, elements):
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH,
             elements)))

    def Waitinvisible(driver, elements):
        WebDriverWait(driver, 60).until(EC.invisibility_of_element_located(
            (By.XPATH,
             elements)))

    def Waitalert(driver):
        WebDriverWait(driver,60).until(EC.alert_is_present())




    def Waitvisibleall(driver, elements):
        WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located(
            (By.XPATH,
             elements)))


    @staticmethod
    def Waitclick(driver, elements):
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable(
            (By.XPATH,
             elements)))

    @staticmethod
    def selectbytext(element, text):
        select = Select(element)
        select.select_by_visible_text(text)

    @staticmethod
    def selectbyindex(element, text):
        select = Select(element)
        select.select_by_index(text)

    @staticmethod
    def screenshot(driver,file):
        path1 = pathlib.Path().absolute()
        print("path is", path1)
        path2 = os.path.join(path1, "TestEvidence",file)
        driver.get_screenshot_as_file(path2)
        # driver.get_screenshot_as_file(os.getcwd()+'TestEvidence',file)

    @staticmethod
    def mousehover(driver,element):
        actionchain = ActionChains(driver)
        actionchain.move_to_element(element).perform()





