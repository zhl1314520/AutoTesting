from auto_with_POM.pages.dashboard_page import DashboardPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from auto_with_POM.conftest import pause

"""
dashboard 相关的用例
"""
# 刷新按钮
def test_refresh(driver, login):    # 利用封装的 conftest/login 注入依赖
    dashboard = DashboardPage(driver)

    # 添加等待，确保登录后跳转到 dashboard
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    dashboard.open()
    dashboard.click_refresh()

    assert dashboard.is_refreshing()


# 卡片
def test_dashboard_cards(driver, login):
    dashboard = DashboardPage(driver)

    # 添加等待，确保登录后跳转到 dashboard
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    dashboard.open()
    dashboard.click_card(0)
    # pause(2)
    assert "projects" in driver.current_url
    driver.back()

    dashboard.click_card(1)
    # pause(2)
    assert "testcases" in driver.current_url
    driver.back()

    dashboard.click_card(2)
    # pause(2)
    assert "bugs" in driver.current_url
    driver.back()

    dashboard.click_card(3)
    assert "executions" in driver.current_url