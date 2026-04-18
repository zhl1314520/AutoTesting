import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# =====================
# 全局 driver fixture
# =====================
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_select_options(driver):
    driver.get('http://localhost:63342/AutoTesting/support_features/select_lists.html?_ijt=le07sf22t30hfn63ubs00f8rcs&_ij_reload=RELOAD_ON_SAVE')

    select_element = driver.find_element(By.NAME, 'selectomatic')
    select = Select(select_element)

    two_element = driver.find_element(By.CSS_SELECTOR, 'option[value=two]')
    four_element = driver.find_element(By.CSS_SELECTOR, 'option[value=four]')
    count_element = driver.find_element(By.CSS_SELECTOR, "option[value='still learning how to count, apparently']")

    select.select_by_visible_text('Four')
    assert four_element.is_selected()

    select.select_by_value('two')
    assert two_element.is_selected()

    select.select_by_index(3)
    assert count_element.is_selected()


def test_select_multiple_options(driver):
    driver.get('http://localhost:63342/AutoTesting/support_features/select_lists.html?_ijt=le07sf22t30hfn63ubs00f8rcs&_ij_reload=RELOAD_ON_SAVE')
    select_element = driver.find_element(By.NAME, 'multi')
    select = Select(select_element)

    ham_element = driver.find_element(By.CSS_SELECTOR, 'option[value=ham]')
    gravy_element = driver.find_element(By.CSS_SELECTOR, "option[value='onion gravy']")
    egg_element = driver.find_element(By.CSS_SELECTOR, 'option[value=eggs]')
    sausage_element = driver.find_element(By.CSS_SELECTOR, "option[value='sausages']")

    option_elements = select_element.find_elements(By.TAG_NAME, 'option')
    option_list = select.options
    assert option_elements == option_list

    selected_option_list = select.all_selected_options
    expected_selection = [egg_element, sausage_element]
    assert selected_option_list == expected_selection

    select.select_by_value('ham')
    select.select_by_value('onion gravy')
    assert ham_element.is_selected()
    assert gravy_element.is_selected()

    select.deselect_by_value('eggs')
    select.deselect_by_value('sausages')
    assert not egg_element.is_selected()
    assert not sausage_element.is_selected()

# Selenium 的 Select 类不支持选择 disabled 选项，尝试选择 disabled 选项会抛出 NotImplementedError 异常
def test_disabled_options(driver):
    driver.get('http://localhost:63342/AutoTesting/support_features/select_lists.html?_ijt=le07sf22t30hfn63ubs00f8rcs&_ij_reload=RELOAD_ON_SAVE')

    select_element = driver.find_element(By.NAME, 'single_disabled')
    select = Select(select_element)

    with pytest.raises(NotImplementedError):
        select.select_by_value('disabled')
