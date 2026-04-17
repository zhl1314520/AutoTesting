import pytest
from selenium import webdriver
from selenium.webdriver.common.print_page_options import PrintOptions

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_orientation(driver):
    driver.get("https://www.selenium.dev/")
    print_options = PrintOptions()
    print_options.orientation = "landscape"     # portrait（纵向）或 landscape（横向）
    assert print_options.orientation == "landscape"

def test_range(driver):
    driver.get("https://www.selenium.dev/")
    print_options = PrintOptions()
    print_options.page_ranges = ["1, 2, 3"]     # 页码范围
    assert print_options.page_ranges == ["1, 2, 3"]

def test_size(driver):
    driver.get("https://www.selenium.dev/")
    print_options = PrintOptions()
    print_options.page_height = 27.94
    assert print_options.page_height == 27.94

def test_margin(driver):
    driver.get("https://www.selenium.dev/")
    print_options = PrintOptions()
    print_options.margin_top = 10   # 单位为毫米，默认值为 0
    print_options.margin_bottom = 10
    print_options.margin_left = 10
    print_options.margin_right = 10
    assert print_options.margin_top == 10
    assert print_options.margin_bottom == 10
    assert print_options.margin_left == 10
    assert print_options.margin_right == 10

def test_scale(driver):
    driver.get("https://www.selenium.dev/")
    print_options = PrintOptions()
    print_options.scale = 0.5 # 打印缩放比例，范围为 0.1 到 2.0，默认值为 1.0
    current_scale = print_options.scale
    assert current_scale == 0.5

def test_background(driver):    # 是否打印背景图像，默认为 False
    driver.get("https://www.selenium.dev/")
    print_options = PrintOptions()
    print_options.background = True
    assert print_options.background is True

def test_shrink_to_fit(driver):     # 是否自动适配
    driver.get("https://www.selenium.dev/")
    print_options = PrintOptions()
    print_options.shrink_to_fit = True
    assert print_options.shrink_to_fit is True
