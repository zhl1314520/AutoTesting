from selenium import webdriver
from selenium.webdriver.common.by import By     # by: 定位元素

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title            # 获取html标题

driver.implicitly_wait(0.5)     # 设置隐式等待时间为 0.5 秒，当查找元素时如果元素不存在，会等待最多 0.5 秒

# by=By.NAME 表示按照 HTML 元素的 name 属性来查找. name 具体值为 my-text
# 这行代码会在网页中查找 <input name="my-text" ...> 或 <textarea name="my-text" ...> 这样的元素
text_box = driver.find_element(by=By.NAME, value="my-text")
# by=By.CSS_SELECTOR 表示使用 CSS 选择器语法
# value="button" 表示查找页面上的 <button> 元素
# 这会找到页面上第一个 <button> 标签
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")  # 模拟输入 "Selenium"
submit_button.click()           # 模拟点击

# 找到 ID 为 "message" 的元素（通常是显示结果的区域）
message = driver.find_element(by=By.ID, value="message")
# 获取该元素的文本内容
text = message.text

driver.quit()     # 关闭浏览器窗口并结束 WebDriver 会话
