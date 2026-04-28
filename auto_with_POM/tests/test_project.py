from auto_with_POM.pages.project_page import ProjectPage

"""
project 相关的用例
"""
# 项目详情
def test_project_detail(driver, login):
    page = ProjectPage(driver)
    page.open()

    page.open_project_detail(0)

    assert page.is_detail_visible()