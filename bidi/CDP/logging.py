import pytest
from selenium.webdriver.common.bidi.console import Console
from selenium.webdriver.common.by import By
from selenium.webdriver.common.log import Log

"""

BiDi（双向协议）“异步写法”版本的日志监听
    从“回调函数（callback）模式” → 变成“async/await + 上下文管理”
"""
@pytest.mark.trio
async def test_console_log(driver):
    driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')

    async with driver.bidi_connection() as session:     # 建立 BiDi 连接，获取 session 对象
        async with Log(driver, session).add_listener(Console.ALL) as messages:
            driver.find_element(by=By.ID, value='consoleLog').click()

        assert messages["message"] == "Hello, world!"


@pytest.mark.trio
async def test_js_error(driver):
    driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')

    async with driver.bidi_connection() as session:
        async with Log(driver, session).add_js_error_listener() as messages:
            driver.find_element(by=By.ID, value='jsException').click()

        assert "Error: Not working" in messages.exception_details.exception.description
