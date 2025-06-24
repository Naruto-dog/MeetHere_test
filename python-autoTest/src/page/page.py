from selenium.common import NoSuchElementException, TimeoutException

from src.base.driver import GetDriver
from src import page
from src.base.base import Base
import time


class Page(Base):
    """配置页面操作"""
    def page_signup_link(self):
        """进入注册页"""
        self.base_click_element(page.page_signup_link)

    def page_login_link(self):
        """进入登录页"""
        self.base_click_element(page.page_login_link)

    def page_logout_link(self):
        """注销登录"""
        self.base_click_element(page.page_logout_link)

    def page_username_input(self, username):
        """输入昵称"""
        self.base_insert_element(page.page_username_input, username)

    def page_email_input(self, email):
        """输入邮箱"""
        self.base_insert_element(page.page_email_input, email)

    def page_phone_input(self, phone):
        """输入手机号"""
        self.base_insert_element(page.page_phone_input, phone)

    def page_userid_input(self, userid):
        """输入用户名"""
        self.base_insert_element(page.page_userID_input, userid)

    def page_password_input(self, password):
        """输入密码"""
        self.base_insert_element(page.page_password_input, password)

    def page_autoalert_email(self):
        """判断邮箱错误是否提示"""
        try:
            self.base_find_element(page.page_alert_email)
            return False
        except TimeoutException:
            return True

    def page_emailer_get(self):
        """获取邮箱提示信息"""
        return self.base_find_element(page.page_email_er)

    def page_autoalert_phone(self):
        """判断手机号错误是否提示"""
        try:
            self.base_find_element(page.page_alert_phone)
            return False
        except TimeoutException:
            return True

    def page_phoneer_get(self):
        """获取手机号提示信息"""
        return self.base_find_element(page.page_phone_er)

    def page_autoalert_id(self):
        """判断用户名错误是否提示"""
        try:
            self.base_find_element(page.page_alert_id)
            return False
        except TimeoutException:
            return True
    def page_userider_get(self):
        """获取用户名提示信息"""
        return self.base_find_element(page.page_userid_er)

    def page_signup_able(self):
        """判断注册按钮是否可用"""
        try:
            self.base_find_element(page.page_signup_able)
            return False
        except Exception as e:
            return True

    def page_submit(self):
        """发送登录/注册请求"""
        self.base_click_element(page.page_submit_button)

    def page_signup(self, username, email, phone, userid, password):
        """注册组合"""
        time.sleep(.2)
        self.page_username_input(username)
        time.sleep(.2)
        self.page_email_input(email)
        time.sleep(.2)
        self.page_phone_input(phone)
        time.sleep(.2)
        self.page_userid_input(userid)
        time.sleep(.2)
        self.page_password_input(password)
        time.sleep(.2)


    def page_login(self, userid, password):
        """登录组合"""
        time.sleep(.2)
        self.page_userid_input(userid)
        time.sleep(.2)
        self.page_password_input(password)
        time.sleep(.2)


    def page_logout_log(self):
        """注销并跳转登录"""
        time.sleep(.2)
        self.page_logout_link()
        time.sleep(.2)
        self.page_login_link()

    def page_alter_info(self):
        """判断登录错误提示框是否出现"""
        try:
            self.base_find_element(page.page_alert_info)
            return False
        except TimeoutException:
            return True

    def page_login_er(self):
        """返回登录提示信息"""
        return self.base_find_element(page.page_login_er)


if __name__ == '__main__':
    pass




