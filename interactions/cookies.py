from selenium import webdriver


def test_add_cookie():
    driver = webdriver.Chrome()
    driver.get("http://www.example.com")    # 示例网址

    # 添加一个名为 "key"、值为 "value" 的 cookie 到当前浏览器上下文
    driver.add_cookie({"name": "key", "value": "value"})


def test_get_named_cookie():
    driver = webdriver.Chrome()
    driver.get("http://www.example.com")

    # 添加一个名为 "foo"、值为 "bar" 的 cookie 到当前浏览器上下文
    driver.add_cookie({"name": "foo", "value": "bar"})

    print(driver.get_cookie("foo"))


def test_get_all_cookies():
    driver = webdriver.Chrome()

    driver.get("http://www.example.com")

    driver.add_cookie({"name": "test1", "value": "cookie1"})
    driver.add_cookie({"name": "test2", "value": "cookie2"})

    print(driver.get_cookies())

def test_delete_cookie():
    driver = webdriver.Chrome()

    driver.get("http://www.example.com")

    driver.add_cookie({"name": "test1", "value": "cookie1"})
    driver.add_cookie({"name": "test2", "value": "cookie2"})

    driver.delete_cookie("test1")


def test_delete_all_cookies():
    driver = webdriver.Chrome()

    driver.get("http://www.example.com")

    driver.add_cookie({"name": "test1", "value": "cookie1"})
    driver.add_cookie({"name": "test2", "value": "cookie2"})

    driver.delete_all_cookies()

# 测试同站点的 cookie 属性
def test_same_side_cookie_attr():
    driver = webdriver.Chrome()

    driver.get("http://www.example.com")

    driver.add_cookie({"name": "foo", "value": "value", "sameSite": "Strict"})
    driver.add_cookie({"name": "foo1", "value": "value", "sameSite": "Lax"})

    cookie1 = driver.get_cookie("foo")
    cookie2 = driver.get_cookie("foo1")

    print(cookie1)
    print(cookie2)
