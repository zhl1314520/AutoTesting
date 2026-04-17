import sys
import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

"""

模拟键盘的操作
"""


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_key_down(driver):
    driver.get('https://selenium.dev/selenium/web/single_text_input.html')

    ActionChains(driver)\
        .key_down(Keys.SHIFT)\
        .send_keys("abc")\
        .perform()  # 模拟按住 Shift 键的同时输入 "abc"

    assert driver.find_element(By.ID, "textInput").get_attribute('value') == "ABC"


def test_key_up(driver):
    driver.get('https://selenium.dev/selenium/web/single_text_input.html')

    ActionChains(driver)\
        .key_down(Keys.SHIFT)\
        .send_keys("a")\
        .key_up(Keys.SHIFT)\
        .send_keys("b")\
        .perform()

    assert driver.find_element(By.ID, "textInput").get_attribute('value') == "Ab"


def test_send_keys_to_active_element(driver):
    driver.get('https://selenium.dev/selenium/web/single_text_input.html')

    ActionChains(driver)\
        .send_keys("abc")\
        .perform()

    assert driver.find_element(By.ID, "textInput").get_attribute('value') == "abc"


# 点击页面上的任意位置，使得输入框失去焦点，然后再使用 send_keys_to_element() 方法将 "abc" 输入到输入框中
def test_send_keys_to_designated_element(driver):
    driver.get('https://selenium.dev/selenium/web/single_text_input.html')
    driver.find_element(By.TAG_NAME, "body").click()

    text_input = driver.find_element(By.ID, "textInput")
    ActionChains(driver)\
        .send_keys_to_element(text_input, "abc")\
        .perform()

    assert driver.find_element(By.ID, "textInput").get_attribute('value') == "abc"

# =====================
# 全局慢速模式开关
# =====================
SLOW_MODE = True
def pause(seconds=1):
    if SLOW_MODE:
        time.sleep(seconds)

def test_copy_and_paste(driver):
    driver.get('https://selenium.dev/selenium/web/single_text_input.html')
    pause(3)
    cmd_ctrl = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL   # 兼容 Mac 和 Windows/Linux 系统

    """
    模拟以下操作：
    1. 在输入框中输入 "Selenium!"
    2. 按下左箭头键，将光标移动到 "!" 前面
    3. 按住 Shift 键的同时按下上箭头键，选中 "Selenium"
    4. 松开 Shift 键
    5. 按住 Command/Ctrl 键的同时按下 "x" -> vv: 粘贴两次
    6. 松开 Command/Ctrl 键
    
    最终输入框中的内容应该是 "SeleniumSelenium!”
    """
    ActionChains(driver)\
        .send_keys("Selenium!")\
        .send_keys(Keys.ARROW_LEFT).pause(1)\
        .key_down(Keys.SHIFT).pause(1)\
        .send_keys(Keys.ARROW_UP).pause(1)\
        .key_up(Keys.SHIFT).pause(1)\
        .key_down(cmd_ctrl).pause(1)\
        .send_keys("xvv").pause(1)\
        .key_up(cmd_ctrl).pause(1)\
        .perform()
    pause(3)
    assert driver.find_element(By.ID, "textInput").get_attribute('value') == "SeleniumSelenium!"
