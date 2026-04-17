from selenium import webdriver

# 此页面的脚本主要测试了 webdriver.ChromeService 的使用方法，展示了如何通过 Service 来管理 ChromeDriver 的启动和配置。
def test_basic_service():
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)
    # 上面两行等价于: driver = webdriver.Chrome()

    driver.quit()


def test_driver_location(chromedriver_bin, chrome_bin):
    options = get_default_chrome_options()
    options.binary_location = chrome_bin        # 指定 Chrome 浏览器的路径

    service = webdriver.ChromeService(executable_path=chromedriver_bin)

    driver = webdriver.Chrome(service=service, options=options)

    driver.quit()


def test_driver_port():
    service = webdriver.ChromeService(port=1234)

    driver = webdriver.Chrome(service=service)

    driver.quit()

def get_default_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    return options
