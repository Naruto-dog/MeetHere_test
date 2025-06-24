"""执行用例"""
import unittest
from os import mkdir
from HTMLTestRunner_cn import HTMLTestRunner
from src.scripts import case

# '''

reports_path = 'E:/testpro/MeetHere/python-autoTest/src/reports/MeetHere_report.html'

loader = unittest.TestLoader()
suite = loader.loadTestsFromNames(
    ['LoginTest'], case)  #'SignUpTest',

with open (reports_path,'wb') as f:

    runner = HTMLTestRunner(stream=f, title='初次测试', description='测试')
    runner.run(suite)
# '''
'''
loader = unittest.TestLoader()
suite = loader.loadTestsFromTestCase(SignUpTest)
runner = unittest.TextTestRunner()
runner.run(suite)
'''