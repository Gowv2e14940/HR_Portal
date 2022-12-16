import os
import smtplib
import ssl
import time
import unittest
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import allure
import pytest

from Base.Base import Base
from Utilities import ExcelReadandWrite
from Utilities.Commonfunctions import Commonfunctions
from Utilities.Constant import Constant
from Utilities.customLogger import Log
from allure_commons.types import AttachmentType


class AttendanceManagementTest(Base, unittest.TestCase):
    logger = Log.logCreate()
    global total_no_of_testcase
    total_no_of_testcase = 0

    global passtc
    passtc = 0

    global failtc
    failtc = 0

    global startdate
    global starttime
    global start_time_hour
    global start_time_min

    now = datetime.now()
    startdate = now.strftime("%d-%m-%Y")
    starttime = now.strftime("%I:%M:%S:%p")
    start_time_hour = now.strftime("%I")
    start_time_min = now.strftime("%M")

    global mail_start_time
    mail_start_time = "{} & {}".format(startdate, starttime)

    def setUp(self) -> None:
        global input
        data = self._testMethodName
        print("data is", data)
        dd = data.split('_')
        print("split", dd)
        dd.reverse()
        print("reverse", dd.reverse())
        validate = '{}{}{}'.format(dd[1], '_', dd[2])

        print("dd 1", dd[1])
        print("dd 0", dd[2])
        search = validate
        print("search is", search)
        j = ExcelReadandWrite.excelsearch(self.excelname, self.sheetname, search)
        excel_input_data = ExcelReadandWrite.readData(self.excelname, self.sheetname, j, 4)
        if excel_input_data is None:
            print("")
        else:
            input = excel_input_data.split(",")
            # print(input[0],input[1])

    # @pytest.fixture(autouse=True)
    @pytest.mark.order(1)
    def test_LeaveManagement_001(self):
        try:

            self.logger.info("Validating Test case 1")
            print("Launched Browser")
            self.logger.info("Employee Casual Leave Apply")
            self.login.Employee_Login(input[0],input[1])
            self.login.Employee_LoginSuccess()
            self.login.Employee_LeaveRequest('casual','Flexi')
            self.assertTrue(self.login.Employee_leaveapply_success())
        except:
            raise self.failureException

    @pytest.mark.order(2)
    def test_LeaveManagement_002(self):
        try:
            self.logger.info("Validating Test case 2")
            self.logger.info("Employee Earned Leave Apply")
            self.login.Employee_LeaveRequest(input[0],input[1])
            self.assertTrue(self.login.Employee_leaveapply_success())
        except:
            raise self.failureException

    @pytest.mark.run(order=3)
    def test_LeaveManagement_003(self):
        try:

            self.logger.info("Validating Test case 3")
            self.logger.info("Employee Flexi Leave Apply")
            self.login.Employee_LeaveRequest(input[0],input[1])
            self.assertTrue(self.login.Employee_leaveapply_success())
        except:
            raise self.failureException

    @pytest.mark.run(order=4)
    def test_LeaveManagement_004(self):
        try:
            self.logger.info("Validating Test case 4")
            self.logger.info("Employee Compoff Apply")
            self.login.Employee_LeaveRequest(input[0],input[1])
            self.assertTrue(self.login.Employee_leaveapply_success())
        except:
            raise self.failureException

    @pytest.mark.run(order=5)
    def test_LeaveManagement_005(self):
        try:
            self.logger.info("Validating Test case 5")
            self.logger.info("Employee Permission Request Apply")
            self.assertTrue(self.login.Employee_PermissionRequest())

        except:
            raise self.failureException

    @pytest.mark.run(order=6)
    def test_LeaveManagement_006(self):
        try:

            self.logger.info("Validating Test case 6")
            self.logger.info("Employee WFH Apply")
            self.login.Employee_LeaveRequest(input[0],input[1])
            self.assertTrue(self.login.Employee_WFHRequest_success())

        except:
            raise self.failureException

    @pytest.mark.order(7)
    def test_LeaveManagement_007(self):
        try:
            self.logger.info("Validating Test case 7")
            self.logger.info("Employee Casual Leave Applied Validation")
            self.assertTrue(self.login.Employee_LeaveDetails(input[0],input[1]))
            Commonfunctions.screenshot(self.driver, 'casual.png')

            # self.driver.close()
        except:
            raise self.failureException

    @pytest.mark.run(order=8)
    def test_LeaveManagement_008(self):
        try:
            self.logger.info("Validating Test case 8")
            self.logger.info("Employee Earned Leave Applied Validation")
            self.assertTrue(self.login.Employee_LeaveDetails(input[0],input[1]))
            Commonfunctions.screenshot(self.driver, 'earned.png')
        except:
            raise self.failureException

    @pytest.mark.run(order=9)
    def test_LeaveManagement_009(self):
        try:
            self.logger.info("Validating Test case 9")
            self.logger.info("Employee Flexi Leave Applied Validation")
            self.assertTrue(self.login.Employee_LeaveDetails(input[0],input[1]))
            Commonfunctions.screenshot(self.driver, 'flexi.png')
        except:
            raise self.failureException

    @pytest.mark.run(order=10)
    def test_LeaveManagement_010(self):
        try:
            self.logger.info("Validating Test case 10")
            self.logger.info("Employee Compoff Leave Applied Validation")
            self.assertTrue(self.login.Employee_LeaveDetails(input[0],input[1]))
            Commonfunctions.screenshot(self.driver, 'compoff.png')
        except:
            raise self.failureException

    @pytest.mark.run(order=11)
    def test_LeaveManagement_011(self):
        try:
            self.logger.info("Validating Test case 11")
            self.logger.info("Employee WFH Applied Validation")
            self.assertTrue(self.login.Employee_WFHDetails(input[0],input[1]))
            Commonfunctions.screenshot(self.driver, 'wfh.png')
        except:
            raise self.failureException

    @pytest.mark.run(order=12)
    def test_LeaveManagement_012(self):
        try:
            # self.driver.close()
            self.login.Employee_Logout()
            self.logger.info("Validating Test case 12")
            # Base.setUpClass()
            self.driver.get(self.baseURL)
            self.logger.info("Supervisor Casual Leave Approve")
            self.supervisor.Supervisor_Login(input[0], input[1])
            self.login.Employee_LoginSuccess()
            self.supervisor.Supervisor_LeaveApprove(input[2], input[3])
            # self.driver.close()
        except:
            raise self.failureException

    @pytest.mark.run(order=13)
    def test_LeaveManagement_013(self):
        try:
            self.logger.info("Validating Test case 13")
            self.logger.info("Supervisor Earned Leave Approve")
            self.supervisor.Supervisor_LeaveApprove(input[0], input[1])
            # self.driver.close()
        except:
            raise self.failureException

    @pytest.mark.run(order=14)
    def test_LeaveManagement_014(self):
        try:

            self.logger.info("Validating Test case 14")
            self.logger.info("Supervisor Flexi Leave Approve")
            self.supervisor.Supervisor_LeaveApprove(input[0], input[1])
            # self.driver.close()
        except:
            raise self.failureException

    @pytest.mark.run(order=15)
    def test_LeaveManagement_015(self):
        try:
            self.logger.info("Validating Test case 15")
            self.logger.info("Supervisor Compoff Leave Approve")
            self.supervisor.Supervisor_LeaveApprove(input[0], input[1])
            # self.driver.close()
        except:
            raise self.failureException

    @pytest.mark.run(order=16)
    def test_LeaveManagement_016(self):
        try:
            self.logger.info("Validating Test case 16")
            self.logger.info("Supervisor Permission Request Approve")
            self.supervisor.Supervisor_PermissionApprove(input[0])
            # self.driver.close()
        except:
            raise self.failureException

    @pytest.mark.run(order=17)
    def test_LeaveManagement_017(self):
        try:
            self.logger.info("Validating Test case 12")
            self.logger.info("Supervisor WFH request Approve")
            self.supervisor.Supervisor_WFHApprove(input[0], input[1])
            # self.driver.close()
        except:
            raise self.failureException

    @pytest.mark.order(18)
    def test_LeaveManagement_018(self):
        try:
            self.login.Employee_Logout()
            self.logger.info("Validating Test case 18")
            self.driver.get(self.baseURL)
            self.logger.info("Employee Casual Leave status")
            self.login.Employee_Login(input[0], input[1])
            self.login.Employee_LoginSuccess()
            self.assertTrue(self.login.Employee_LeaveStatus(input[2], input[3]))
            Commonfunctions.screenshot(self.driver, 'casualapproved.png')

        except:
            raise self.failureException

    @pytest.mark.order(19)
    def test_LeaveManagement_019(self):
        try:
            self.logger.info("Validating Test case 19")
            self.logger.info("Employee Earned Leave status")
            self.assertTrue(self.login.Employee_LeaveStatus(input[0], input[1]))
            Commonfunctions.screenshot(self.driver, 'earnedapproved.png')
        except:
            raise self.failureException

    @pytest.mark.order(20)
    def test_LeaveManagement_020(self):
        try:
            self.logger.info("Validating Test case 20")
            self.logger.info("Employee Flexi Leave status")
            self.assertTrue(self.login.Employee_LeaveStatus(input[0], input[1]))
            Commonfunctions.screenshot(self.driver, 'flexiapproved.png')
        except:
            raise self.failureException

    @pytest.mark.order(21)
    def test_LeaveManagement_021(self):
        try:
            self.logger.info("Validating Test case 21")
            self.logger.info("Employee Compoff Leave status")
            self.assertTrue(self.login.Employee_LeaveStatus(input[0], input[1]))
            Commonfunctions.screenshot(self.driver, 'compoffapproved.png')
        except:
            raise self.failureException

    @pytest.mark.order(22)
    def test_LeaveManagement_022(self):
        try:
            self.logger.info("Validating Test case 22")
            self.logger.info("Employee Permission status")
            self.assertTrue(self.login.Employee_PermissionStatus(input[0]))
            Commonfunctions.screenshot(self.driver, 'permissionapproved.png')
        except:
            raise self.failureException

    @pytest.mark.order(23)
    def test_LeaveManagement_023(self):
        try:
            self.logger.info("Validating Test case 23")
            self.logger.info("Employee WFH status")
            self.assertTrue(self.login.Employee_WFHStatus(input[0]))
            Commonfunctions.screenshot(self.driver, 'wfhapproved.png')
        except:
            raise self.failureException

    @pytest.mark.order(24)
    def test_LeaveManagement_024(self):
        try:
            # self.login.Employee_Logout()
            self.logger.info("Validating Test case 24")
            # self.driver.get(self.baseURL)
            self.logger.info("Employee Casual Leave Attendance Report")
            # self.login.Employee_Login(input[0], input[1])
            # self.login.Employee_LoginSuccess()
            self.assertTrue(self.login.Employee_attendancereport('CL'))
            Commonfunctions.screenshot(self.driver, 'casualattendance.png')
            # self.driver.close()
        except:
            raise self.failureException

    @pytest.mark.order(25)
    def test_LeaveManagement_025(self):
        try:
            self.logger.info("Validating Test case 25")
            self.logger.info("Employee Earned Leave Attendance Report")
            self.assertTrue(self.login.Employee_attendancereport('EL'))
            Commonfunctions.screenshot(self.driver, 'earnedattendance.png')
            # self.driver.close()
        except:
            raise self.failureException

    @pytest.mark.order(26)
    def test_LeaveManagement_026(self):
        try:

            self.logger.info("Validating Test case 26")
            self.logger.info("Employee Flexi Leave Attendance Report")
            self.assertTrue(self.login.Employee_attendancereport('FL'))
            Commonfunctions.screenshot(self.driver, 'flexiattendance.png')
            # self.driver.close()
        except:
            raise self.failureException

    @pytest.mark.order(27)
    def test_LeaveManagement_027(self):
        try:

            self.logger.info("Validating Test case 27")
            self.logger.info("Employee Compoff Attendance Report")
            self.assertTrue(self.login.Employee_attendancereport('CO'))
            Commonfunctions.screenshot(self.driver, 'compoffattendance.png')
            # self.driver.close()
        except:
            raise self.failureException

    @pytest.mark.order(28)
    def test_LeaveManagement_028(self):
        try:
            self.login.Employee_Logout()
            self.logger.info("Validating Test case 28")
            self.driver.get(self.baseURL)
            self.logger.info("Supervisor View Team Leave Details Casual Leave")
            self.supervisor.Supervisor_Login(input[0], input[1])
            self.login.Employee_LoginSuccess()
            self.assertTrue(self.supervisor.Supervisor_Team_LeaveDetails(input[2], input[3]))
            Commonfunctions.screenshot(self.driver, 'casualteamdetails.png')
            time.sleep(2)
        except:
            raise self.failureException
        # finally:
        #     self.db.dbconnection('V2E06428', 'CL', '1')

    @pytest.mark.order(29)
    def test_LeaveManagement_029(self):
        try:

            self.logger.info("Validating Test case 29")
            self.logger.info("Supervisor View Team Leave Details Earned Leave")
            self.assertTrue(self.supervisor.Supervisor_Team_LeaveDetails(input[0], input[1]))
            Commonfunctions.screenshot(self.driver, 'earnedteamdetails.png')

        except:
            raise self.failureException
        # finally:
        #     time.sleep(2)
        #     self.db.dbconnection('V2E06428', 'EL', '3')

    @pytest.mark.order(30)
    def test_LeaveManagement_030(self):
        try:
            self.logger.info("Validating Test case 30")
            self.logger.info("Supervisor View Team Leave Details Flexi Leave")
            self.assertTrue(self.supervisor.Supervisor_Team_LeaveDetails(input[0], input[1]))
            Commonfunctions.screenshot(self.driver, 'flexiteamdetails.png')
        except:
            raise self.failureException
        # finally:
        #     time.sleep(2)
        #     self.db.dbconnection('V2E06428', 'FL', '2')

    @pytest.mark.order(31)
    def test_LeaveManagement_031(self):
        try:
            self.logger.info("Validating Test case 31")
            self.logger.info("Supervisor View Team Leave Details Compoff Leave")
            self.assertTrue(self.supervisor.Supervisor_Team_LeaveDetails(input[0], input[1]))
            Commonfunctions.screenshot(self.driver, 'compoffteamdetails.png')

        except:
            raise self.failureException
        # finally:
        #     time.sleep(2)
        #     self.db.dbconnection('V2E06428', 'CO', '4')

    @pytest.mark.order(32)
    def test_LeaveManagement_032(self):
        try:
            self.logger.info("Validating Test case 32")
            self.logger.info("Supervisor View Team Leave Details Permission")
            # self.assertTrue(self.supervisor.Supervisor_Team_permissionDetails('Permission','Vee5'))
            self.supervisor.Supervisor_Team_permissionDetails(input[0], input[1],input[2])
            Commonfunctions.screenshot(self.driver, 'permissionteamdetails.png')

        except:
            raise self.failureException
        # finally:
        #     time.sleep(2)
        #     self.db.dbconnection_permission('V2E06428')

    @pytest.mark.order(33)
    def test_LeaveManagement_033(self):
        try:
            self.logger.info("Validating Test case 33")
            self.logger.info("Supervisor View Team Leave Details WFH Details")
            self.assertTrue(self.supervisor.Supervisor_Team_WfhDetails(input[0], input[1]))
            Commonfunctions.screenshot(self.driver, 'wfhteamdetails.png')
        except:
            raise self.failureException
        finally:
            time.sleep(2)
            # self.driver.close()
            self.db.dbconnection(input[2], 'CL', '1')
            self.db.dbconnection(input[2], 'EL', '3')
            self.db.dbconnection(input[2], 'FL', '2')
            self.db.dbconnection(input[2], 'CO', '4')
            self.db.dbconnection_permission(input[2])
            self.db.dbconnection(input[2], 'WFH', '9')


    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

    def tearDown(self):
        global total_no_of_testcase
        total_no_of_testcase = total_no_of_testcase + 1
        if hasattr(self, '_outcome'):
            result = self.defaultTestResult()
            self._feedErrorsToResult(result, self._outcome.errors)
        else:
            result = getattr(self, '_outcomeForDoCleanups', self._resultForDoCleanups)
        error = self.list2reason(result.errors)
        failure = self.list2reason(result.failures)
        ok = not error and not failure
        if not ok:
            data = self._testMethodName
            dd = data.split('_')
            dd.reverse()
            validate = '{}{}{}'.format(dd[1], '_', dd[0])
            search = validate
            j = ExcelReadandWrite.excelsearch(self.excelname, self.sheetname, search)
            ExcelReadandWrite.writeData(self.excelname, self.sheetname, j, 8, "FAIL")
            allure.attach(self.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
            global failtc
            failtc = failtc + 1
        else:
            data = self._testMethodName
            dd = data.split('_')
            dd.reverse()
            validate = '{}{}{}'.format(dd[1], '_', dd[0])
            search = validate
            j = ExcelReadandWrite.excelsearch(self.excelname, self.sheetname, search)
            ExcelReadandWrite.writeData(self.excelname, self.sheetname, j, 8, "PASS")
            # allure.attach(self.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
            global passtc
            passtc = passtc + 1

    @classmethod
    def tearDownClass(self):

        self.convert_date_end_time(self)
        self.driver.close()
        self.send_mail_test(self)

        # cmd = r'allure generate D:\PythonPyCharmProjects\HireMeeSkillsProject\HireMeeSkill_Dir\LogiticsReports -c -o  D:\PythonPyCharmProjects\HireMeeSkillsProject\HireMeeSkill_Dir\Results'
        # proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # out = proc.communicate()
        # self.driver.close()
        # self.send_mail_test(self)

        #### generate mail purpose ###
        # print("total", total_no_of_testcase)
        # print("pass", passtc)
        # print("fail", failtc)
        # self.driver.close()
        # self.send_mail_test(self)

    #############################################  Send mail ##################################################################################

    def convert_date_end_time(self):
        now = datetime.now()
        enddate = now.strftime("%d-%m-%Y")
        endtime = now.strftime("%I:%M:%S:%p")
        end_time_hour = now.strftime("%I")
        end_time_min = now.strftime("%M")

        convert_start_time_hour_int = int(start_time_hour)
        convert_start_time_min_int = int(start_time_min)
        convert_end_time_hour_int = int(end_time_hour)
        convert_end_time_min_int = int(end_time_min)

        hour = convert_end_time_hour_int - convert_start_time_hour_int
        minute = convert_end_time_min_int - convert_start_time_min_int

        global mail_end_time
        mail_end_time = "{} & {}".format(enddate, endtime)

        global mail_overall_execution
        mail_overall_execution = " {} hr:{} min".format(hour, minute)
        print("mail_overall_execution", mail_overall_execution)

        global pass_percentage
        pass_percentage = passtc * 100 // total_no_of_testcase

    def send_mail_test(self):
        print("data")
        smtp_server = "smtp.office365.com"
        port = 587  # For starttls
        sender_email = "vts-info@veetechnologies.com"
        password = "Ik-3hl8Xs]cr"
        message = MIMEMultipart("alternative")
        message["Subject"] = "HRportal_LMS Automation Test"

        ####################  Testing Configuration ##############################
        host = "HRPortal_LMS"
        projectname = "\nHRPortal_LMS Automation Report"
        operatingsystem = "Windows 10"
        browser = "Google Chrome"
        regression = "HRPortal_LMS Sanity Report"

        starttime = mail_start_time
        endtime = mail_end_time
        # overall_execution = mail_overall_execution
        strdata = os.getcwd() + '\Reports'
        report = "allure serve {}".format(strdata)
        pass_percent_data = "%"

        html = """
                                                                <center style=padding-bottom:24px>
                                                                                <table width=600 style=width:600px>
                                                                                   <tbody>
                                                                                        <tr height=101 style=padding-top:24px;padding-bottom:24px>
                                                                                           <td width=\"70%\" style=\"width:70%;padding:0\"> <div style="font-size: 22px; center-align: bottom;">
                                                                                                <img src=https://172.17.1.12/hrportal/Images/vee-technologies-logo.png alt=HireMeePro alt="Logo" style="min-height: 50px; min-width: 50px; max-height: 150px; max-width: 150px; align="left">
                                                                                                        <span style="color: rgb(01, 137, 02);"><br>{}</br></span></td>\r\n
                                                                                            </div>
                                                                                        </td>
                                                                                        <td width=50% valign=middle style=width:50%;vertical-align:middle;padding:0>
                                                                                              <h2 style=margin:0;font-size:18px;color:#04a0dc;text-align:right>Test Suite Execution Report</h2>
                                                                                        </td>
                                                                                        </tr>
                                                                                        <tr style=background-color:#fff>
                                                                                         <td style=\"border:1px solid #dddee1;padding:24px;word-break:break-word;word-wrap:break-word\" colspan=\"2\">

                                                                                                <p>Hi Team,<br><br>HRPortal_LMS Automation Sanity Test Case Executed and Here is the summary report.</p></br>
                                                                                                <table class=border width=100% border=1 bgcolor=#f5f7fa style=width:100%;background-color:#f5f7fa;border:1px solid #dddee1>
                                                                                                    <tbody>
                                                                                                        <tr>
                                                                                                            <b><td width=24% style=width:24%>Project Name</td></b>
                                                                                                            <td colspan=3 class=border>{}</td>
                                                                                                        </tr>
                                                                                                        <tr>
                                                                                                           <b> <td>Operating System</td></b>
                                                                                                            <td colspan=3>{}</td>
                                                                                                        </tr>
                                                                                                        <tr>
                                                                                                           <b> <td class=border>Browser</td></b>
                                                                                                            <td colspan=3>{}</td>
                                                                                                        </tr>
                                                                                                         <tr>
                                                                                                          <b>  <td class=border>Start Time</td></b>
                                                                                                            <td colspan=3>{}</td>
                                                                                                        </tr>
                                                                                                        <tr>
                                                                                                           <b> <td class=border>End Time</td></b>
                                                                                                            <td colspan=3>{}</td>
                                                                                                        </tr>                                                                                                        
                                                                                    <tr>
                                                                                   <b><td class=border>Report path</td></b>
                                                                                   <td colspan=3>{}</td>
                                                                               </tr>

                                                                                                        <tr>
                                                                                                           <b> <td>Module Name</td></b>
                                                                                                            <td colspan=3>{}</td>
                                                                                                        </tr>
                                                                                                        <tr>
                                                                                                           <b> <td>Result</td></b>
                                                                                                            <td width=25% style=width:25%;color:blue>Total: {}</td>
                                                                                                            <td width=25% style=width:25%;color:green>Passed: {}</td>
                                                                                                            <td width=25% style=width:25%;color:red>Failed: {}</td>
                                                                                                        </tr>
                                                                                                         <tr>
                                                                                        <b> <td class=border>Pass Percentage</td></b>
                                                                                       <td colspan=3>{}{}</td>
                                                                                   </tr>
                                                                                                    </tbody>
                                                                                                </table>                                                                                            
                                                                                                <br>
                                                                                                <br>This email was sent automatically by Automation Team. Please do not reply.<br><br>Regards,<br>Testing Team </p>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </center> """.format(projectname, host,
                                                                                                 operatingsystem,
                                                                                                 browser, starttime,
                                                                                                 endtime,
                                                                                                 report,
                                                                                                 regression,
                                                                                                 total_no_of_testcase,
                                                                                                 passtc, failtc,
                                                                                                 pass_percentage,
                                                                                                 pass_percent_data)
        part1 = MIMEText(html, "html")
        message.attach(part1)

        # Create a secure SSL context
        context = ssl.create_default_context()
        context = ssl._create_unverified_context()

        # Try to log in to server and send email

        with smtplib.SMTP(smtp_server, port) as server:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()  # Can be omitted
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            # data = 'gowthaman.k@veetechnologies.com'
            data = self.mailid
            # data = 'arunkumar.a@vee2it.com',
            server.sendmail(sender_email, data, message.as_string())
            server.quit()
            # subprocess.Popen(Reportpath, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
