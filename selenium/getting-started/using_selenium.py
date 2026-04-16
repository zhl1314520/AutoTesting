from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_eight_components():
    driver = setup()

    title = driver.title        # 验证页面标题: 确保成功加载了正确的页面
    print(f"页面标题: {title}")
    assert title == "Web form"  # 断言: 如果标题不是 "Web form"，测试将失败

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text") # 获取 name = ”my-text“
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    print("已输入 'Selenium'")
    time.sleep(2)
    submit_button.click()
    print("已点击提交按钮")
    time.sleep(2)

    message = driver.find_element(by=By.ID, value="message")    # 获取 ID = "message" 的元素
    value = message.text        # 会获取元素的可见文本内容
    print(f"收到消息: {value}")
    assert value == "Received!"

    time.sleep(6)
    teardown(driver)    # 清理资源

# 初始化测试环境
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    print("已打开测试页面")
    time.sleep(2)
    return driver

# 测试结束，清理测试环境
def teardown(driver):
    driver.quit()


if __name__ == "__main__":
    test_eight_components()
