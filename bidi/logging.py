import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

"""

Selenium 里 BiDi（双向协议）日志监听
    浏览器一旦发生日志 / JS报错 → Selenium 能“实时推送”给你（而不是你去主动查）
"""

# =====================
# 全局 driver fixture
# =====================
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.driver_type("bidi")
def test_add_console_log_handler(driver):   # 注册一个监听器：只要浏览器有 console.log，就把日志加到 log_entries
    driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')
    log_entries = []

    driver.script.add_console_message_handler(log_entries.append)

    driver.find_element(By.ID, "consoleLog").click()
    WebDriverWait(driver, 5).until(lambda _: log_entries)
    assert log_entries[0].text == "Hello, world!"


@pytest.mark.driver_type("bidi")
def test_remove_console_log_handler(driver):    # 注册监听 → 再立刻取消
    driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')
    log_entries = []

    id = driver.script.add_console_message_handler(log_entries.append)
    driver.script.remove_console_message_handler(id)

    driver.find_element(By.ID, "consoleLog").click()
    assert len(log_entries) == 0


@pytest.mark.driver_type("bidi")
def test_add_js_exception_handler(driver):# 监听 JS 报错（异常）
    driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')
    log_entries = []

    driver.script.add_javascript_error_handler(log_entries.append)

    driver.find_element(By.ID, "jsException").click()
    WebDriverWait(driver, 5).until(lambda _: log_entries)
    assert log_entries[0].text == "Error: Not working"


@pytest.mark.driver_type("bidi")
def test_remove_js_exception_handler(driver):   # 注册监听 → 再立刻取消
    driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')
    log_entries = []

    id = driver.script.add_javascript_error_handler(log_entries.append)
    driver.script.remove_javascript_error_handler(id)

    driver.find_element(By.ID, "consoleLog").click()
    assert len(log_entries) == 0
