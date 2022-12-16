@ECHO OFF
set PythonDIR=D:\PycharmProjects\HR_Portal\Python39
set PYTHONPATH=%PythonDIR%\Lib\site-packages
set location=D:\PycharmProjects\HR_Portal
pushd %location%
python -W ignore -m pytest TestCases\test_Leavemanagement.py --alluredir D:\PycharmProjects\HR_Portal\Reports
set AllurePath = D:\PycharmProjects\HR_Portal\allure-2.19.0\bin
set location=%AllurePath%
pushd %location%
allure serve D:\PycharmProjects\HR_Portal\Reports
PAUSE