import time

# from selenium.webdriver import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from PageObjects.hrPortal_PageObjects import HRPortal_PageObjects
from Utilities.Commonfunctions import Commonfunctions
from Utilities.customLogger import Log


class Supervisor_LeaveManagement():

    logger = Log.logCreate()


    def __init__(self,driver):
        self.driver=driver

    def Supervisor_Login(self,uname,pwd):
        self.logger.info("Wait till login page appears")
        Commonfunctions.Waitvisible(self.driver,HRPortal_PageObjects.loginbutton)
        self.logger.info("Entering Supervisor credentials")
        self.driver.find_element(By.XPATH,(HRPortal_PageObjects.username)).clear()
        self.driver.find_element(By.XPATH,(HRPortal_PageObjects.username)).send_keys(uname)
        self.driver.find_element(By.XPATH,(HRPortal_PageObjects.password)).clear()
        self.driver.find_element(By.XPATH,(HRPortal_PageObjects.password)).send_keys(pwd)
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.loginbutton)
        self.driver.find_element(By.XPATH,(HRPortal_PageObjects.loginbutton)).click()



    def Supervisor_LeaveApprove(self,empid,leavetype):
        try:
            self.logger.info("Employee Leave Management Menu clicks ")
            # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sleavemanagement)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sleavemanagement)).click()
            self.logger.info("wait until Approve Leave clicks")
            Commonfunctions.mousehover(self.driver,self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sleavepermissiondetails)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sapproveleave)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sapproveleave)).click()
        except:
            print("")
        try:
            # if leavetype=='casual':
            # Commonfunctions.Waitclick(self.driver, "//*[@id='ContentPlaceHolder1_lblPageHeader'][contains(text(),'Approve/Reject Leave')]")
            Commonfunctions.Waitclick(self.driver,
                                      "//table[@id='ContentPlaceHolder1_gvLeaveApproval']/tbody/tr/td/span[contains(text(),'"+empid+"')]//following::a[contains(text(),'Approve')]")
            self.driver.find_element(By.XPATH,"//table[@id='ContentPlaceHolder1_gvLeaveApproval']/tbody/tr/td/span[contains(text(),'"+empid+"')]//following::a[contains(text(),'Approve')]").click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sapproverequestpage)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sapprovecomments)).send_keys("TestApprove")
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sapprove)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sapprove)).click()
        except:
            Commonfunctions.mousehover(self.driver, self.driver.find_element(By.XPATH, (
                HRPortal_PageObjects.sleavepermissiondetails)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sapproveleave)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sapproveleave)).click()
            Commonfunctions.Waitclick(self.driver,
                                      "//table[@id='ContentPlaceHolder1_gvLeaveApproval']/tbody/tr/td/span[contains(text(),'" + empid + "')]//following::a[contains(text(),'Approve')]")
            self.driver.find_element(By.XPATH,
                                     "//table[@id='ContentPlaceHolder1_gvLeaveApproval']/tbody/tr/td/span[contains(text(),'" + empid + "')]//following::a[contains(text(),'Approve')]").click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sapproverequestpage)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sapprovecomments)).send_keys("TestApprove")
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sapprove)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sapprove)).click()

    def Supervisor_PermissionApprove(self,empid):
        try:
            self.logger.info("Employee Leave Management Menu clicks ")
            # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sleavemanagement)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sleavemanagement)).click()
        except:
            print("")
        self.logger.info("wait until Request Leave clicks")
        Commonfunctions.mousehover(self.driver,self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sleavepermissiondetails)))
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sapprovepermission)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sapprovepermission)).click()
        # if leavetype=='casual':
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sapprovepermissionpage)
        self.driver.find_element(By.XPATH,"//table[@id='ContentPlaceHolder1_gvPermissionApproval']/tbody/tr/td/span[contains(text(),'"+empid+"')]//following::a[contains(text(),'Approve')]").click()
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sapprovepermissioncomments)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sapprovepermissioncomments)).send_keys("TestApprove")
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.spermissionapprove)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.spermissionapprove)).click()


    def Supervisor_WFHApprove(self,empid,leavetype):
        try:
            self.logger.info("Employee Leave Management Menu clicks ")
            # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sleavemanagement)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sleavemanagement)).click()
        except:
            print("")
        self.logger.info("wait until Request Leave clicks")
        Commonfunctions.mousehover(self.driver,self.driver.find_element(By.XPATH, (HRPortal_PageObjects.swfhrequestdetails)))
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sapprovewfh)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sapprovewfh)).click()
        # if leavetype=='casual':
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sapproveleavepage)
        self.driver.find_element(By.XPATH,"//table[@id='ContentPlaceHolder1_gvLeaveApproval']/tbody/tr/td/span[contains(text(),'"+empid+"')]//following::a[contains(text(),'Approve')]").click()
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sapproverequestpage)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sapprovecomments)).send_keys("TestApprove")
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sapprove)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sapprove)).click()

    def Supervisor_Team_LeaveDetails(self,leavetype,location):
        try:
            self.driver.find_element(By.XPATH,
                                     "//*[@id='page-wrapper']/div/div[2]/div/div/div/span[contains(text(),'Leave Details')]").is_displayed()
            Commonfunctions.Waitvisible(self.driver,
                                        "//*[@id='page-wrapper']/div/div[2]/div/div/div/span[contains(text(),'Leave Details')]")


        except:
            self.logger.info("Employee Leave Management Menu clicks ")
            # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sleavemanagement)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sleavemanagement)).click()
            self.logger.info("wait until Request Leave clicks")
            Commonfunctions.mousehover(self.driver, self.driver.find_element(By.XPATH, (
                HRPortal_PageObjects.sleavepermissiondetails)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sviewteamleave)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sviewteamleave)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sleavedetailspage)
            Commonfunctions.selectbytext(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.departmentselect)), "--Select--")
            Commonfunctions.selectbytext(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.locationselect)), location)
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smonthsearch)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smonthsearch)).click()
        try:
            if leavetype == 'CL':
                isdisplayed = self.driver.find_element(By.XPATH, "//table[@id='ContentPlaceHolder1_gvLeaveDetails']//following::span[contains(text(),'"+leavetype+"')]").is_displayed()
                self.driver.find_element(By.XPATH,
                                         "//table[@id='ContentPlaceHolder1_gvLeaveDetails']//following::span[contains(text(),'" + leavetype + "')]").click()
                return isdisplayed
            if leavetype == 'EL':
                isdisplayed = self.driver.find_element(By.XPATH, "//table[@id='ContentPlaceHolder1_gvLeaveDetails']//following::span[contains(text(),'"+leavetype+"')]").is_displayed()
                self.driver.find_element(By.XPATH,
                                         "//table[@id='ContentPlaceHolder1_gvLeaveDetails']//following::span[contains(text(),'" + leavetype + "')]").click()
                return isdisplayed
            if leavetype == 'FL':
                isdisplayed =   self.driver.find_element(By.XPATH, "//table[@id='ContentPlaceHolder1_gvLeaveDetails']//following::span[contains(text(),'"+leavetype+"')]").is_displayed()
                self.driver.find_element(By.XPATH,
                                         "//table[@id='ContentPlaceHolder1_gvLeaveDetails']//following::span[contains(text(),'" + leavetype + "')]").click()
                return isdisplayed
            if leavetype == 'CO':
                isdisplayed =   self.driver.find_element(By.XPATH, "//table[@id='ContentPlaceHolder1_gvLeaveDetails']//following::span[contains(text(),'"+leavetype+"')]").is_displayed()
                self.driver.find_element(By.XPATH,
                                         "//table[@id='ContentPlaceHolder1_gvLeaveDetails']//following::span[contains(text(),'" + leavetype + "')]").click()
                return isdisplayed
        except:
            value = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonth)).get_attribute('value')
            value = int(value) - 1
            print("the value in select", value)
            Commonfunctions.selectbyindex(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonthclick)), value)
            Commonfunctions.selectbytext(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.departmentselect)), "--Select--")
            Commonfunctions.selectbytext(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.locationselect)), location)
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smonthsearch)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smonthsearch)).click()
            if leavetype == 'CL':
                isdisplayed = self.driver.find_element(By.XPATH,
                                                       "//table[@id='ContentPlaceHolder1_gvLeaveDetails']//following::span[contains(text(),'" + leavetype + "')]").is_displayed()
                self.driver.find_element(By.XPATH,
                                         "//table[@id='ContentPlaceHolder1_gvLeaveDetails']//following::span[contains(text(),'" + leavetype + "')]").click()
                return isdisplayed
            if leavetype == 'EL':
                isdisplayed = self.driver.find_element(By.XPATH,
                                                       "//table[@id='ContentPlaceHolder1_gvLeaveDetails']//following::span[contains(text(),'" + leavetype + "')]").is_displayed()
                self.driver.find_element(By.XPATH,
                                         "//table[@id='ContentPlaceHolder1_gvLeaveDetails']//following::span[contains(text(),'" + leavetype + "')]").click()
                return isdisplayed
            if leavetype == 'FL':
                isdisplayed = self.driver.find_element(By.XPATH,
                                                       "//table[@id='ContentPlaceHolder1_gvLeaveDetails']//following::span[contains(text(),'" + leavetype + "')]").is_displayed()
                self.driver.find_element(By.XPATH,
                                         "//table[@id='ContentPlaceHolder1_gvLeaveDetails']//following::span[contains(text(),'" + leavetype + "')]").click()
                return isdisplayed
            if leavetype == 'CO':
                isdisplayed = self.driver.find_element(By.XPATH,
                                                       "//table[@id='ContentPlaceHolder1_gvLeaveDetails']//following::span[contains(text(),'" + leavetype + "')]").is_displayed()
                self.driver.find_element(By.XPATH,
                                         "//table[@id='ContentPlaceHolder1_gvLeaveDetails']//following::span[contains(text(),'" + leavetype + "')]").click()
                return isdisplayed

    def Supervisor_Team_permissionDetails(self,leavetype,location,dept):
        # self.logger.info("Employee Leave Management Menu clicks ")
        # # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sleavemanagement)
        # self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sleavemanagement)).click()
        try:
            self.logger.info("wait until Request Leave clicks")
            Commonfunctions.mousehover(self.driver,self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sleavepermissiondetails)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sviewteampermission)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sviewteampermission)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.spermissionpage)
            Commonfunctions.selectbytext(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.departmentselect)), dept)
            Commonfunctions.selectbytext(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.locationselect)), location)
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smonthsearch)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smonthsearch)).click()
            time.sleep(2)
            if leavetype == 'Permission':
                isdisplayed = self.driver.find_element(By.XPATH, "//table[@id='ContentPlaceHolder1_gvPermissionApproval']//following::span[contains(text(),'Test Permission')]").is_displayed()
                return isdisplayed

        except:
            value = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonth)).get_attribute('value')
            value = int(value) - 1
            print("the value in select", value)
            Commonfunctions.selectbyindex(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonthclick)), value)
            Commonfunctions.selectbytext(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.departmentselect)), dept)
            Commonfunctions.selectbytext(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.locationselect)), location)
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smonthsearch)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smonthsearch)).click()
            time.sleep(2)
        if leavetype == 'Permission':
            Commonfunctions.Waitvisible(self.driver, "//table[@id='ContentPlaceHolder1_gvPermissionApproval']//following::span[contains(text(),'Test Permission')]")
            isdisplayed = self.driver.find_element(By.XPATH,
                                                   "//table[@id='ContentPlaceHolder1_gvPermissionApproval']//following::span[contains(text(),'Test Permission')]").is_displayed()
            return isdisplayed




    def Supervisor_Team_WfhDetails(self,leavetype,location):
        # self.logger.info("Employee Leave Management Menu clicks ")
        # # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sleavemanagement)
        # self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sleavemanagement)).click()
        self.logger.info("wait until Request Leave clicks")
        Commonfunctions.mousehover(self.driver,
                                   self.driver.find_element(By.XPATH, (HRPortal_PageObjects.swfhrequestdetails)))
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sviewteamwfh)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sviewteamwfh)).click()
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sleavedetailspage)
        Commonfunctions.selectbytext(
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.departmentselect)), "--Select--")
        Commonfunctions.selectbytext(
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.locationselect)), location)
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smonthsearch)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smonthsearch)).click()
        try:
            if leavetype == 'WFH':
                isdisplayed =   self.driver.find_element(By.XPATH, "//table[@id='ContentPlaceHolder1_gvLeaveDetails']//following::span[contains(text(),'"+leavetype+"')]").is_displayed()
                return isdisplayed
        except:
            value = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonth)).get_attribute('value')
            value = int(value) - 1
            print("the value in select", value)
            Commonfunctions.selectbyindex(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonthclick)), value)
            Commonfunctions.selectbytext(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.departmentselect)), "--Select--")
            Commonfunctions.selectbytext(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.locationselect)), location)
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smonthsearch)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smonthsearch)).click()
            if leavetype == 'WFH':
                isdisplayed = self.driver.find_element(By.XPATH, "//table[@id='ContentPlaceHolder1_gvLeaveDetails']//following::span[contains(text(),'"+leavetype+"')]").is_displayed()
                return isdisplayed

    def Supervisor_ApproveLOP(self,empcode,mode):
        try:
            # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sattendancemgmt)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemgmt)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.Bioattendancepage)
            Commonfunctions.mousehover(self.driver,self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemanager)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sapprovelop)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sapprovelop)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.slopapprovechangepage)
        except:
            print("")
        # Commonfunctions.selectbyindex(
        #     self.driver.find_element(By.XPATH, (HRPortal_PageObjects.slopdatedropdown)), "1")
        Commonfunctions.Waitvisible(self.driver, "//select[@id = 'ContentPlaceHolder1_ddlLOPDate']/option[contains(text(),'23-')]")
        self.driver.find_element(By.XPATH,"//select[@id = 'ContentPlaceHolder1_ddlLOPDate']/option[contains(text(),'23-')]")
        self.driver.find_element(By.XPATH,(HRPortal_PageObjects.slopemployeecode)).send_keys(empcode)
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sloprecordsearch)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sloprecordsearch)).click()
        Commonfunctions.Waitclick(self.driver, "//table[@id='ContentPlaceHolder1_dgvChangeLOPApproval']//following::td[contains(text(),'"+empcode+"')]//following::td[contains(text(),'Test LOP Request')]//preceding::td/center/span/input")
        self.driver.find_element(By.XPATH,"//table[@id='ContentPlaceHolder1_dgvChangeLOPApproval']//following::td[contains(text(),'"+empcode+"')]//following::td[contains(text(),'Test LOP Request')]//preceding::td/center/span/input").click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.slopapprovebutton)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.slopapprovebutton)).click()
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.slopapprovepopup)
        Commonfunctions.selectbytext(
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemodedropdown)), mode)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.slopapprovecomments)).send_keys("Test LOP Approved")
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.slopapproveupdate)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.slopapproveupdate)).click()
        Commonfunctions.Waitalert(self.driver)
        # self.driver.switch_to_alert().accept()
        Alert(self.driver).accept()

    def Supervisor_MarkULOP(self,empcode,attendancetype):
        try:
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.profileclick)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.profileclick)).click()
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.homeclick)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.homeclick)).click()
            # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sattendancemgmt)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemgmt)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.Bioattendancepage)
            Commonfunctions.mousehover(self.driver,self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemanager)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.smarkulop)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkulop)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.smarkuloppage)
        except:
            print("")
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkulopempname)).send_keys(empcode)
        time.sleep(1)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkulopempname)).send_keys(Keys.ENTER)
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smarkulopfromdateclick)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkulopfromdateclick)).click()
        today = self.driver.find_element(By.XPATH,
                                         "//table[@class='ui-datepicker-calendar']//tr//td[@class=' ui-datepicker-days-cell-over  ui-datepicker-current-day ui-datepicker-today']").text
        if today == '1':
            self.driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click()
            Commonfunctions.Waitvisible(self.driver, "//table[@class='ui-datepicker-calendar']//tr//following::td[@class=' ui-datepicker-week-end ']//following::a[@class='ui-state-default'][last()]")
            self.driver.find_element(By.XPATH, "//table[@class='ui-datepicker-calendar']//tr//following::td[@class=' ui-datepicker-week-end ']//following::a[@class='ui-state-default'][last()]").click()
        else:
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.smarkulopfromdate)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkulopfromdate)).click()
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smarkuloptodateclick)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkuloptodateclick)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.smarkuloptodate)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkuloptodate)).click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smarkulopsearch)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkulopsearch)).click()
        Commonfunctions.Waitclick(self.driver, "//table[@id='ContentPlaceHolder1_dgvChangeLOPRequest']//following::td[contains(text(),'"+empcode+"')]//preceding::td/span/input")
        self.driver.find_element(By.XPATH,"//table[@id='ContentPlaceHolder1_dgvChangeLOPRequest']//following::td[contains(text(),'"+empcode+"')]//preceding::td/span/input").click()
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkulopcomments)).send_keys("Test ULOP Approve")
        Commonfunctions.selectbytext(
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkulopattendancetype)), attendancetype)
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smarkulopsubmit)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkulopsubmit)).click()

    def Supervisor_MarkShiftoff(self,empcode,attendancetype):
        try:
            # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.profileclick)
            # self.driver.find_element(By.XPATH, (HRPortal_PageObjects.profileclick)).click()
            # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.homeclick)
            # self.driver.find_element(By.XPATH, (HRPortal_PageObjects.homeclick)).click()
            # # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sattendancemgmt)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemgmt)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.Bioattendancepage)
            Commonfunctions.mousehover(self.driver,self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemanager)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.smarkshiftoff)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkshiftoff)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.smarkushiftoffpage)
        except:
            print("")
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkshiftoffcode)).send_keys(empcode)
        time.sleep(1)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkshiftoffcode)).send_keys(Keys.ENTER)
        # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smarkulopfromdateclick)
        # self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkulopfromdateclick)).click()
        # Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.smarkulopfromdate)
        # self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkulopfromdate)).click()
        # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smarkuloptodateclick)
        # self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkuloptodateclick)).click()
        # Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.smarkuloptodate)
        # self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkuloptodate)).click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smarkshiftoffsearch)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkshiftoffsearch)).click()
        Commonfunctions.Waitclick(self.driver, "//table[@id='ContentPlaceHolder1_dgvChangeLOPRequest']//following::td[contains(text(),'"+empcode+"')]//preceding::td/span/input")
        self.driver.find_element(By.XPATH,"//table[@id='ContentPlaceHolder1_dgvChangeLOPRequest']//following::td[contains(text(),'"+empcode+"')]//preceding::td/span/input").click()
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkulopcomments)).send_keys("Test Shiftoff Approve")
        Commonfunctions.selectbytext(
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkulopattendancetype)), attendancetype)
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smarkulopsubmit)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkulopsubmit)).click()
        Commonfunctions.Waitalert(self.driver)
        # self.driver.switch_to_alert().accept()
        Alert(self.driver).accept()

    def Supervisor_ExtensionWorkPlan(self,empcode,attendancetype):
        try:
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemgmt)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.Bioattendancepage)
            Commonfunctions.mousehover(self.driver,self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemanager)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sextensionworkplan)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sextensionworkplan)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sextensionworkplanpage)
        except:
            print("")
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sextensionempcode)).send_keys(empcode)
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smarkshiftoffsearch)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkshiftoffsearch)).click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smarkshiftoffsearch)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkshiftoffsearch)).click()
        Commonfunctions.Waitclick(self.driver, "//table[@id='ContentPlaceHolder1_dgvAttendanceExtensionWorkPlan']/tbody//following::input[@value='"+empcode+"']//following::input[1]")
        self.driver.find_element(By.XPATH,"//table[@id='ContentPlaceHolder1_dgvAttendanceExtensionWorkPlan']/tbody//following::input[@value='"+empcode+"']//following::input[1]").click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smarkulopfromdateclick)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkulopfromdateclick)).click()
        Commonfunctions.Waitvisible(self.driver, "//*[@id='ui-datepicker-div']/table/tbody/tr//following::td[@class=' ui-datepicker-days-cell-over  ui-datepicker-today']")
        self.driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr//following::td[@class=' ui-datepicker-days-cell-over  ui-datepicker-today']").click()
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sextensionfromtime)
        self.driver.execute_script("document.getElementById('ContentPlaceHolder1_txtFromTime').value='07:00 PM'")
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sextensiontotime)
        self.driver.execute_script("document.getElementById('ContentPlaceHolder1_txtToTime').value='09:00 PM'")
        Commonfunctions.selectbytext(
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sextensiontype)), attendancetype)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sextensioncomments)).send_keys("Test Extension work plan")
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smarkulopsubmit)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkulopsubmit)).click()
        try:
            isdisplayed = self.driver.find_element(By.XPATH,"//*[@id='ContentPlaceHolder1_lblCommonError'][contains(text(),'Selected Work plan date is declared as a National Holiday, you are not allowed to raise work plan on National Holiday.')]")

        except:
            Commonfunctions.Waitalert(self.driver)
            # self.driver.switch_to_alert().accept()
            Alert(self.driver).accept()

    def Supervisor_ExtensionEntry(self,empcode,attendancetype):
        try:
            # self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemgmt)).click()
            # Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.Bioattendancepage)
            Commonfunctions.mousehover(self.driver,self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemanager)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sextensionentry)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sextensionentry)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sextensionentrypage)
        except:
            print("")
        self.driver.execute_script("document.getElementById('ContentPlaceHolder1_txtFromDate').value='01-01-2022'")
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sextensionempcode)).send_keys(empcode)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sextensionempcode)).send_keys(Keys.ENTER)
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smarkshiftoffsearch)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkshiftoffsearch)).click()
        Commonfunctions.Waitvisible(self.driver, "//table[@id='ContentPlaceHolder1_dgvAttendanceExtension']/tbody//following::td[contains(text(),'"+empcode+"')]//following::input[1]")
        self.driver.find_element(By.XPATH,"//table[@id='ContentPlaceHolder1_dgvAttendanceExtension']/tbody//following::td[contains(text(),'"+empcode+"')]//following::input[1]").click()
        Commonfunctions.selectbytext(
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sextensiontype)), attendancetype)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sextensioncomments)).send_keys("Test CH Extension Entry")
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smarkulopsubmit)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkulopsubmit)).click()
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sextensionentrysubmit)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sextensionentrysubmit)).click()
        Commonfunctions.Waitinvisible(self.driver,"//*[@id='ContentPlaceHolder1_lblmpeError'][contains(text(),'Please wait, The Process is going on...')]")
        # Commonfunctions.Waitalert(self.driver)
        # # self.driver.switch_to_alert().accept()
        # Alert(self.driver).accept()

    def Supervisor_UlopDashboard(self,empcode,attendancetype):
        try:

            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemgmt)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.Bioattendancepage)
            Commonfunctions.mousehover(self.driver,self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemanager)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sulopdashboard)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sulopdashboard)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sulopdashboardpage)
        except:
            print("")
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.smarkshiftoffsearch)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.smarkshiftoffsearch)).click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sulopdashboardabsconding)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sulopdashboardabsconding)).click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sulopdashboardtermination)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sulopdashboardtermination)).click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sulopdashboarduloplist)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sulopdashboarduloplist)).click()
        Commonfunctions.Waitvisible(self.driver, "//*[@id='ContentPlaceHolder1_gvEmployeeULOPList']/tbody/tr/td[contains(text(),'"+empcode+"')]//following::td[contains(text(),'"+attendancetype+"')]")
        ulopdisplayed = self.driver.find_element(By.XPATH,"//*[@id='ContentPlaceHolder1_gvEmployeeULOPList']/tbody/tr/td[contains(text(),'"+empcode+"')]//following::td[contains(text(),'"+attendancetype+"')]").is_displayed()
        return  ulopdisplayed


    def Supervisor_ViewTeamattendancereport(self):
        try:
            # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.attendancemanagement)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemanagement)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.Bioattendancepage)
            Commonfunctions.mousehover(self.driver,
                                       self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemanager)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sviewteamattendance)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sviewteamattendance)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sviewteamattendancepage)
        except:
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.profileclick)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.profileclick)).click()
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.homeclick)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.homeclick)).click()
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemanagement)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.Bioattendancepage)
            Commonfunctions.mousehover(self.driver,
                                       self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemanager)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sviewteamattendance)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sviewteamattendance)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sviewteamattendancepage)



    def Supervisor_viewteamattendance(self,leavetype,empcode):
        try:
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancestaffcode)).clear()
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancestaffcode)).send_keys(empcode)
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sattendancesearch)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancesearch)).click()
            # self.driver.find_element(By.XPATH, "//*[@id='tblAttendance']//following::td[contains(text(),'"+leavetype+"') and not (contains(text(),'LOP'))]").is_displayed()
            if leavetype == 'P':
                try:
                    self.driver.find_element(By.XPATH,"//table[@id='tblAttendance']//following::td[contains(text(),'"+empcode+"')]//following::td[contains(text(),'" + leavetype + "') and not (contains(text(),'LOP'))]")
                    Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sattendanceexcelclick)
                    self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendanceexcelclick)).click()
                    return True
                except:
                    self.driver.find_element(By.XPATH, "//*[@id='tblAttendance']//following::td[contains(text(),'" + leavetype + "') and not (contains(text(),'LOP'))]").is_displayed()
                    Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sattendanceexcelclick)
                    self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendanceexcelclick)).click()
                    return True
        except:
            value = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonth)).get_attribute('value')
            value = int(value) - 1
            print("the value in select", value)
            Commonfunctions.selectbyindex(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonthclick)), value)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancestaffcode)).clear()
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancestaffcode)).send_keys(empcode)
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sattendancesearch)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancesearch)).click()
            if leavetype == 'P':
                self.driver.find_element(By.XPATH,
                                         "//*[@id='tblAttendance']//following::td[contains(text(),'" + leavetype + "') and not (contains(text(),'LOP'))]").is_displayed()
                Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sattendanceexcelclick)
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendanceexcelclick)).click()
                return True

    def Supervisor_ApproveShiftOff(self,empcode):
        try:
            # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sattendancemgmt)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemgmt)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.Bioattendancepage)
            Commonfunctions.mousehover(self.driver,self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemanager)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sapproveshiftoff)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sapproveshiftoff)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sshiftoffapprovecpage)
        except:
            print("")
        # Commonfunctions.selectbyindex(
        #     self.driver.find_element(By.XPATH, (HRPortal_PageObjects.slopdatedropdown)), "1")
        # Commonfunctions.Waitvisible(self.driver, "//select[@id = 'ContentPlaceHolder1_ddlLOPDate']/option[contains(text(),'23-')]")
        # self.driver.find_element(By.XPATH,"//select[@id = 'ContentPlaceHolder1_ddlLOPDate']/option[contains(text(),'23-')]")
        # self.driver.find_element(By.XPATH,(HRPortal_PageObjects.slopemployeecode)).send_keys(empcode)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sapproveshiftdate)).click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sloprecordsearch)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sloprecordsearch)).click()
        Commonfunctions.Waitvisible(self.driver, "//table[@id='ContentPlaceHolder1_dgvChangeLOPApproval']//following::td[contains(text(),'"+empcode+"')]//following::td[contains(text(),'Test Shiftoff Approve')]//preceding::td/center/span/input")
        self.driver.find_element(By.XPATH,"//table[@id='ContentPlaceHolder1_dgvChangeLOPApproval']//following::td[contains(text(),'"+empcode+"')]//following::td[contains(text(),'Test Shiftoff Approve')]//preceding::td/center/span/input").click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.slopapprovebutton)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.slopapprovebutton)).click()
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sshiftoffapprovepopup)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.slopapprovecomments)).send_keys("Test Shiftoff Approved")
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.slopapproveupdate)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.slopapproveupdate)).click()
        # Commonfunctions.Waitalert(self.driver)
        # # self.driver.switch_to_alert().accept()
        # Alert(self.driver).accept()

    def Supervisor_Extensionworkplanapprove(self,empcode):
        try:
            Commonfunctions.mousehover(self.driver,self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sreviewandanalyze)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sextensiondetails)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sextensiondetails)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sextensiondetailspage)
        except:
            print("")
        # Commonfunctions.selectbyindex(
        #     self.driver.find_element(By.XPATH, (HRPortal_PageObjects.slopdatedropdown)), "1")
        # Commonfunctions.Waitvisible(self.driver, "//select[@id = 'ContentPlaceHolder1_ddlLOPDate']/option[contains(text(),'23-')]")
        # self.driver.find_element(By.XPATH,"//select[@id = 'ContentPlaceHolder1_ddlLOPDate']/option[contains(text(),'23-')]")
        self.driver.find_element(By.XPATH,(HRPortal_PageObjects.sextensiondetailsempcode)).send_keys(empcode)
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sextensiondetailsfromdate)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sextensiondetailsfromdate)).click()
        Commonfunctions.Waitvisible(self.driver,
                                    "//*[@id='ui-datepicker-div']/table/tbody/tr//following::td[@class=' ui-datepicker-days-cell-over  ui-datepicker-today']")
        self.driver.find_element(By.XPATH,
                                 "//*[@id='ui-datepicker-div']/table/tbody/tr//following::td[@class=' ui-datepicker-days-cell-over  ui-datepicker-today']").click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sextensiondetailstodate)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sextensiondetailstodate)).click()
        Commonfunctions.Waitvisible(self.driver,
                                    "//*[@id='ui-datepicker-div']/table/tbody/tr//following::td[@class=' ui-datepicker-days-cell-over  ui-datepicker-today']")
        self.driver.find_element(By.XPATH,
                                 "//*[@id='ui-datepicker-div']/table/tbody/tr//following::td[@class=' ui-datepicker-days-cell-over  ui-datepicker-today']").click()

        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sloprecordsearch)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sloprecordsearch)).click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sextensiondetailsworkplantab)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sextensiondetailsworkplantab)).click()
        Commonfunctions.Waitvisible(self.driver, "//table[@id='ContentPlaceHolder1_gvExtensionWorkplan']//following::td[contains(text(),'"+empcode+"')]//following::td[contains(text(),'Test Extension work plan')]//following::span[contains(text(),'Closed')]")
        isdisplayed = self.driver.find_element(By.XPATH,"//table[@id='ContentPlaceHolder1_gvExtensionWorkplan']//following::td[contains(text(),'"+empcode+"')]//following::td[contains(text(),'Test Extension work plan')]//following::span[contains(text(),'Closed')]").is_displayed()
        return isdisplayed

    def Supervisor_ReviewandAnalyze(self, empcode):
        try:
            Commonfunctions.mousehover(self.driver,
                                       self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sreviewandanalyze)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sextensiondetails)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sextensiondetails)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sextensiondetailspage)
        except:
            print("")
        # Commonfunctions.selectbyindex(
        #     self.driver.find_element(By.XPATH, (HRPortal_PageObjects.slopdatedropdown)), "1")
        # Commonfunctions.Waitvisible(self.driver, "//select[@id = 'ContentPlaceHolder1_ddlLOPDate']/option[contains(text(),'23-')]")
        # self.driver.find_element(By.XPATH,"//select[@id = 'ContentPlaceHolder1_ddlLOPDate']/option[contains(text(),'23-')]")
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sextensiondetailsempcode)).send_keys(empcode)
        self.driver.execute_script("document.getElementById('ContentPlaceHolder1_txtFromDate').value='01-01-2022'")
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sextensiondetailstodate)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sextensiondetailstodate)).click()
        Commonfunctions.Waitvisible(self.driver,
                                    "//*[@id='ui-datepicker-div']/table/tbody/tr//following::td[@class=' ui-datepicker-days-cell-over  ui-datepicker-today']")
        self.driver.find_element(By.XPATH,
                                 "//*[@id='ui-datepicker-div']/table/tbody/tr//following::td[@class=' ui-datepicker-days-cell-over  ui-datepicker-today']").click()

        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sloprecordsearch)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sloprecordsearch)).click()
        Commonfunctions.Waitvisible(self.driver,
                                    "//table[@id='ContentPlaceHolder1_dgvCO']//following::td[contains(text(),'"+empcode+"')]//following::td[contains(text(),'Test CH Extension Entry')]")
        isdisplayed = self.driver.find_element(By.XPATH,
                                               "//table[@id='ContentPlaceHolder1_dgvCO']//following::td[contains(text(),'"+empcode+"')]//following::td[contains(text(),'Test CH Extension Entry')]").is_displayed()
        return isdisplayed


    def Supervisor_AttendanceFreezingDate(self):
        try:
            # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sattendancemgmt)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemgmt)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.Bioattendancepage)
            Commonfunctions.mousehover(self.driver,self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemanager)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sattendancefreezingdateconfig)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancefreezingdateconfig)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sattendancefreezingdatepage)
        except:
            print("")
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.spayrolldateconfig)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.spayrolldateconfig)).click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.spayrollstartday)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.spayrollstartday)).click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.spayrollendday)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.spayrollendday)).click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.spayrollyear)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.spayrollyear)).click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.spayrollsubmit)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.spayrollsubmit)).click()
        try:
            Commonfunctions.Waitalert(self.driver)
            Alert(self.driver).accept()
        except:
            print("Already Exists for the month and year given")
        Commonfunctions.mousehover(self.driver,
                                   self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemanager)))
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sattendancefreezingdateconfig)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancefreezingdateconfig)).click()
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sattendancefreezingdatepage)
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sattendancefreezingyear)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancefreezingyear)).click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sattendancefreezingmonth)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancefreezingmonth)).click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sattendancefreezingdateclick)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancefreezingdateclick)).click()
        Commonfunctions.Waitvisible(self.driver, "//table[@class='ui-datepicker-calendar']//following::td[@class=' ui-datepicker-days-cell-over  ui-datepicker-today']/a")
        today = self.driver.find_element(By.XPATH,
                                         "//table[@class='ui-datepicker-calendar']//following::td[@class=' ui-datepicker-days-cell-over  ui-datepicker-today']/a").text

        if int(today) <= 22:
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancefreezingdate)).click()
        elif int(today) >= 23 and int(today) <= 31:
            # Commonfunctions.Waitclick(self.driver, "//*[@id='ui-datepicker-div']/div/a[2]/span")
            self.driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click()
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sattendancefreezingdate)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancefreezingdate)).click()

        # else:
        #     Commonfunctions.Waitclick(self.driver, "//table[@class='ui-datepicker-calendar']//following::td[@class=' ui-datepicker-days-cell-over  ui-datepicker-today']/a")
        #     self.driver.find_element(By.XPATH, "//table[@class='ui-datepicker-calendar']//following::td[@class=' ui-datepicker-days-cell-over  ui-datepicker-today']/a").click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sattendancefreezingsubmit)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancefreezingsubmit)).click()
        Commonfunctions.Waitalert(self.driver)
        Alert(self.driver).accept()


    def Supervisor_NHEntry(self):
        try:
            # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sattendancemgmt)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemgmt)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.Bioattendancepage)
            Commonfunctions.mousehover(self.driver,self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemanager)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.snhentry)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.snhentry)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.snhentrypage)
        except:
            print("")

        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.snhentrydate)).click()
        try:
            isdisplayed =self.driver.find_element(By.XPATH, (HRPortal_PageObjects.snhentrydateselect)).is_displayed()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.snhentrydateselect)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.snhentrydateselect)).click()
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.snhentryreason)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.snhentryreason)).send_keys("Test NH Entry")
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.snhentrysubmit)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.snhentrysubmit)).click()
            Commonfunctions.Waitalert(self.driver)
            Alert(self.driver).accept()
        except:
            Commonfunctions.Waitvisible(self.driver, "//table[@class='ui-datepicker-calendar']//following::td[@class=' ui-datepicker-days-cell-over  ui-datepicker-today']/a")
            self.driver.find_element(By.XPATH, "//table[@class='ui-datepicker-calendar']//following::td[@class=' ui-datepicker-days-cell-over  ui-datepicker-today']/a").click()
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.snhentryreason)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.snhentryreason)).send_keys("Test NH Entry")
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.snhentrysubmit)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.snhentrysubmit)).click()
            Commonfunctions.Waitalert(self.driver)
            Alert(self.driver).accept()


    def Supervisor_MapEmployeeShiftTime(self,empcode):
        try:
            # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sattendancemgmt)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemgmt)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.Bioattendancepage)
            Commonfunctions.mousehover(self.driver,self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sshifttime)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sshifttimemap)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sshifttimemap)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sshifttimemappage)
        except:
            print("")
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.profileclick)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.profileclick)).click()
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.homeclick)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.homeclick)).click()
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemanagement)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.Bioattendancepage)
            Commonfunctions.mousehover(self.driver, self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sshifttime)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sshifttimemap)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sshifttimemap)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sshifttimemappage)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sshifttimeempcode)).send_keys(empcode)
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sshifttimeempcodesearch)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sshifttimeempcodesearch)).click()
        Commonfunctions.Waitvisible(self.driver,
                                    "//table[@id='ContentPlaceHolder1_dgvAddShiftTiming']//following::span[contains(text(),'"+empcode+"')]//preceding::td/span/input")
        self.driver.find_element(By.XPATH,
                                 "//table[@id='ContentPlaceHolder1_dgvAddShiftTiming']//following::span[contains(text(),'"+empcode+"')]//preceding::td/span/input").click()
        Commonfunctions.Waitclick(self.driver,
                                    "//table[@id='ContentPlaceHolder1_dgvAddShiftTiming']//following::span[contains(text(),'"+empcode+"')]//following::td[9]/a")
        self.driver.find_element(By.XPATH,
                                 "//table[@id='ContentPlaceHolder1_dgvAddShiftTiming']//following::span[contains(text(),'"+empcode+"')]//following::td[9]/a").click()
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sshifttimeaddshiftimepage)
        # self.driver.execute_script("document.getElementById('ContentPlaceHolder1_txtInTime').value='10:00 AM'")
        # time.sleep(1)
        # self.driver.execute_script("document.getElementById('ContentPlaceHolder1_txtOutTime').value='07:00 PM'")
        # time.sleep(1)
        # self.driver.execute_script("document.getElementById('ContentPlaceHolder1_txtWorkingHours').value='07:45'")
        Commonfunctions.Waitclick(self.driver,HRPortal_PageObjects.sshifttimeupdate)
        self.driver.find_element(By.XPATH,
                                 HRPortal_PageObjects.sshifttimeupdate).click()
        # Commonfunctions.Waitalert(self.driver)
        # Alert(self.driver).accept()