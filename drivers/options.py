from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType

"""

这些函数主要测试和演示 sel_tests WebDriver 的各种 浏览器配置选项
"""

# 页面加载策略(normal)
def test_page_load_strategy_normal():
    options = get_default_chrome_options()      # 浏览器启动配置
    options.page_load_strategy = 'normal'       # normal: 等待页面完全加载完成（HTML + CSS + JS + 图片）
    driver = webdriver.Chrome(options=options)  # 带配置启动浏览器
    driver.get("https://www.selenium.dev/")
    driver.quit()


def test_page_load_strategy_eager():
    options = get_default_chrome_options()
    options.page_load_strategy = 'eager'    # eager: DOM 加载完就返回,不等待 CSS、JS、图片等资源加载完成
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.selenium.dev/")
    driver.quit()


def test_page_load_strategy_none():
    options = get_default_chrome_options()
    options.page_load_strategy = 'none'     # none: 完全不等页面加载,get() 一执行就返回
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.selenium.dev/")
    driver.quit()

# 超时设置（脚本）
def test_timeouts_script():
    options = get_default_chrome_options()
    options.timeouts = {'script': 5000}     # 最大脚本执行时间
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.selenium.dev/")
    driver.quit()

# （页面加载）
def test_timeouts_page_load():
    options = get_default_chrome_options()
    options.timeouts = {'pageLoad': 5000}
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.selenium.dev/")
    driver.quit()

# （隐式等待）
def test_timeouts_implicit_wait():
    options = get_default_chrome_options()
    options.timeouts = {'implicit': 5000}
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.selenium.dev/")
    driver.quit()

# 设置未处理的 JS 弹窗
def test_unhandled_prompt():
    options = get_default_chrome_options()
    options.unhandled_prompt_behavior = 'accept'    # 页面弹窗自动点确定
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.selenium.dev/")
    driver.quit()

# 设置浏览器窗口矩形属性（位置和尺寸）
def test_set_window_rect():
    options = webdriver.FirefoxOptions()
    options.set_window_rect = True  # Chrome 默认支持，Firefox 需要显式开启
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.selenium.dev/")
    driver.quit()

# 启用严格的文件输入交互性检查
def test_strict_file_interactability():
    options = get_default_chrome_options()
    options.strict_file_interactability = True
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.selenium.dev/")
    driver.quit()

# 配置代理服务器设置
def test_proxy():
    options = get_default_chrome_options()
    options.proxy = Proxy({'proxyType': ProxyType.MANUAL, 'httpProxy': 'http.proxy:1234'})
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.selenium.dev/")
    driver.quit()


def test_set_browser_name():
    options = get_default_chrome_options()
    assert options.capabilities['browserName'] == 'chrome'
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.selenium.dev/")
    driver.quit()


def test_set_browser_version():
    options = get_default_chrome_options()
    options.browser_version = 'stable'
    assert options.capabilities['browserVersion'] == 'stable'
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.selenium.dev/")
    driver.quit()


def test_platform_name():
    options = get_default_chrome_options()
    options.platform_name = 'any'       # 任何操作系统都可以
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.selenium.dev/")
    driver.quit()

# 设置接受自签名证书或过期的 HTTPS 证书
def test_accept_insecure_certs():
    options = get_default_chrome_options()
    options.accept_insecure_certs = True
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.selenium.dev/")
    driver.quit()


def get_default_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    return options

