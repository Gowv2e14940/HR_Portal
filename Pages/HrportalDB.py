import datetime
from datetime import date



import pyodbc
class HrportalDB():
    # conn = pyodbc.connect('Driver={SQL Server};'
    #                       'Server=172.17.1.13;'
    #                       'Database=HRPortalTest;'
    #                       'UID=sa;'
    #                       'PWD=Temp!123;'
    #                       'Trusted_Connection=yes;'
    #                       )

    def dbconnection(self,empid,attendancetype,leavetype):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=172.17.1.13;'
                              'Database=HRPortalTest;'
                              'UID=sa;'
                              'PWD=Temp!123;'
                              'Trusted_Connection=no;'
                              )
        self.cursor = conn.cursor()
        # if attendancetype == "Permission":
        #     print("attendance type",)
        #     self.cursor.execute("delete from PermissionRequest where empid='" + empid + "' and Reason = 'Test Permission'")
        #     conn.commit()

        # elif attendancetype != "Permission":
        # self.cursor.execute("select autoid from leaverequest where empid='"+empid+"' and reason='AutomationTesting'")
        # leaverecord = self.cursor.fetchone()
        # leaverequestid = leaverecord[0]
        # print("leave records are", leaverecord)
        # print("leave is", leaverequestid)


        if leavetype == str(1):
            self.cursor.execute(
                "select autoid from leaverequest where empid='" + empid + "' and reason='AutomationTesting'")
            leaverecord = self.cursor.fetchone()
            leaverequestid = leaverecord[0]
            print("leave records are", leaverecord)
            print("leave is", leaverequestid)
            self.cursor.execute(
                "update LeaveRequestDetails set IsDeleted=1 where LeaveRequestID='" + str(leaverequestid) + "'")
            self.cursor.execute(
                "update TOP (1) attendance set AttendanceType='LOP' where empid='" + empid + "' and comments='TestApprove' and AttendanceType='" + attendancetype + "'")
            self.cursor.execute(
                "update leavebalance set leavetaken = 0,balance = 10 where empid='" + empid + "' and leavetype =" + leavetype + " ")
            self.cursor.execute("delete from leaverequest where empid='" + empid + "' and autoid='" + str(leaverequestid) + "'")
            conn.commit()
        if leavetype == str(2):
            self.cursor.execute(
                "select autoid from leaverequest where empid='" + empid + "' and reason='AutomationTesting'")
            leaverecord = self.cursor.fetchone()
            leaverequestid = leaverecord[0]
            print("leave records are", leaverecord)
            print("leave is", leaverequestid)
            self.cursor.execute(
                "update LeaveRequestDetails set IsDeleted=1 where LeaveRequestID='" + str(leaverequestid) + "'")
            self.cursor.execute(
                "update TOP (1) attendance set AttendanceType='LOP' where empid='" + empid + "' and comments='TestApprove' and AttendanceType='" + attendancetype + "'")
            self.cursor.execute(
                "update leavebalance set leavetaken = 0,balance = 7 where empid='" + empid + "' and leavetype =" + leavetype + " ")
            self.cursor.execute(
                "delete from leaverequest where empid='" + empid + "' and autoid='" + str(leaverequestid) + "'")
            conn.commit()
        if leavetype == str(3):
            self.cursor.execute(
                "select autoid from leaverequest where empid='" + empid + "' and reason='AutomationTesting'")
            leaverecord = self.cursor.fetchone()
            leaverequestid = leaverecord[0]
            print("leave records are", leaverecord)
            print("leave is", leaverequestid)
            self.cursor.execute(
                "update LeaveRequestDetails set IsDeleted=1 where LeaveRequestID='" + str(leaverequestid) + "'")
            self.cursor.execute(
                "update TOP (1) attendance set AttendanceType='LOP' where empid='" + empid + "' and comments='TestApprove' and AttendanceType='" + attendancetype + "'")
            self.cursor.execute(
                "update leavebalance set leavetaken = 0,balance = 10 where empid='" + empid + "' and leavetype =" + leavetype + " ")
            self.cursor.execute(
                "delete from leaverequest where empid='" + empid + "' and autoid='" + str(leaverequestid) + "'")
            conn.commit()
        if leavetype == str(4):
            self.cursor.execute(
                "select autoid from leaverequest where empid='" + empid + "' and reason='AutomationTesting'")
            leaverecord = self.cursor.fetchone()
            leaverequestid = leaverecord[0]
            print("leave records are", leaverecord)
            print("leave is", leaverequestid)
            self.cursor.execute(
                "update LeaveRequestDetails set IsDeleted=1 where LeaveRequestID='" + str(leaverequestid) + "'")
            self.cursor.execute(
                "update TOP (1) attendance set AttendanceType='LOP' where empid='" + empid + "' and comments='TestApprove' and AttendanceType='" + attendancetype + "'")
            self.cursor.execute(
                "update leavebalance set leavetaken = 0,balance = 10 where empid='" + empid + "' and leavetype =" + leavetype + " ")
            self.cursor.execute(
                "delete from leaverequest where empid='" + empid + "' and autoid='" + str(leaverequestid) + "'")
            conn.commit()
        if leavetype == str(9):
            self.cursor.execute(
                "select autoid from leaverequest where empid='" + empid + "' and reason='AutomationTesting'")
            leaverecord = self.cursor.fetchone()
            leaverequestid = leaverecord[0]
            print("leave records are", leaverecord)
            print("leave is", leaverequestid)
            self.cursor.execute(
                "update LeaveRequestDetails set IsDeleted=1 where LeaveRequestID='" + str(leaverequestid) + "'")
            self.cursor.execute(
                "update TOP (1) attendance set AttendanceType='LOP' where empid='" + empid + "' and comments='TestApprove' and AttendanceType='" + attendancetype + "'")
            # self.cursor.execute(
            #     "update leavebalance set leavetaken = 0,balance = 10 where empid='" + empid + "' and leavetype =" + leavetype + " ")
            self.cursor.execute("delete from leaverequest where empid='" + empid + "' and autoid='" + str(leaverequestid) + "'")
            conn.commit()
        conn.commit()
        self.cursor.close()
        conn.close()

    def dbconnection_permission(self,empid):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=172.17.1.13;'
                              'Database=HRPortalTest;'
                              'UID=sa;'
                              'PWD=Temp!123;'
                              'Trusted_Connection=no;'
                              )
        self.cursor = conn.cursor()
        self.cursor.execute("delete from PermissionRequest where empid='" + empid + "' and Reason = 'Test Permission'")
        conn.commit()

        self.cursor.close()
        conn.close()

    def dbconnection_ChangeLOPRequest(self,empid):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=172.17.1.13;'
                              'Database=HRPortalTest;'
                              'UID=sa;'
                              'PWD=Temp!123;'
                              'Trusted_Connection=no;'
                              )
        self.cursor = conn.cursor()
        self.cursor.execute(
            "select id from ChangeLOPRequest where empid='" + empid + "' and reason='Test LOP Request'")
        loprecord = self.cursor.fetchone()
        loprequestid = loprecord[0]
        print("leave records are", loprecord)
        print("leave is", loprequestid)
        self.cursor.execute(
            "update TOP(1) attendance set AttendanceType='LOP'  where empid='" + empid + "' and AttendanceType='P'")
        self.cursor.execute(
            "delete from ChangeLOPRequestApproval where LOPRequestID='" + str(loprequestid) + "'")
        self.cursor.execute(
            "delete from ChangeLOPRequest where empid = '" + empid + "' and Reason = 'Test LOP Request' and Comments='Test LOP Approved'")
        conn.commit()

        self.cursor.close()
        conn.close()

    def dbconnection_ChangeShiftoffRequest(self,empid):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=172.17.1.13;'
                              'Database=HRPortalTest;'
                              'UID=sa;'
                              'PWD=Temp!123;'
                              'Trusted_Connection=no;'
                              )
        self.cursor = conn.cursor()
        self.cursor.execute(
            "delete from ChangeShiftOffRequest where empid='" + empid + "' and AttendanceType='SO' and RequesterComments='Test Shiftoff Approve'")
        self.cursor.execute("update Attendance set AttendanceType='LOP' where EmpID='" + empid + "' and AttendanceType='SO'")
        self.cursor.execute("update Attendance set AttendanceType='LOP' where EmpID='" + empid + "' and AttendanceType='ULOP' and Comments = 'Test ULOP Approve'")
        conn.commit()

        self.cursor.close()
        conn.close()

    def dbconnection_FreezingDate(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=172.17.1.13;'
                              'Database=HRPortalTest;'
                              'UID=sa;'
                              'PWD=Temp!123;'
                              'Trusted_Connection=no;'
                              )
        self.cursor = conn.cursor()
        self.cursor.execute("select top(1) id,CreatedDate from AttendanceFreezingDetails order by CreatedDate desc")
        record = self.cursor.fetchone()
        id = record[0]
        createddate = record[1]
        cdate = str(createddate)
        print("created date",type(str(createddate)))
        print("records are", record)
        # print("Id and createddate", id,createddate.strftime("%Y-%m-%d"))
        self.cursor.execute("select top(1) id,[CreatedDate] from tbl_PayrollDateConfigMaster order by CreatedDate desc")
        payrecord = self.cursor.fetchone()
        payid = payrecord[0]
        paycreateddate = payrecord[1]
        if createddate.strftime("%Y-%m-%d")==str(date.today()):
            print("Today",date.today())
            print("date conversion",type(createddate.strftime('%Y-%m-%d %H:%M:%S.%f')))
            # a = createddate.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            # print(str(a))

            self.cursor.execute(
                "delete from AttendanceFreezingDetails where id = '"+str(id)+"' and [CreatedDate]= '"+str(createddate.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])+"' ")


            self.cursor.execute(
                "update tbl_PayrollDateConfigMaster set DeleteMark=1 where id='"+str(payid)+"' and [CreatedDate] = '" +str(paycreateddate.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])+ "' ")
            self.cursor.execute(
                "delete from tbl_PayrollDateConfigMaster where id='" + str(payid) + "' and [CreatedDate] = '" +str(paycreateddate.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])+ "' ")

        else:
            print("")
        conn.commit()

        self.cursor.close()
        conn.close()


    def dbconnection_NationalHoliday(self,empid):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=172.17.1.13;'
                              'Database=HRPortalTest;'
                              'UID=sa;'
                              'PWD=Temp!123;'
                              'Trusted_Connection=no;'
                              )
        self.cursor = conn.cursor()
        self.cursor.execute("update tbl_NationalHolidayDeclaration set DeleteMark=1 where NHDate='" + str(date.today() - datetime.timedelta(days = 1)) + " 00:00:00.000' and LeaveReason = 'Test NH Entry'")
        self.cursor.execute("delete from tbl_NationalHolidayDeclaration where NHDate='" + str(date.today() - datetime.timedelta(days=1)) + " 00:00:00.000' and LeaveReason = 'Test NH Entry'")
        self.cursor.execute("update Attendance set AttendanceType='LOP' where EmpID='" + empid + "' and AttendanceType='NH' and Date='" + str(date.today() - datetime.timedelta(days=1)) + " 00:00:00.000'")
        conn.commit()

        self.cursor.close()
        conn.close()

    def dbconnection_attendancescript(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=172.17.1.13;'
                              'Database=HRPortalTest;'
                              'UID=sa;'
                              'PWD=Temp!123;'
                              'Trusted_Connection=no;'
                              )
        self.cursor = conn.cursor()
        self.cursor.execute("EXEC [spHRPortal_Bio_InsertAttendance] '" + str(date.today() - datetime.timedelta(days = 1)) + " 00:00:00.000' ")
        conn.commit()

        self.cursor.close()
        conn.close()

    # def dbconnection_LOPscript(self):
    #     conn = pyodbc.connect('Driver={SQL Server};'
    #                           'Server=172.17.1.13;'
    #                           'Database=HRPortalTest;'
    #                           'UID=sa;'
    #                           'PWD=Temp!123;'
    #                           'Trusted_Connection=no;'
    #                           )
    #     self.cursor = conn.cursor()
    #     self.cursor.execute()
    #     conn.commit()
    #
    #     self.cursor.close()
    #     conn.close()

    def dbconnection_Extensionworkplan(self,empid):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=172.17.1.13;'
                              'Database=HRPortalTest;'
                              'UID=sa;'
                              'PWD=Temp!123;'
                              'Trusted_Connection=no;'
                              )
        self.cursor = conn.cursor()
        self.cursor.execute(
            "delete from AttendanceExtensionWorkPlan where empid='" + empid + "' and [Date]='" + str(date.today()) + " 00:00:00.000' and ExtensionReason='Test Extension work plan'")

        conn.commit()

        self.cursor.close()
        conn.close()

    def dbconnection_Extensionentry(self,empid,uempid):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=172.17.1.13;'
                              'Database=HRPortalTest;'
                              'UID=sa;'
                              'PWD=Temp!123;'
                              'Trusted_Connection=no;'
                              )
        self.cursor = conn.cursor()
        self.cursor.execute(
            "update attendance set ExtensionReason='',ExtensionType='',ExtensionUpdatedBy='',ExtensionUpdatedDate='1900-01-01 00:00:00.000', ExtensionStatus='' where EmpID='"+empid+"' and ExtensionReason='Test CH Extension Entry'")
        self.cursor.execute(
            "delete from AttendanceExtensionApproval where extensionreason = 'Test CH Extension Entry' and ApprovedBy='"+uempid+"'")

        conn.commit()

        self.cursor.close()
        conn.close()