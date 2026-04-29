import pytest
from auto_with_POM.pages.login_page import LoginPage
from selenium import webdriver
import time


# ======
# 全局 fixture
# ======
@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = "eager"
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()    # 浏览器窗口最大化
    yield driver
    driver.quit()


# =====================
# 全局慢速模式开关
# =====================
SLOW_MODE = True


def pause(seconds=1):
    if SLOW_MODE:
        time.sleep(seconds)

"""
封装的登录
"""
@pytest.fixture(scope="session")
def login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("17201665342@163.com", "123456")
    return page