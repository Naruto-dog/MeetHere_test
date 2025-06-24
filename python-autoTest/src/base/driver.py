from selenium import webdriver
from selenium.webdriver.edge.service import Service
from src import page


class GetDriver:
    """单例模式获取driver"""
    driver = None

    @classmethod
    def get_driver(cls):
        if not cls.driver:
            cls.service = Service(r'D:\webdriver\edge\msedgedriver.exe')
            cls.driver = webdriver.Edge(service=cls.service)
            cls.driver.get(page.page_url)
            cls.driver.maximize_window()
        return cls.driver

    @classmethod
    def driver_quit(cls):
        cls.driver.quit()
        cls.driver = None


if __name__ == '__main__':
    import time

    driver = GetDriver()
    driver.get_driver()
    time.sleep(3)
    driver.driver_quit()
