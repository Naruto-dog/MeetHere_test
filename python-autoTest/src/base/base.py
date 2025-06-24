from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait



class Base:
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, el_address, timeout=3, frq=0.5):
        """查找元素"""
        return (WebDriverWait(self.driver, timeout=timeout, poll_frequency=frq).
                until(lambda driver: driver.find_element(by=el_address[0], value=el_address[1])))

    def base_click_element(self, el_address):
        """点击元素"""
        self.base_find_element(el_address).click()

    def base_insert_element(self, el_address, text):
        """输入信息"""
        el = self.base_find_element(el_address)
        el.clear()
        el.send_keys(text)

    def base_alert_get(self):
        """获取弹窗"""
        try:
            alert = self.driver.switch_to.alert
            return alert
        except Exception as e:
            return None

    def base_img_get(self, userid):
        """失败截图"""
        self.driver.save_screenshot(f'E:/testpro/MeetHere/python-autoTest/src/imgs/{userid}.png')

