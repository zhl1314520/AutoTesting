from auto_with_POM.pages.login_page import LoginPage
from auto_with_POM.conftest import driver


"""
登录相关的用例
"""
def test_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("17201665342@163.com", "123456")

    assert page.is_login_success()