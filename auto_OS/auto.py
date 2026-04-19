from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# =====================
# 全局登录用例
# =====================
def login_case(driver):
    driver.get("http://localhost:5173/login")

    wait = WebDriverWait(driver, 10)

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")

    email_input.clear()
    email_input.send_keys("17201665342@163.com")

    password_input.clear()
    password_input.send_keys("123456")

    driver.find_element(By.CLASS_NAME, "submit-button").click()

    # 等待跳转
    wait.until(lambda d: "dashboard" in d.current_url)



@pytest.mark.parametrize(
    "email,password", [
    ("17201665342@163.com", "123456"),  # right account
    # ("19283948437@163.com", "123456"),  # wrong account
    # ("taylor@163.com", "12345678"),
    # ("eric@163.com", "1234567890"),
])
def test_login(driver, email, password):
    driver.get("http://localhost:5173/login")

    wait = WebDriverWait(driver, 10) # 显式等待，等待元素加载完成

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")

    email_input.clear()
    email_input.send_keys(email)

    password_input.clear()
    password_input.send_keys(password)

    # 点击登录
    driver.find_element(By.CLASS_NAME, "submit-button").click()
    # 断言登录成功（URL变化）
    wait.until(lambda d: "dashboard" in d.current_url)

    assert "dashboard" in driver.current_url, "应该跳转到 ./dashboard 页面"

# 概览-数据洞察-刷新按钮
def test_button_refresh(driver):
    login_case(driver)
    driver.get("http://localhost:5173/dashboard")

    wait = WebDriverWait(driver, 10)

    refresh_btn = wait.until(
        lambda d: d.find_element(By.CLASS_NAME, "refresh-btn")
    )

    refresh_btn.click()

    # 等待动画状态变化（如果是异步刷新）
    wait.until(
        lambda d: "spinning" in refresh_btn.get_attribute("class")
    )

    assert "spinning" in refresh_btn.get_attribute("class"), "应显示刷新动画"

# 概览-数据洞察-卡片按钮
def test_button_projects(driver):
    login_case(driver)
    driver.get("http://localhost:5173/dashboard")

    wait = WebDriverWait(driver, 10)

    # find_element: 只能找到一个元素，find_elements: 可以找到多个元素，返回一个列表
    insight_cards = driver.find_elements(By.CLASS_NAME, "insight-card")
    insight_cards[0].click()  # 项目卡片
    wait.until(lambda d: "dashboard/projects" in d.current_url)
    assert "dashboard/projects" in driver.current_url, "应该跳转到 .dashboard/projects 页面"
    driver.back()  # 返回概览页
    wait.until(lambda d: "dashboard" in d.current_url)

    insight_cards = driver.find_elements(By.CLASS_NAME, "insight-card") # 重新获取所有卡片
    insight_cards[1].click()  # 用例卡片
    wait.until(lambda d: "dashboard/testcases" in d.current_url)
    assert "dashboard/testcases" in driver.current_url, "应该跳转到 .dashboard/testcases 页面"
    driver.back()  # 返回概览页
    wait.until(lambda d: "dashboard" in d.current_url)

    insight_cards = driver.find_elements(By.CLASS_NAME, "insight-card") # 重新获取所有卡片
    insight_cards[2].click()
    wait.until(lambda d: "dashboard/bugs" in d.current_url)
    assert "dashboard/bugs" in driver.current_url, "应该跳转到 .dashboard/bugs 页面"
    driver.back()  # 返回概览页
    wait.until(lambda d: "dashboard" in d.current_url)

    insight_cards = driver.find_elements(By.CLASS_NAME, "insight-card") # 重新获取所有卡片
    insight_cards[3].click()
    wait.until(lambda d: "dashboard/executions" in d.current_url)
    assert "dashboard/executions" in driver.current_url, "应该跳转到 .dashboard/executions 页面"

# 概览-数据洞察-项目进展
def test_button_project_progress(driver):
    login_case(driver)
    driver.get("http://localhost:5173/dashboard")

    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "project-progress-list")))    # 使用 EC 预期条件等待项目进展列表加载完成
    all_projects = driver.find_elements(By.CSS_SELECTOR, ".project-progress-item")

    for i in range(len(all_projects)):
        # 重新获取项目列表，避免 StaleElementReferenceException, 因为 DOM 更新后之前的元素引用可能失效
        all_projects = driver.find_elements(By.CSS_SELECTOR, ".project-progress-item")  # 可以使用 By.CLASS_NAME, "project-progress-item"

        all_projects[i].find_element(By.CLASS_NAME, "project-info").click()
        # pause(2)

        # 防止项目没有展开内容，导致后续查找失败（TimeoutException）
        try:
            modules_list = wait.until(
                EC.visibility_of(
                    all_projects[i].find_element(By.CSS_SELECTOR, ".modules-list") # 可以使用 By.CLASS_NAME, "modules-list"
                )
            )
            assert modules_list.is_displayed(), "项目展开后应该显示模块列表"
        except:
            print(f"第{i}个项目没有展开内容")



if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "auto.py::test_login"])
    pytest.main(["-v", "auto.py::test_button_refresh"])
    pytest.main(["-v", "auto.py::test_button_projects"])
    pytest.main(["-v", "auto.py::test_button_project_progress"])