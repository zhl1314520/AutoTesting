import pytest
import time
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

"""

这段代码讲的是 Selenium 三种等待机制（不等待 / sleep / 隐式等待 / 显式等待）

Web 页面是“动态的”，元素不会立刻出现，所以必须“等”
"""

# 证明：不等待一定会出问题
def test_fails(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click() # 点击 adder → 延迟生成新元素（box0）

    with pytest.raises(NoSuchElementException):
        driver.find_element(By.ID, 'box0')


def test_sleep(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    time.sleep(2)
    added = driver.find_element(By.ID, "box0")

    assert added.get_dom_attribute('class') == "redbox"

# 隐式等待
def test_implicit(driver):
    driver.implicitly_wait(2) # 查找元素时最多等 2 秒
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    added = driver.find_element(By.ID, "box0")

    assert added.get_dom_attribute('class') == "redbox"

# 显式等待
def test_explicit(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    revealed = driver.find_element(By.ID, "revealed")
    driver.find_element(By.ID, "reveal").click()    # 点击 reveal → 输入框变成可见

    """
    流程：
        找到元素（但还不可见）
        点击按钮
        等待：元素变成可见
        输入内容
    """
    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda _ : revealed.is_displayed())

    revealed.send_keys("Displayed")
    assert revealed.get_property("value") == "Displayed"

# 显式等待 + 忽略异常
def test_explicit_options(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    revealed = driver.find_element(By.ID, "revealed")
    driver.find_element(By.ID, "reveal").click()

    errors = [NoSuchElementException, ElementNotInteractableException]

    # poll_frequency: 每隔 0.2 秒检查一次条件，直到满足条件或超时
    wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
    wait.until(lambda _ : revealed.send_keys("Displayed") or True)

    assert revealed.get_property("value") == "Displayed"
