from datetime import datetime

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

"""

定位元素
"""
# =====================
# 全局慢速模式开关
# =====================
SLOW_MODE = True


def pause(seconds=1):
    if SLOW_MODE:
        time.sleep(seconds)


# =====================
# 全局 driver fixture
# =====================
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# =====================
# 公共 URL
# =====================
URL = "file:///D:/Desktop/4.html"


# =====================
# 显式等待封装
# =====================
def wait_element(driver, by, value, timeout=5):
    element = WebDriverWait(driver, timeout).until(
        expected_conditions.presence_of_element_located((by, value))
    )
    pause()
    return element


def wait_elements(driver, by, value, timeout=5):
    elements = WebDriverWait(driver, timeout).until(
        expected_conditions.presence_of_all_elements_located((by, value))
    )
    pause()
    return elements


# =====================
# 测试用例
# =====================

def test_class_name(driver):
    driver.get(URL)
    pause()

    elements = wait_elements(driver, By.CLASS_NAME, "information")

    assert len(elements) > 0
    assert elements[0].tag_name == "input"


def test_css_selector(driver):
    driver.get(URL)
    pause()

    element = wait_element(driver, By.CSS_SELECTOR, "#fname")

    assert element is not None
    assert element.get_attribute("value") == "Jane"


def test_id(driver):
    driver.get(URL)
    pause()

    element = wait_element(driver, By.ID, "lname")

    assert element is not None
    assert element.get_attribute("value") == "Doe"


def test_name(driver):
    driver.get(URL)
    pause()

    element = wait_element(driver, By.NAME, "newsletter")

    assert element is not None
    assert element.tag_name == "input"


def test_link_text(driver):
    driver.get(URL)
    pause()

    element = wait_element(driver, By.LINK_TEXT, "Selenium Official Page")

    assert element is not None
    assert element.get_attribute("href") == URL


def test_partial_link_text(driver):
    driver.get(URL)
    pause()

    element = wait_element(driver, By.PARTIAL_LINK_TEXT, "Official Page")

    assert element is not None
    assert element.get_attribute("href") == URL


def test_tag_name(driver):
    driver.get(URL)
    pause()

    elements = wait_elements(driver, By.TAG_NAME, "a")

    assert len(elements) > 0
    assert elements[0].get_attribute("href") == URL


def test_xpath(driver):
    driver.get(URL)
    pause()

    element = wait_element(driver, By.XPATH, "//input[@value='f']")

    assert element is not None
    assert element.get_attribute("type") == "radio"


def test_input_update(driver):
    driver.get(URL)
    pause()

    element = wait_element(driver, By.ID, "fname")

    # 清空
    element.clear()
    pause()

    # 输入
    element.send_keys("Eric")
    pause(2)

    assert element.get_attribute("value") == "Eric"

def test_click_button(driver):
    # 设置开始点击的时间
    start_time = datetime(2026, 4, 19, 13, 59, 0)
    # 设置结束点击的时间
    end_time = datetime(2026, 4, 19, 14, 0, 0)
    # driver.get("file:///D:/Desktop/1.html")
    driver.get("http://localhost:5173/login")

    while datetime.now() < start_time:
        try:
            # 每次点击前重新查找元素（因为页面刷新后元素会失效）
            button = wait_element(driver, By.CLASS_NAME, "logo-link")
            button.click()
            pause(1)
        except Exception as e:
            print(f"点击失败：{e}")
            pause(1)
            # 页面刷新后重新加载
            driver.get("http://localhost:5173/login")
        if datetime.now() > end_time:
            break