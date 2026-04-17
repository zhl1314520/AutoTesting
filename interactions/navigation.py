from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev")
driver.get("https://www.selenium.dev/selenium/web/index.html")

title = driver.title
assert title == "Index of Available Pages"

driver.back()   # 返回上一页
title = driver.title
assert title == "Selenium"

driver.forward()    # 前进到下一页
title = driver.title
assert title == "Index of Available Pages"

driver.refresh()
title = driver.title
assert title == "Index of Available Pages"

driver.quit()
