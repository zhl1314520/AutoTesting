import base64
from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.common.devtools.v145.network import Headers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
"""

Selenium 直接操控浏览器底层（网络 / 性能 / cookie）
"""

# =====================
# 全局 driver fixture
# =====================
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
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
这个用例只适用于：HTTP认证（Basic / Token），对于普通表单登录（Form-based Authentication）无效
"""
@pytest.mark.trio
async def test_basic_auth(driver):  # 通过修改 HTTP 请求头，绕过浏览器登录弹窗，实现自动登录
    async with driver.bidi_connection() as connection:  # 打开一个“浏览器底层控制通道”（类似 DevTools）
        await connection.session.execute(connection.devtools.network.enable())  # 启用“网络拦截/修改能力”

        credentials = base64.b64encode("admin:admin".encode()).decode() # 将用户名和密码转为 Base64 编码
        auth = {'authorization': 'Basic ' + credentials}    # 构造 HTTP 请求头

        # 给浏览器“所有后续请求”加上这个 header
        await connection.session.execute(connection.devtools.network.set_extra_http_headers(Headers(auth)))

        driver.get('https://the-internet.herokuapp.com/basic_auth')

    pause(2)
    success = driver.find_element(by=By.TAG_NAME, value='p')
    pause(3)
    assert success.text == 'Congratulations! You must have the proper credentials.'


@pytest.mark.trio
async def test_performance(driver): # 获取浏览器内部性能数据
    driver.get('https://www.selenium.dev/selenium/web/frameset.html')

    async with driver.bidi_connection() as connection:
        await connection.session.execute(connection.devtools.performance.enable())
        metric_list = await connection.session.execute(connection.devtools.performance.get_metrics())

    metrics = {metric.name: metric.value for metric in metric_list}

    assert metrics["DevToolsCommandDuration"] > 0
    assert metrics["Frames"] == 12

@pytest.mark.trio
async def test_set_cookie(driver):  # 通过 CDP 设置 cookie，验证是否生效
    async with driver.bidi_connection() as connection:
        execution = connection.devtools.network.set_cookie(
            # 在浏览器里“种一个 cookie”
            name="cheese",
            value="gouda",
            domain="www.selenium.dev",
            secure=True
        )
        await connection.session.execute(execution) # 真正把 cookie 写进浏览器

    driver.get("https://www.selenium.dev")  # 打开页面，此时 cookie 已经存在
    cheese = driver.get_cookie("cheese")

    assert cheese["value"] == "gouda"


"""
拓展：
    单个账号自动登录认证（Form-based Authentication）：模拟账号密码登录
"""
def test_login(driver):
    driver.get("http://localhost:5173/login")

    wait = WebDriverWait(driver, 10)

    # 输入用户名、密码
    email = wait.until(expected_conditions.presence_of_element_located((By.ID, "email")))
    email.clear()
    email.send_keys("17201665342@163.com")

    password = driver.find_element(By.ID, "password")
    password.clear()
    password.send_keys("123456")

    # 点击登录
    driver.find_element(By.CLASS_NAME, "submit-button").click()
    # 断言登录成功（URL变化）
    wait.until(lambda d: "dashboard" in d.current_url)

    assert "dashboard" in driver.current_url
"""
批量登录
"""
@pytest.mark.parametrize(
    "email,password", [
    ("17201665342@163.com", "123456"),
    ("taylor@163.com", "12345678"),
    ("eric@163.com", "1234567890"),
])
def test_login(driver, email, password):
    driver.get("http://localhost:5173/login")

    wait = WebDriverWait(driver, 10)

    email_input = wait.until(
        expected_conditions.presence_of_element_located((By.ID, "email"))
    )
    password_input = driver.find_element(By.ID, "password")

    email_input.clear()
    email_input.send_keys(email)

    password_input.clear()
    password_input.send_keys(password)

    # 点击登录
    driver.find_element(By.CLASS_NAME, "submit-button").click()
    # 断言登录成功（URL变化）
    wait.until(lambda d: "dashboard" in d.current_url)

    assert "dashboard" in driver.current_url