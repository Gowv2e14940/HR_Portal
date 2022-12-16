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


class AttendanceManagmentTest(Base, unittest.TestCase):
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
        j = ExcelReadandWrite.excelsearch(self.excelname, self.sheetname2, search)
        excel_input_data = ExcelReadandWrite.readData(self.excelname, self.sheetname2, j, 4)
        print("j value is",j)
        print("input is",excel_input_data)
        if excel_input_data is None:
            print("")
        else:
            input = excel_input_data.split(",")
            # print(input[0],input[1])

    # @pytest.fixture(autouse=True)
    # @pytest.mark.order(1)
    # def test_Attendancemanagement_001(self):
    #     try:
    #         self.logger.info("Validating Test case 1")
    #         print("Launched Browser")
    #         self.logger.info("Employee LOP Attendance Verify")
    #         self.login.Employee_Login(input[0],input[1])
    #         self.login.Employee_LoginSuccess()
    #         self.login.Employee_Viewattendancereport("LOP")
    #         self.assertTrue(self.login.Employee_LOPattendanceverify())
    #         Commonfunctions.screenshot(self.driver, 'LOPDate.png')
    #     except:
    #         raise self.failureException

    @pytest.mark.order(1)
    def test_Attendancemanagement_001(self):
        try:
            self.logger.info("Validating Test case 1")
            print("Launched Browser")
            self.logger.info("Employee LOP Attendance Verify")
            self.login.Employee_Login(input[0], input[1])
            self.login.Employee_LoginSuccess()
            self.login.Employee_Viewattendancereport()
            self.assertTrue(self.login.Employee_LOPattendanceverify(input[2]))
            Commonfunctions.screenshot(self.driver, 'LOPattendance.png')
        except:
            raise self.failureException

    @pytest.mark.order(2)
    def test_Attendancemanagement_002(self):
        try:
            self.logger.info("Validating Test case 2")
            self.logger.info("Employee Raise LOP Verify")
            # self.login.Employee_RaiseLop()
            self.assertTrue(self.login.Employee_RaiseLop())
            Commonfunctions.screenshot(self.driver, 'LOPRequest.png')
        except:
            raise self.failureException

    @pytest.mark.order(3)
    def test_Attendancemanagement_003(self):
        try:

            self.login.Employee_Logout()
            self.logger.info("Validating Test case 3")
            # Base.setUpClass()
            self.driver.get(self.baseURL)
            self.logger.info("Supervisor Approve LOP Request Verify")
            self.login.Employee_Login(input[0], input[1])
            self.login.Employee_LoginSuccess()
            self.supervisor.Supervisor_ApproveLOP(input[2],"Present")
            Commonfunctions.screenshot(self.driver, 'TLLOPApprove.png')
        except:
            raise self.failureException

    @pytest.mark.order(4)
    def test_Attendancemanagement_004(self):
        try:

            self.login.Employee_Logout()
            self.logger.info("Validating Test case 4")
            # Base.setUpClass()
            self.driver.get(self.baseURL)
            self.logger.info("HR Approve LOP Request Verify")
            self.login.Employee_Login(input[0],input[1])
            self.login.Employee_LoginSuccess()
            self.supervisor.Supervisor_ApproveLOP(input[2], "Present")
            Commonfunctions.screenshot(self.driver, 'HRLOPApprove.png')
        except:
            raise self.failureException

    @pytest.mark.order(5)
    def test_Attendancemanagement_005(self):
        try:
            self.login.Employee_Logout()
            self.logger.info("Validating Test case 05")
            self.driver.get(self.baseURL)
            self.logger.info("Employee Casual Leave Attendance Report")
            self.login.Employee_Login(input[0], input[1])
            self.login.Employee_LoginSuccess()
            self.assertTrue(self.login.Employee_attendancereport('P'))
            Commonfunctions.screenshot(self.driver, 'Presentattendance.png')
            # self.driver.close()
        except:
            raise self.failureException
        # finally:
        #     self.db.dbconnection_ChangeLOPRequest("V2E11587")

    @pytest.mark.order(6)
    def test_Attendancemanagement_006(self):
        try:
            self.login.Employee_Logout()
            self.logger.info("Validating Test case 06")
            self.driver.get(self.baseURL)
            self.logger.info("Employee Casual Leave Attendance Report")
            self.login.Employee_Login(input[0],input[1])
            self.login.Employee_LoginSuccess()
            self.supervisor.Supervisor_ViewTeamattendancereport()
            self.supervisor.Supervisor_viewteamattendance('P',input[2])
            Commonfunctions.screenshot(self.driver, 'SupervisorViewTeampresentattendance.png')
            # self.driver.close()
        except:
            raise self.failureException
        finally:
            self.db.dbconnection_ChangeLOPRequest(input[2])

    @pytest.mark.order(7)
    def test_Attendancemanagement_007(self):
        try:
            self.logger.info("Validating Test case 2")
            self.logger.info("Mark ULOP for employee Verify")
            self.supervisor.Supervisor_MarkULOP(input[0],"ULOP")
            Commonfunctions.screenshot(self.driver, 'SupervisorMarkUlop.png')
        except:
            raise self.failureException

    @pytest.mark.order(8)
    def test_Attendancemanagement_008(self):
        try:
            self.login.Employee_Logout()
            self.logger.info("Validating Test case 8")
            self.driver.get(self.baseURL)
            self.logger.info("Employee ULOP Attendance Verify")
            self.login.Employee_Login(input[0], input[1])
            self.login.Employee_LoginSuccess()
            self.login.Employee_Viewattendancereport()
            self.assertTrue(self.login.Employee_attendancereport("ULOP"))
            Commonfunctions.screenshot(self.driver, 'EmployeeULOPattendance.png')
        except:
            raise self.failureException

    @pytest.mark.order(9)
    def test_Attendancemanagement_009(self):
        try:

            self.login.Employee_Logout()
            self.logger.info("Validating Test case 9")
            # Base.setUpClass()
            self.driver.get(self.baseURL)
            self.logger.info("Supervisor Mark shiftoff Request Verify")
            self.login.Employee_Login(input[0], input[1])
            self.login.Employee_LoginSuccess()
            self.supervisor.Supervisor_MarkShiftoff(input[2], "Shift Off")
            Commonfunctions.screenshot(self.driver, 'SupervisorMarkshiftoff.png')
        except:
            raise self.failureException

    @pytest.mark.order(10)
    def test_Attendancemanagement_010(self):
        try:

            self.login.Employee_Logout()
            self.logger.info("Validating Test case 10")
            # Base.setUpClass()
            self.driver.get(self.baseURL)
            self.logger.info("HR Approve SHiftoff Request Verify")
            self.login.Employee_Login(input[0], input[1])
            self.login.Employee_LoginSuccess()
            self.supervisor.Supervisor_ApproveShiftOff(input[2])
            Commonfunctions.screenshot(self.driver, 'HRshiftoffApprove.png')
        except:
            raise self.failureException

    @pytest.mark.order(11)
    def test_Attendancemanagement_011(self):
        try:
            self.login.Employee_Logout()
            self.logger.info("Validating Test case 11")
            self.driver.get(self.baseURL)
            self.logger.info("Employee SO Attendance Verify")
            self.login.Employee_Login(input[0], input[1])
            self.login.Employee_LoginSuccess()
            self.login.Employee_Viewattendancereport()
            self.assertTrue(self.login.Employee_attendancereport("SO"))
            Commonfunctions.screenshot(self.driver, 'SOattendance.png')
        except:
            raise self.failureException

    @pytest.mark.order(12)
    def test_Attendancemanagement_012(self):
        try:

            self.login.Employee_Logout()
            self.logger.info("Validating Test case 12")
            # Base.setUpClass()
            self.driver.get(self.baseURL)
            self.logger.info("Supervisor ULOP Dashboard Verify")
            self.login.Employee_Login(input[0], input[1])
            self.login.Employee_LoginSuccess()
            self.assertTrue(self.supervisor.Supervisor_UlopDashboard(input[2], "ULOP"))
            Commonfunctions.screenshot(self.driver, 'ulopdashboard.png')
        except:
            raise self.failureException
        finally:
            self.db.dbconnection_ChangeShiftoffRequest(input[2])

    @pytest.mark.order(13)
    def test_Attendancemanagement_013(self):
        try:
            self.login.Employee_Logout()
            self.logger.info("Validating Test case 13")
            self.logger.info("Supervisor Extension work plan Verify")
            self.driver.get(self.baseURL)
            self.login.Employee_Login(input[0], input[1])
            self.login.Employee_LoginSuccess()
            self.supervisor.Supervisor_ExtensionWorkPlan(input[2], "CompensatoryHours")
            Commonfunctions.screenshot(self.driver, 'SupervisorExtensionworkplan.png')
        except:
            raise self.failureException


    @pytest.mark.order(14)
    def test_Attendancemanagement_014(self):
        try:
            self.logger.info("Supervisor Approve Extension work plan Request Verify")
            self.supervisor.Supervisor_Extensionworkplanapprove(input[0])
            Commonfunctions.screenshot(self.driver, 'WorkPlanApprove.png')
        except:
            raise self.failureException
        finally:
            self.db.dbconnection_Extensionworkplan(input[0])

    @pytest.mark.order(15)
    def test_Attendancemanagement_015(self):
        try:
            # self.login.Employee_Logout()
            self.logger.info("Validating Test case 15")
            self.logger.info("Supervisor Extension Entry Verify")
            # self.driver.get(self.baseURL)
            # self.login.Employee_Login("davv2e07518", "Temp@123")
            # self.login.Employee_LoginSuccess()
            self.supervisor.Supervisor_ExtensionEntry(input[0], "CompensatoryHours")
            Commonfunctions.screenshot(self.driver, 'SupervisorExtensionEntry.png')
        except:
            raise self.failureException

    @pytest.mark.order(16)
    def test_Attendancemanagement_016(self):
        try:
            self.logger.info("Supervisor Approve Extension work plan Request Verify")
            self.supervisor.Supervisor_ReviewandAnalyze(input[0])
            Commonfunctions.screenshot(self.driver, 'ReviewandAnalyze.png')
        except:
            raise self.failureException
        finally:
            self.db.dbconnection_Extensionentry(input[0],input[1])

    @pytest.mark.order(17)
    def test_Attendancemanagement_017(self):
        try:

            self.login.Employee_Logout()
            self.logger.info("Validating Test case 19")
            self.driver.get(self.baseURL)
            self.logger.info("Supervisor Attendance Freezing Date Verify")
            self.login.Employee_Login(input[0], input[1])
            self.login.Employee_LoginSuccess()
            self.supervisor.Supervisor_AttendanceFreezingDate()
            Commonfunctions.screenshot(self.driver, 'SupervisorAttendanceFreezingDate.png')
        except:
            raise self.failureException

    @pytest.mark.order(18)
    def test_Attendancemanagement_018(self):
        try:
            self.login.Employee_Logout()
            self.logger.info("Validating Test case 11")
            self.driver.get(self.baseURL)
            self.logger.info("Employee Attendance Freezing Date Verify")
            self.login.Employee_Login(input[0], input[1])
            self.login.Employee_LoginSuccess()
            self.login.Employee_Viewattendancereport()
            self.login.Employee_attendanceFreezeverify()
            Commonfunctions.screenshot(self.driver, 'Attendance Freezing Date.png')
        except:
            raise self.failureException
        finally:
            self.db.dbconnection_FreezingDate()

    @pytest.mark.order(19)
    def test_Attendancemanagement_019(self):
        try:

            self.login.Employee_Logout()
            self.logger.info("Validating Test case 19")
            self.driver.get(self.baseURL)
            self.logger.info("Supervisor National Holiday Entry Verify")
            self.login.Employee_Login(input[0], input[1])
            self.login.Employee_LoginSuccess()
            self.supervisor.Supervisor_NHEntry()
            Commonfunctions.screenshot(self.driver, 'SupervisorNHEntry.png')
        except:
            raise self.failureException

    @pytest.mark.order(20)
    def test_Attendancemanagement_020(self):
        try:
            self.login.Employee_Logout()
            self.logger.info("Validating Test case 20")
            self.driver.get(self.baseURL)
            self.logger.info("Employee NH Attendance Verify")
            self.db.dbconnection_attendancescript()
            self.login.Employee_Login(input[0], input[1])
            self.login.Employee_LoginSuccess()
            self.login.Employee_Viewattendancereport()
            self.login.Employee_attendancereport('NH')
            Commonfunctions.screenshot(self.driver, 'NHattendance.png')
        except:
            raise self.failureException
        finally:
            self.db.dbconnection_NationalHoliday(input[2])

    @pytest.mark.order(21)
    def test_Attendancemanagement_021(self):
        try:

            # self.login.Employee_Logout()
            # self.logger.info("Validating Test case 14")
            # self.driver.get(self.baseURL)
            self.logger.info("Supervisor Map EmployeeShiftTime Verify")
            # self.login.Employee_Login("POOV2E08714", "Temp@123")
            # self.login.Employee_LoginSuccess()
            self.supervisor.Supervisor_MapEmployeeShiftTime(input[0])
            Commonfunctions.screenshot(self.driver, 'SupervisorMapEmployeeShiftTime.png')
        except:
            raise self.failureException

    @pytest.mark.order(22)
    def test_Attendancemanagement_022(self):
        try:
            self.login.Employee_Logout()
            self.logger.info("Validating Test case 22")
            self.driver.get(self.baseURL)
            self.logger.info("Employee Shift Time Verify")
            self.login.Employee_Login(input[0], input[1])
            self.login.Employee_LoginSuccess()
            self.assertTrue(self.login.Employee_MapEmployeeShiftTime(input[2]))
            Commonfunctions.screenshot(self.driver, 'EmployeeShiftTime.png')
        except:
            raise self.failureException


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
            print("excel name",self.excelname,self.sheetname)
            j = ExcelReadandWrite.excelsearch(self.excelname, self.sheetname2, search)
            ExcelReadandWrite.writeData(self.excelname, self.sheetname2, j, 8, "FAIL")
            allure.attach(self.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
            global failtc
            failtc = failtc + 1
        else:
            data = self._testMethodName
            dd = data.split('_')
            dd.reverse()
            validate = '{}{}{}'.format(dd[1], '_', dd[0])
            search = validate
            j = ExcelReadandWrite.excelsearch(self.excelname, self.sheetname2, search)
            ExcelReadandWrite.writeData(self.excelname, self.sheetname2, j, 8, "PASS")
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
        message["Subject"] = "HRportal_AMS Automation Test"

        ####################  Testing Configuration ##############################
        host = "HRPortal_AMS"
        projectname = "\nHRPortal_AMS Automation Report"
        operatingsystem = "Windows 10"
        browser = "Google Chrome"
        regression = "HRPortal_AMS Sanity Report"

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

                                                                                                <p>Hi Team,<br><br>HRPortal_AMS Automation Sanity Test Case Executed and Here is the summary report.</p></br>
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
