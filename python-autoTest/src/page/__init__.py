from selenium.webdriver.common.by import By
"""配置页面元素信息"""

'''首页元素信息'''
page_url = 'http://localhost:8888/index'
page_login_link = By.PARTIAL_LINK_TEXT, '登录'
page_signup_link = By.PARTIAL_LINK_TEXT, '注册'
page_logout_link = By.PARTIAL_LINK_TEXT, '注销'

'''注册页和登录页元素信息'''
page_username_input = By.ID, 'userName'
page_email_input = By.ID, 'email'
page_phone_input = By.ID, 'phone'
page_userID_input = By.ID, 'userID'
page_password_input = By.ID, 'password'
page_submit_button = By.ID, 'submit'
page_alert_email = By.XPATH, '//main[@class="container"]//div[@id="alertEmail" and @hidden]'
page_email_er = By.XPATH, '/html/body/main/form/div[4]'
page_alert_phone = By.XPATH, '//main[@class="container"]//div[@id="alertPhone" and @hidden]'
page_phone_er = By.XPATH, '/html/body/main/form/div[6]'
page_alert_id = By.XPATH, '//main[@class="container"]//div[@id="alertId" and @hidden]'
page_userid_er = By.XPATH, '/html/body/main/form/div[8]'
page_alert_info = By.XPATH, '//main[@class="container col-4"]//div[@hidden]'
page_login_er = By.XPATH, '/html/body/main/form/div[4]'

page_signup_able = By.CSS_SELECTOR,'[disabled="disabled"]'




