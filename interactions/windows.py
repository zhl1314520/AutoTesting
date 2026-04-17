from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

with webdriver.Chrome() as driver:
    driver.get("https://seleniumhq.github.io")

    wait = WebDriverWait(driver, 10)

    original_window = driver.current_window_handle  # 记录当前窗口

    assert len(driver.window_handles) == 1  # 确保只有一个窗口（防御性代码）

    driver.find_element(By.LINK_TEXT, "new window").click() # 打开新窗口

    wait.until(expected_conditions.number_of_windows_to_be(2))

    for window_handle in driver.window_handles:     # 切换到新窗口
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    wait.until(expected_conditions.title_is("SeleniumHQ Browser Automation"))   # 验证新窗口切换成功