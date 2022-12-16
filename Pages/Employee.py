import time
from datetime import date

from selenium.webdriver.common.by import By

from PageObjects.hrPortal_PageObjects import HRPortal_PageObjects
from Utilities.Commonfunctions import Commonfunctions
from Utilities.customLogger import Log


class Employee_LeaveManagement():

    logger = Log.logCreate()


    def __init__(self,driver):
        self.driver=driver

    def Employee_Login(self,uname,pwd):
        self.logger.info("Wait till login page appears")
        Commonfunctions.Waitvisible(self.driver,HRPortal_PageObjects.loginbutton)
        self.logger.info("Entering Employee credentials")
        self.driver.find_element(By.XPATH,(HRPortal_PageObjects.username)).clear()
        # self.driver.find_element_by_xpath(HRPortal_PageObjects.username).clear()
        self.driver.find_element(By.XPATH,(HRPortal_PageObjects.username)).send_keys(uname)
        self.driver.find_element(By.XPATH,(HRPortal_PageObjects.password)).clear()
        self.driver.find_element(By.XPATH,(HRPortal_PageObjects.password)).send_keys(pwd)
        self.driver.find_element(By.XPATH,(HRPortal_PageObjects.loginbutton)).click()

    def Employee_Logout(self):
        self.logger.info("Wait till profile click")
        Commonfunctions.Waitclick(self.driver,HRPortal_PageObjects.profileclick)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.profileclick)).click()
        self.logger.info("Wait till logout click")
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.logout)
        self.driver.find_element(By.XPATH,(HRPortal_PageObjects.logout)).click()


    def Employee_LoginSuccess(self):
        self.logger.info("wait till login the application")
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.loginsuccesspage)
        isdisplayed = self.driver.find_element(By.XPATH,(HRPortal_PageObjects.loginsuccesspage)).is_displayed()
        return isdisplayed


    def Employee_LeaveRequest(self,leavetype,shifttype):
        self.logger.info("Employee Leave Management Menu clicks ")
        try:
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.leavemanagement)).click()
        except:
            print("")
        self.logger.info("wait until Request Leave clicks")
        if(leavetype == "wfh"):
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.requestwfh)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.requestwfh)).click()
            self.logger.info("wait until Request WFH form appears")
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.newleaverequestheading)
            self.logger.info("Request WFH From date clicks")
        else:
            Commonfunctions.Waitclick(self.driver,HRPortal_PageObjects.requestleave)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.requestleave)).click()
            self.logger.info("wait until Request Leave form appears")
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.newleaverequestheading)
            self.logger.info("Request Leave From date clicks")
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.leavefromdate)).click()
        self.logger.info("wait untill From date calendar appears")
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.fromdatedays)
        noofdays=self.driver.find_elements(By.XPATH, (HRPortal_PageObjects.fromdatedays))
        for i in range(1,len(noofdays)):

            for j in range(i):
                print("j value is",j)
                print("length",len(noofdays))
                print("i value is",i)
                self.logger.info("select leave type casual")
                if(leavetype=='casual'):
                    self.driver.find_element(By.XPATH,"//table[@class='ui-datepicker-calendar']//tr[2]//td[not(@class=' ui-datepicker-week-end ') and @data-handler='selectDay']["+str(j+1)+"]/a[1]").click()
                    casualcheck=self.driver.find_element(By.XPATH, (HRPortal_PageObjects.casualcheckbox))
                    if(casualcheck).is_selected():
                        print("is selected")
                        break
                    else:
                        self.driver.find_element(By.XPATH,(HRPortal_PageObjects.casualcheckbox)).click()
                        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.cl)
                        self.driver.find_element(By.XPATH,(HRPortal_PageObjects.cl)).send_keys(1)
                    break
                elif (leavetype == 'flexi'):
                    self.driver.find_element(By.XPATH,
                                             "//table[@class='ui-datepicker-calendar']//tr[2]//td[not(@class=' ui-datepicker-week-end ') and @data-handler='selectDay']["+str(j+2)+"]/a[1]").click()
                    flexicheck = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.flexicheckbox))
                    if (flexicheck).is_selected():
                        print("is selected")
                        break
                    else:
                        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.flexicheckbox)).click()
                        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.fl)
                        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.fl)).send_keys(1)
                    break
                elif (leavetype == 'earned'):
                    self.driver.find_element(By.XPATH,
                                             "//table[@class='ui-datepicker-calendar']//tr[2]//td[not(@class=' ui-datepicker-week-end ') and @data-handler='selectDay'][" + str(
                                                 j+3) +"]/a[1]").click()
                    earnedcheck = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.earnedcheckbox))
                    if (earnedcheck).is_selected():
                        print("is selected")
                        break
                    else:
                        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.earnedcheckbox)).click()
                        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.el)
                        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.el)).send_keys(1)
                    break
                elif (leavetype == 'compoff'):
                    self.driver.find_element(By.XPATH,
                                             "//table[@class='ui-datepicker-calendar']//tr[2]//td[not(@class=' ui-datepicker-week-end ') and @data-handler='selectDay'][" + str(
                                                 j+4) +"]/a[1]").click()
                    compocheck = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.compoffcheckbox))
                    if (compocheck).is_selected():
                        print("is selected")
                        break
                    else:
                        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.compoffcheckbox)).click()
                        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.co)).send_keys(1)
                    break
                elif (leavetype == 'wfh'):
                    self.driver.find_element(By.XPATH,
                                             "//table[@class='ui-datepicker-calendar']//tr[3]//td[not(@class=' ui-datepicker-week-end ') and @data-handler='selectDay'][" + str(
                                                 j+4) +"]/a[1]").click()
                    wfhcheck = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.wfhcheckbox))
                    if (wfhcheck).is_selected():
                        print("is selected")
                        break
                    else:
                        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.wfhcheckbox)).click()
                        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.noofwfh)).send_keys("1")
                    break
            if(i==2):
                break
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.leavetodate)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.leavetodate)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.fromdatedays)
            self.logger.info("wait untill To date calendar appears")
        Commonfunctions.selectbytext(self.driver.find_element(By.XPATH,(HRPortal_PageObjects.shiftypedropdown)),shifttype)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.pendingtask)).send_keys("Nil")
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.reason)).send_keys("AutomationTesting")
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.submitbutton)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.submitbutton)).click()

    def Employee_leaveapply_success(self):
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.leavesummary)
        isdisplayed = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.leavesummary)).is_displayed()
        return isdisplayed



    def Employee_PermissionRequest(self):
        try:
            self.logger.info("Employee Leave Management Menu clicks ")
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.leavemanagement)).click()
        except:
            print("")
        self.logger.info("wait until Request Permission clicks")
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.requestpermission)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.requestpermission)).click()
        self.logger.info("wait until Request Permission form appears")
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.permissionclick)
        self.logger.info("Request permission date clicks")
        self.driver.find_element(By.XPATH,(HRPortal_PageObjects.permissionclick)).click()
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.fromdatedays)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.permissiondate)).click()
        time.sleep(1)
        self.driver.execute_script("document.getElementById('ContentPlaceHolder1_txtFromTime').value = '04:00 PM'")
        time.sleep(1)
        self.driver.execute_script("document.getElementById('ContentPlaceHolder1_txtToTime').value = '07:00 PM'")
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.permissionreason)).send_keys("Test Permission")
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.permissionsubmit)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.permissionsubmit)).click()
        try:
            isdisplayedalert = self.driver.find_element(By.XPATH,"//*[@id='ContentPlaceHolder1_ErrorMessage'][contains(text(),'Already you were applied leave for this date')]").is_displayed()
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.permissionclick)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.fromdatedays)
            self.driver.find_element(By.XPATH,
                                 "//table[@class='ui-datepicker-calendar']//tr[2]//td[not(@class=' ui-datepicker-week-end ') and @data-handler='selectDay'][5]/a[1]").click()
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.permissionsubmit)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.permissionsubmit)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.permissionsummary)
            isdisplayed = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.permissionsummary)).is_displayed()
            return isdisplayed
        except:
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.permissionsummary)
            isdisplayed = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.permissionsummary)).is_displayed()
            return isdisplayed

    # def Employee_WFHRequest(self):
    #     self.logger.info("Employee Leave Management Menu clicks ")
    #     self.driver.find_element(By.XPATH, (HRPortal_PageObjects.leavemanagement)).click()
    #     self.logger.info("wait until Request Permission clicks")
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.requestwfh)
    #     self.driver.find_element(By.XPATH, (HRPortal_PageObjects.requestwfh)).click()
    #     self.logger.info("wait until Request Permission form appears")
    #     Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.newpermissionrequest)
    #     self.logger.info("Request permission date clicks")
    #     self.driver.find_element(By.XPATH,(HRPortal_PageObjects.permissionclick)).click()
    #     Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.fromdatedays)
    #     self.driver.find_element(By.XPATH, (HRPortal_PageObjects.permissiondate)).click()
    #     time.sleep(1)
    #     self.driver.execute_script("document.getElementById('ContentPlaceHolder1_txtFromTime').value = '04:00 PM'")
    #     time.sleep(1)
    #     self.driver.execute_script("document.getElementById('ContentPlaceHolder1_txtToTime').value = '07:00 PM'")
    #     Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.permissionsubmit)
    #     self.driver.find_element(By.XPATH, (HRPortal_PageObjects.permissionsubmit)).click()

    def Employee_WFHRequest_success(self):
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.wfhsummary)
        isdisplayed = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.wfhsummary)).is_displayed()
        return isdisplayed

    def Employee_LeaveDetails(self,empid,leavetype):
        try:
            # if leavetype == 'casual':
            time.sleep(2)
            # Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.moredetails)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.moredetails)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.leavedetailspage)
        except:
            print("")
        try:
            leavemode=self.driver.find_element(By.XPATH, "//table[@id='ContentPlaceHolder1_grdLeaveDetails']/tbody/tr/td/span[contains(text(),'"+empid+"')]//following::span[contains(text(),'"+leavetype+"')]").text
            self.driver.find_element(By.XPATH,
                                     "//table[@id='ContentPlaceHolder1_grdLeaveDetails']/tbody/tr/td/span[contains(text(),'" + empid + "')]//following::span[contains(text(),'" + leavetype + "')]").click()
            print(leavemode)
            totaldays=self.driver.find_element(By.XPATH, ("//table[@id='ContentPlaceHolder1_grdLeaveDetails']/tbody/tr/td/span[contains(text(),'"+empid+"')]//following::span[contains(text(),'"+leavetype+"')]//following::span[1]")).text
            print(totaldays)
            if leavetype=='CL' and leavemode=='CL' and totaldays=='1':
                return True
            if leavetype=='EL' and leavemode=='EL' and totaldays=='1':
                return True
            if leavetype=='FL' and leavemode=='FL' and totaldays=='1':
                return True
            if leavetype=='CO' and leavemode=='CO' and totaldays=='1':
                return True
        except:
            value = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonth)).get_attribute('value')
            value = int(value) - 1
            print("the value in select", value)
            Commonfunctions.selectbyindex(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonthclick)), value)
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.leavesearch)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.leavesearch)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.leavemode)
            leavemode = self.driver.find_element(By.XPATH,
                                                 "//table[@id='ContentPlaceHolder1_grdLeaveDetails']/tbody/tr/td/span[contains(text(),'" + empid + "')]//following::span[contains(text(),'" + leavetype + "')]").text
            self.driver.find_element(By.XPATH,
                                     "//table[@id='ContentPlaceHolder1_grdLeaveDetails']/tbody/tr/td/span[contains(text(),'" + empid + "')]//following::span[contains(text(),'" + leavetype + "')]").click()
            print(leavemode)
            totaldays = self.driver.find_element(By.XPATH, (
                        "//table[@id='ContentPlaceHolder1_grdLeaveDetails']/tbody/tr/td/span[contains(text(),'" + empid + "')]//following::span[contains(text(),'" + leavetype + "')]//following::span[1]")).text
            print(totaldays)
            if leavetype == 'CL' and leavemode == 'CL' and totaldays == '1':
                return True
            if leavetype == 'EL' and leavemode == 'EL' and totaldays == '1':
                return True
            if leavetype == 'FL' and leavemode == 'FL' and totaldays == '1':
                return True
            if leavetype == 'CO' and leavemode == 'CO' and totaldays == '1':
                return True


    def Employee_WFHDetails(self,empid, leavetype):
        try:
            # if leavetype == 'casual':
            time.sleep(2)
            # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.wfhmoredetails)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.wfhmoredetails)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.leavedetailspage)
        except:
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.profileclick)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.profileclick)).click()
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.homeclick)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.homeclick)).click()
            Commonfunctions.Waitvisible(self.driver, "//h4[contains(text(),'Leave Management')]")
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.leavemanagement)).click()
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.wfhmoredetails)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.wfhmoredetails)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.leavedetailspage)
        try:
            leavemode = self.driver.find_element(By.XPATH,
                                                 "//table[@id='ContentPlaceHolder1_grdLeaveDetails']/tbody/tr/td/span[contains(text(),'" + empid + "')]//following::span[contains(text(),'" + leavetype + "')]").text
            self.driver.find_element(By.XPATH,
                                     "//table[@id='ContentPlaceHolder1_grdLeaveDetails']/tbody/tr/td/span[contains(text(),'" + empid + "')]//following::span[contains(text(),'" + leavetype + "')]").click()
            print(leavemode)
            totaldays = self.driver.find_element(By.XPATH, (
                    "//table[@id='ContentPlaceHolder1_grdLeaveDetails']/tbody/tr/td/span[contains(text(),'" + empid + "')]//following::span[contains(text(),'" + leavetype + "')]//following::span[1]")).text
            print(totaldays)
            if leavetype == 'WFH' and leavemode == 'WFH' and totaldays == '1':
                return True
        except:
            value = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonth)).get_attribute('value')
            value = int(value) - 1
            print("the value in select", value)
            Commonfunctions.selectbyindex(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonthclick)), value)
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.leavesearch)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.leavesearch)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.leavemode)
            leavemode = self.driver.find_element(By.XPATH,
                                                 "//table[@id='ContentPlaceHolder1_grdLeaveDetails']/tbody/tr/td/span[contains(text(),'" + empid + "')]//following::span[contains(text(),'" + leavetype + "')]").text
            self.driver.find_element(By.XPATH,
                                     "//table[@id='ContentPlaceHolder1_grdLeaveDetails']/tbody/tr/td/span[contains(text(),'" + empid + "')]//following::span[contains(text(),'" + leavetype + "')]").click()
            print(leavemode)
            totaldays = self.driver.find_element(By.XPATH, (
                    "//table[@id='ContentPlaceHolder1_grdLeaveDetails']/tbody/tr/td/span[contains(text(),'" + empid + "')]//following::span[contains(text(),'" + leavetype + "')]//following::span[1]")).text
            print(totaldays)
            if leavetype == 'WFH' and leavemode == 'WFH' and totaldays == '1':
                return True

    def Employee_LeaveStatus(self,empid,leavetype):
        try:
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.leavemanagement)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.leavesummarypage)
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.moredetails)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.moredetails)).click()
            # Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.leavedetailspage)
        except:
            print("")

        try:
            Commonfunctions.Waitvisible(self.driver, "//table[@id='ContentPlaceHolder1_grdLeaveDetails']/tbody/tr/td/span[contains(text(),'" + empid + "')]//following::span[contains(text(),'" + leavetype + "')]//following::span[8][contains(text(),'Approved')]")
            isdisplayed = self.driver.find_element(By.XPATH,
                                                   "//table[@id='ContentPlaceHolder1_grdLeaveDetails']/tbody/tr/td/span[contains(text(),'" + empid + "')]//following::span[contains(text(),'" + leavetype + "')]//following::span[8][contains(text(),'Approved')]").is_displayed()
            return isdisplayed
        except:
            value = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonth)).get_attribute('value')
            value = int(value) - 1
            print("the value in select", value)
            Commonfunctions.selectbyindex(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonthclick)), value)
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.leavesearch)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.leavesearch)).click()
            Commonfunctions.Waitvisible(self.driver, "//table[@id='ContentPlaceHolder1_grdLeaveDetails']/tbody/tr/td/span[contains(text(),'"+empid+"')]//following::span[contains(text(),'"+leavetype+"')]//following::span[8][contains(text(),'Approved')]")
            print("")
            isdisplayed = self.driver.find_element(By.XPATH, "//table[@id='ContentPlaceHolder1_grdLeaveDetails']/tbody/tr/td/span[contains(text(),'"+empid+"')]//following::span[contains(text(),'"+leavetype+"')]//following::span[8][contains(text(),'Approved')]").is_displayed()
            return isdisplayed

    def Employee_PermissionStatus(self,empid):
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.profileclick)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.profileclick)).click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.homeclick)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.homeclick)).click()
        Commonfunctions.Waitvisible(self.driver, "//h4[contains(text(),'Leave Management')]")
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.leavemanagement)).click()
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.leavesummarypage)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.permissionmoredetails)).click()
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.permissiondetailspage)
        try:
            isdisplayed = self.driver.find_element(By.XPATH,
                                                   "//table[@id='ContentPlaceHolder1_gvPermissionLog']/tbody/tr/td/span[contains(text(),'" + empid + "')]//following::span[contains(text(),'Approved')]").is_displayed()
            return isdisplayed
        except:
            value = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonth)).get_attribute('value')
            value = int(value) - 1
            print("the value in select", value)
            Commonfunctions.selectbyindex(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonthclick)), value)
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.leavesearch)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.leavesearch)).click()
            isdisplayed = self.driver.find_element(By.XPATH, "//table[@id='ContentPlaceHolder1_gvPermissionLog']/tbody/tr/td/span[contains(text(),'"+empid+"')]//following::span[contains(text(),'Approved')]").is_displayed()
            return isdisplayed

    def Employee_WFHStatus(self,empid):
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.profileclick)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.profileclick)).click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.homeclick)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.homeclick)).click()
        Commonfunctions.Waitvisible(self.driver, "//h4[contains(text(),'Leave Management')]")
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.leavemanagement)).click()
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.leavesummarypage)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.wfhmoredetails)).click()
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.leavedetailspage)
        try:
            isdisplayed = self.driver.find_element(By.XPATH,
                                                   "//table[@id='ContentPlaceHolder1_grdLeaveDetails']/tbody/tr/td/span[contains(text(),'" + empid + "')]//following::span[contains(text(),'Approved')]").is_displayed()
            return isdisplayed
        except:
            value = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonth)).get_attribute('value')
            value = int(value) - 1
            print("the value in select", value)
            Commonfunctions.selectbyindex(
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonthclick)), value)
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.leavesearch)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.leavesearch)).click()
            isdisplayed = self.driver.find_element(By.XPATH, "//table[@id='ContentPlaceHolder1_grdLeaveDetails']/tbody/tr/td/span[contains(text(),'"+empid+"')]//following::span[contains(text(),'Approved')]").is_displayed()
            return isdisplayed

    def Employee_attendancereport(self,leavetype):
        try:
            self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div/div/div[2]/div/div/div[contains(text(),'Monthly Attendance')]").is_displayed()
            Commonfunctions.Waitvisible(self.driver, "//*[@id='page-wrapper']/div/div/div[2]/div/div/div[contains(text(),'Monthly Attendance')]")
        except:
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.profileclick)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.profileclick)).click()
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.homeclick)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.homeclick)).click()
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemanagement)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.Bioattendancepage)
            Commonfunctions.mousehover(self.driver,self.driver.find_element(By.XPATH, (HRPortal_PageObjects.myattendance)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.viewattendance)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.viewattendance)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.monthlyattendancepage)
        try:
            if leavetype=='CL':
                isdisplayed = self.driver.find_element(By.XPATH, "//*[@id='tblAttendance']//following::span[contains(text(),'"+leavetype+"')]").is_displayed()
                return isdisplayed
            if leavetype=='EL':
                isdisplayed = self.driver.find_element(By.XPATH, "//*[@id='tblAttendance']//following::span[contains(text(),'"+leavetype+"')]").is_displayed()
                return isdisplayed
            if leavetype=='FL':
                isdisplayed = self.driver.find_element(By.XPATH, "//*[@id='tblAttendance']//following::span[contains(text(),'"+leavetype+"')]").is_displayed()
                return isdisplayed
            if leavetype == 'CO':
                isdisplayed = self.driver.find_element(By.XPATH,
                                                       "//*[@id='tblAttendance']//following::span[contains(text(),'" + leavetype + "')]").is_displayed()
                return isdisplayed
            if leavetype == 'P':
                isdisplayed = self.driver.find_element(By.XPATH,
                                                       "//*[@id='tblAttendance']//following::span[contains(text(),'P') and not (contains(text(),'LOP'))]").is_displayed()
                return isdisplayed
            if leavetype == 'ULOP':
                isdisplayed = self.driver.find_element(By.XPATH,
                                                       "//*[@id='tblAttendance']//following::span[contains(text(),'ULOP')]").is_displayed()
                return isdisplayed
            if leavetype == 'SO':
                isdisplayed = self.driver.find_element(By.XPATH,
                                                       "//*[@id='tblAttendance']//following::span[contains(text(),'SO')]").is_displayed()
                return isdisplayed
            if leavetype=='NH':
                isdisplayed = self.driver.find_element(By.XPATH, "//*[@id='tblAttendance']//following::span[contains(text(),'"+leavetype+"')]").is_displayed()
                return isdisplayed
        except:
            # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.attendancemonthclick)
            value = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonth)).get_attribute('value')
            value = int(value) - 1
            print("the value in select",value)
            Commonfunctions.selectbyindex(self.driver.find_element(By.XPATH,(HRPortal_PageObjects.attendancemonthclick)),value)
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.monthsearch)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.monthsearch)).click()
            if leavetype=='CL':
                isdisplayed = self.driver.find_element(By.XPATH, "//*[@id='tblAttendance']//following::span[contains(text(),'"+leavetype+"')]").is_displayed()
                return isdisplayed
            if leavetype=='EL':
                isdisplayed = self.driver.find_element(By.XPATH, "//*[@id='tblAttendance']//following::span[contains(text(),'"+leavetype+"')]").is_displayed()
                return isdisplayed
            if leavetype=='FL':
                isdisplayed = self.driver.find_element(By.XPATH, "//*[@id='tblAttendance']//following::span[contains(text(),'"+leavetype+"')]").is_displayed()
                return isdisplayed
            if leavetype == 'CO':
                isdisplayed = self.driver.find_element(By.XPATH,
                                                       "//*[@id='tblAttendance']//following::span[contains(text(),'" + leavetype + "')]").is_displayed()
                return isdisplayed
            if leavetype == 'P':
                isdisplayed = self.driver.find_element(By.XPATH,
                                                       "//*[@id='tblAttendance']//following::span[contains(text(),'P') and not (contains(text(),'LOP'))]").is_displayed()
                return isdisplayed
            if leavetype == 'ULOP':
                isdisplayed = self.driver.find_element(By.XPATH,
                                                       "//*[@id='tblAttendance']//following::span[contains(text(),'ULOP')]").is_displayed()
                return isdisplayed
            if leavetype == 'SO':
                isdisplayed = self.driver.find_element(By.XPATH,
                                                       "//*[@id='tblAttendance']//following::span[contains(text(),'SO')]").is_displayed()
                return isdisplayed
            if leavetype=='NH':
                isdisplayed = self.driver.find_element(By.XPATH, "//*[@id='tblAttendance']//following::span[contains(text(),'"+leavetype+"')]").is_displayed()
                return isdisplayed

    def Employee_Viewattendancereport(self):
        try:
            # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.attendancemanagement)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemanagement)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.Bioattendancepage)
            Commonfunctions.mousehover(self.driver,self.driver.find_element(By.XPATH, (HRPortal_PageObjects.myattendance)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.viewattendance)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.viewattendance)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.monthlyattendancepage)
        except:
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.profileclick)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.profileclick)).click()
            Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.homeclick)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.homeclick)).click()
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemanagement)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.Bioattendancepage)
            Commonfunctions.mousehover(self.driver,
                                       self.driver.find_element(By.XPATH, (HRPortal_PageObjects.myattendance)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.viewattendance)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.viewattendance)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.monthlyattendancepage)

    def Employee_LOPattendanceverify(self,empid):
        try:
            lop = self.driver.find_element(By.XPATH, "//*[@id='tblAttendance']/tbody/tr[1]/td[contains(text(),'"+empid+"')]//following::td[2]").text
            if lop == 'LOP':
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.lopattendance)).click()
                return True
            elif lop == '':
                value = self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonth)).get_attribute(
                    'value')
                value = int(value) - 1
                print("the value in select", value)
                Commonfunctions.selectbyindex(
                    self.driver.find_element(By.XPATH, (HRPortal_PageObjects.attendancemonthclick)), value)
                Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.monthsearch)
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.monthsearch)).click()
                Commonfunctions.Waitvisible(self.driver, "//*[@id='tblAttendance']/tbody/tr[1]/td[contains(text(),'" + empid + "')]//following::td[32]")
                self.driver.find_element(By.XPATH, (HRPortal_PageObjects.lopattendance)).click()
                return True

        except:
            print("")

    def Employee_attendanceFreezeverify(self):
        try:
            freezedate = self.driver.find_element(By.XPATH, "//table[@id='tblAttendance']//following::th[last()][contains(text(),'21')]").is_displayed()
            self.driver.find_element(By.XPATH, "//table[@id='tblAttendance']//following::th[last()][contains(text(),'21')]").click()
            return freezedate

        except:
            print("")

            # freezedate = self.driver.find_element(By.XPATH,
            #                                       "//table[@id='tblAttendance']//following::th[last()][contains(text(),'22')]").is_displayed()
            # self.driver.find_element(By.XPATH,
            #                          "//table[@id='tblAttendance']//following::th[last()][contains(text(),'22')]").click()
            # return freezedate




    def Employee_RaiseLop(self):
        # try:
        # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.attendancemanagement)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.raiselop)).click()
        lopdate = self.driver.find_elements(By.XPATH,"//*[@id='ContentPlaceHolder1_dgvChangeLOPRequest']/tbody/tr")
        print("lop date",lopdate)
        # self.loprecord = len(lopdate)+1
        pagination = self.driver.find_elements(By.XPATH, (HRPortal_PageObjects.attendancepagination))
        print("Total pages",pagination)
        print("lop date", lopdate)
        for j in range(1,len(pagination)+1):
            print("total pages are",len(pagination)+1)
            for i in range(1,len(lopdate)+1):
                lopdays = self.driver.find_element(By.XPATH,"//*[@id='ContentPlaceHolder1_dgvChangeLOPRequest']/tbody/tr["+str(i)+"]/td[6]").text
                print("lop values are",lopdays)
                if (i==10):
                    self.driver.find_element(By.XPATH, (HRPortal_PageObjects.loprequestnext)).click()
                if('23-' in lopdays):
                    self.driver.find_element(By.XPATH, "//*[@id='ContentPlaceHolder1_dgvChangeLOPRequest']/tbody/tr[" + str(
                        i) + "]/td[6][contains(text(),'23-')]/parent::tr/td/a").click()
                    break
                if ('22-' in lopdays):
                    self.driver.find_element(By.XPATH,
                                             "//*[@id='ContentPlaceHolder1_dgvChangeLOPRequest']/tbody/tr[" + str(
                                                 i) + "]/td[6][contains(text(),'22-')]/parent::tr/td/a").click()
                    break
        Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.LOPrequestpage)
        self.driver.find_element(By.XPATH,(HRPortal_PageObjects.LOPcomments)).send_keys("Test LOP Request")
        Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.LOPrequestsubmit)
        self.driver.find_element(By.XPATH, (HRPortal_PageObjects.LOPrequestsubmit)).click()
        return True

    def Employee_MapEmployeeShiftTime(self,empcode):
        try:
            # Commonfunctions.Waitclick(self.driver, HRPortal_PageObjects.sattendancemgmt)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.sattendancemgmt)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.Bioattendancepage)
            Commonfunctions.mousehover(self.driver,self.driver.find_element(By.XPATH, (HRPortal_PageObjects.shifttime)))
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.shifttimemap)
            self.driver.find_element(By.XPATH, (HRPortal_PageObjects.shifttimemap)).click()
            Commonfunctions.Waitvisible(self.driver, HRPortal_PageObjects.sshifttimemappage)
        except:
            print("")
        try:
            isdisplayed = self.driver.find_element(By.XPATH,
                                     "//table[@id='ContentPlaceHolder1_dgvAddShiftTiming']//following::span[contains(text(),'"+empcode+"')]//following::span[contains(text(),'10:00 AM')]//following::span[contains(text(),'07:45')]")
            return isdisplayed
        except:
            isdisplayed = self.driver.find_element(By.XPATH,
                                                   "//table[@id='ContentPlaceHolder1_dgvAddShiftTiming']//following::span[contains(text(),'" + empcode + "')]")
            return isdisplayed