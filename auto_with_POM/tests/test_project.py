from auto_with_POM.pages.project_page import ProjectPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
project 相关的用例
"""
# 项目详情
def test_project_detail(driver, login): # 先加载执行依赖然后执行方法里面的代码
    page = ProjectPage(driver)  # 实例化页面对象

    # 添加等待，确保登录后跳转到 dashboard
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    page.open()
    project_count = page.get_project_count()
    for i in range(project_count):
        page.open_project_detail(i)
        # 判断详情页是否可见
        assert page.is_detail_visible()
        # 关闭详情页
        page.close_button()
        # 等待
        page.wait_for_close_button(driver)
