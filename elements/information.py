from selenium import webdriver
from selenium.webdriver.common.by import By


def test_informarion():
    driver = webdriver.Chrome()
    driver.implicitly_wait(0.5)

    driver.get("https://www.selenium.dev/selenium/web/inputs.html")

    # 检查连接的元素是否显示在网页上
    is_email_visible = driver.find_element(By.NAME, "email_input").is_displayed()
    assert is_email_visible == True

    # 检查网页上连接的元素是否已启用或禁用
    is_enabled_button = driver.find_element(By.NAME, "button_input").is_enabled()
    assert is_enabled_button == True

    # 用于确定引用的元素是否被选中
    is_selected_check = driver.find_element(By.NAME, "checkbox_input").is_selected()
    assert is_selected_check == True

    # 获取标签名称
    tag_name_inp = driver.find_element(By.NAME, "email_input").tag_name
    assert tag_name_inp == "input"

    # 获取元素的位置和大小
    rect = driver.find_element(By.NAME, "range_input").rect
    assert rect["x"] == 10      # 这个元素在页面上的横坐标是 10 像素

    # 获取元素的 CSS 属性值
    css_value = driver.find_element(By.NAME, "color_input").value_of_css_property(
        "font-size"
    )
    assert css_value == "13.3333px"

    # 获取元素文本
    text = driver.find_element(By.TAG_NAME, "h1").text
    assert text == "Testing Inputs" # 标题是不是 "Testing Inputs"


    email_txt = driver.find_element(By.NAME, "email_input")
    value_info = email_txt.get_attribute("value")
    assert value_info == "admin@localhost"
