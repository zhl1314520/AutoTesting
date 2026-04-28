from selenium.webdriver.common.by import By
from auto_with_POM.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):  # 继承 BasePage 中的 __init__() 方法

    url = "http://localhost:5173/login"

    email_input = (By.ID, "email")
    password_input = (By.ID, "password")
    submit_btn = (By.CLASS_NAME, "submit-button")

    def open(self):
        self.driver.get(self.url)

    def login(self, email, password):
        self.input(self.email_input, email)
        self.input(self.password_input, password)
        self.click(self.submit_btn)

    def is_login_success(self):
        # 页面跳转延迟，添加显示等待
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains("dashboard"))
        return "dashboard" in self.driver.current_url