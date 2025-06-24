import time
import unittest
from src.base.driver import GetDriver
from src.page.page import Page
from parameterized import parameterized
from src.tool.json_load import signup_data_get
from src.tool.json_load import login_data_get
from src import page
from src.log.logger import LogGet


log = LogGet().log_get()


class SignUpTest(unittest.TestCase):
    """注册测试"""
    driver_obj = GetDriver()

    @classmethod
    def setUpClass(cls):
        log.info('======启动浏览器')
        cls.driver = cls.driver_obj.get_driver()
        cls.index = Page(cls.driver)

    @classmethod
    def tearDownClass(cls):
        log.info('======关闭浏览器')
        cls.driver_obj.driver_quit()

    @parameterized.expand(signup_data_get())
    def test_signup(self, username, email, phone, userid, password, expect):
        log.info('======点击注册')
        self.index.page_signup_link()
        log.info('======输入信息')
        self.index.page_signup(username, email, phone, userid, password)
        log.info('======判断注册按钮是否有效')
        if  self.index.page_signup_able():  # 判断注册按钮是否有效
            self.index.page_submit()
            if username == '':
                input_el = self.index.base_find_element(page.page_username_input)
                self.assertIn(expect, input_el.get_attribute("validationMessage"))
            elif userid == '':
                input_el = self.index.base_find_element(page.page_userID_input)
                self.assertIn(expect, input_el.get_attribute("validationMessage"))
            elif password == '':
                input_el = self.index.base_find_element(page.page_password_input)
                self.assertIn(expect, input_el.get_attribute("validationMessage"))
            else:
                try:
                    log.info('======获取弹窗')
                    alert = self.index.base_alert_get()
                    log.info('======弹窗内容：', alert.text)
                    self.assertEqual(alert.text, expect)
                    alert.accept()
                except AttributeError as e :
                    log.info('======获取弹窗失败，信息：', e)
                    log.info(f'======按照是否跳转到登录页来断言，expect为：{expect}')
                    self.assertIn('/login', self.driver.current_url)
                    self.index.page_signup_link()

        elif self.index.page_autoalert_email():
            message = self.index.page_emailer_get()
            self.assertEqual(expect.strip(), message.text.strip())

        elif self.index.page_autoalert_phone():
            message = self.index.page_phoneer_get()
            self.assertEqual(expect.strip(), message.text.strip())

        elif self.index.page_autoalert_id():
            message = self.index.page_userider_get()
            self.assertEqual(expect.strip(), message.text.strip())
        else:
            try:
                print('======')
            except Exception as e :
                print('======', e)

class LoginTest(unittest.TestCase):
    """登录测试"""
    driver_obj = GetDriver()

    @classmethod
    def setUpClass(cls):
        log.info('======启动浏览器')
        cls.driver = cls.driver_obj.get_driver()
        cls.index = Page(cls.driver)

    @classmethod
    def tearDownClass(cls):
        log.info('======关闭浏览器')
        cls.driver_obj.driver_quit()

    @parameterized.expand(login_data_get())
    def test_login(self, userid, password, expect):
        log.info('======点击跳转登录按钮')
        self.index.page_login_link()
        self.index.page_login(userid, password)
        if userid and password:
            self.index.page_submit()
            try:
                log.info('======获取弹窗')
                alert = self.index.base_alert_get()
                log.info('======弹窗内容：{}'.format(alert.text))
                self.assertIn(alert.text, expect)
                alert.accept()
                self.index.page_logout_log()
            except AttributeError:
                log.info('======无弹窗')
                if self.index.page_alter_info():
                    message = self.index.page_login_er()
                    self.assertIn(expect.strip(), message.text.strip())
            except Exception as e:
                log.info('======获取弹窗失败，信息：')
                log.info(f'======按照是否跳转到登录后首页页来断言，expect为：{expect}')
                self.assertIn('/index', self.driver.current_url)
                self.index.page_logout_log()
        elif userid == '':
            self.index.page_submit()
            input_el = self.index.base_find_element(page.page_userID_input)
            self.assertIn(expect, input_el.get_attribute("validationMessage"))
        elif password == '':
            self.index.page_submit()
            input_el = self.index.base_find_element(page.page_password_input)
            self.assertIn(expect, input_el.get_attribute("validationMessage"))
