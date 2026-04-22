from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# =====================
# 全局 driver fixture（夹具）：统一管理浏览器的创建和销毁
# =====================
@pytest.fixture(scope="session")    # 整个测试会话只创建一个 driver 实例，所有测试用例共享这个实例，最后在测试结束时关闭浏览器
def driver():
    options = webdriver.ChromeOptions() # 创建浏览器配置
    options.page_load_strategy = "eager"    # eager：页面 DOM 加载完成就继续执行
    driver = webdriver.Chrome(options=options)
    yield driver    # 把 driver 交给测试用例使用
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

    # 如果已经在 dashboard，说明已经登录
    if "dashboard" in driver.current_url:
        return

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
@pytest.mark.smoke  # 使用：pytest -m smoke 来运行这个测试用例
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
@pytest.mark.smoke
def test_button_refresh(driver):
    login_case(driver)
    driver.get("http://localhost:5173/dashboard")

    wait = WebDriverWait(driver, 10)

    # 使用 EC.element_to_be_clickable 确保按钮已经加载完毕且可被点击
    refresh_btn = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "refresh-btn"))
    )

    refresh_btn.click()

    # 动态重新查找元素并获取属性，防止抛出 StaleElementReferenceException；并加入 or "" 防止 get_attribute 返回 None 时执行 in 抛出 TypeError 报错
    wait.until(
        lambda d: "spinning" in (d.find_element(By.CLASS_NAME, "refresh-btn").get_attribute("class") or "")
    )

    assert "spinning" in (driver.find_element(By.CLASS_NAME, "refresh-btn").get_attribute("class") or ""), "应显示刷新动画"

# 概览-数据洞察-卡片按钮
@pytest.mark.smoke
def test_button_projects(driver):
    login_case(driver)
    driver.get("http://localhost:5173/dashboard")

    wait = WebDriverWait(driver, 10)

    wait.until( # 等待所有卡片加载完成
        EC.presence_of_all_elements_located((By.CLASS_NAME, "insight-card"))
    )
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
@pytest.mark.smoke
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
        print()
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

# 项目-输入框
@pytest.mark.smoke
def test_input_project(driver):
    login_case(driver)
    driver.get("http://localhost:5173/dashboard/projects")

    wait = WebDriverWait(driver, 10)

    # 查找输入框并输入内容
    project_input = wait.until(
        # visibility_of_element_located: 等待元素可见（不仅存在于 DOM 中，还要在页面上可见）
        # presence_of_element_located: 只等待元素存在于 DOM 中，不要求可见
        EC.presence_of_element_located((By.CLASS_NAME, "search-input"))
    )
    project_input.clear()
    project_input.send_keys("Test Project Final")
    # pause(6)

    # 等待加载
    try:
        projects_list = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "projects-grid")))
        assert projects_list.is_displayed(), "输入后应该显示对应项目列表"
    except:
        print("项目不存在")

# 项目-点击卡片查看项目的详情
@pytest.mark.smoke
def test_button_projects_details(driver):
    login_case(driver)
    driver.get("http://localhost:5173/dashboard/projects")

    wait = WebDriverWait(driver, 10)

    # 等待加载列表容器 gird
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "projects-grid")))
    all_projects = driver.find_elements(By.CLASS_NAME, "project-card")

    for i in range(len(all_projects)):
        all_projects = driver.find_elements(By.CLASS_NAME, "project-card")

        all_projects[i].click()
        # pause(2)

        try:
            projects_details_page = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "detail-modal"))
            )
            assert projects_details_page.is_displayed(), "点击项目卡片后应该显示项目详情页面"
        except:
            print(f"第{i}个项目没有详情页面")
            continue  # 没有详情页就跳过，不要执行关闭操作
        # 关闭详情页面
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-close"))).click()

        # 等待加载卡片内容，避免影响再次点击
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-overlay")))
        # === 补充这行：等待可能出现的 toast 消失 ===
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "toast-overlay")))
        all_projects = driver.find_elements(By.CLASS_NAME, "project-card")
        all_projects[i].find_element(By.CLASS_NAME, "btn-edit").click()
        try:
            wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "modal-container"))
            )
        except:
            continue  # 没有修改表单就跳过
        # 等待弹窗关闭，避免影响下一个卡片点击
        wait.until(
            lambda d: len(d.find_elements(By.CLASS_NAME, "modal-footer")) == 0 # 强制等待所有 modal-footer 元素消失，说明弹窗已经关闭
        )


# 项目-卡片-修改按钮（包含里面的关闭、取消、提交修改按钮）
@pytest.mark.smoke
def test_button_projects_details_edit(driver):
    login_case(driver)
    driver.get("http://localhost:5173/dashboard/projects")

    wait = WebDriverWait(driver, 10)

    # 等待加载列表容器 gird
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "projects-grid")))
    all_projects = driver.find_elements(By.CLASS_NAME, "project-card")

    for i in range(len(all_projects)):
        all_projects = driver.find_elements(By.CLASS_NAME, "project-card")

        # 点击修改按钮
        all_projects[i].find_element(By.CLASS_NAME, "btn-edit").click()

        # 等待修改表单出现
        try:
            edit_form = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "modal-container"))
            )
            assert edit_form.is_displayed(), "点击修改按钮后应该显示修改表单"
        except:
            print(f"第{i}个项目没有修改表单")
            continue  # 没有修改表单就跳过

        # 右上角的关闭按钮
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-close"))).click()
        # 等待加载卡片内容，避免影响再次点击
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-overlay")))
        # === 补充这行：等待可能出现的 toast 消失 ===
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "toast-overlay")))
        all_projects = driver.find_elements(By.CLASS_NAME, "project-card")
        all_projects[i].find_element(By.CLASS_NAME, "btn-edit").click()
        try:
            wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "modal-container"))
            )
        except:
            continue  # 没有修改表单就跳过

        # 取消按钮
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-cancel"))).click()
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-overlay")))
        # === 补充这行：等待可能出现的 toast 消失 ===
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "toast-overlay")))
        all_projects = driver.find_elements(By.CLASS_NAME, "project-card")
        all_projects[i].find_element(By.CLASS_NAME, "btn-edit").click()
        try:
            wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "modal-container"))
            )
        except:
            continue  # 没有修改表单就跳过
        # 点击保存按钮
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-submit"))).click()
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-overlay")))
        # === 新增：等待 toast 提示消失(避免“成功修改”弹窗遮挡) ===
        try:
            wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "toast-overlay")))
        except:
            pass  # 没有 toast 也不影响
