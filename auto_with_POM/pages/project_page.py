from selenium.webdriver.common.by import By
from auto_with_POM.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProjectPage(BasePage):
    url = "http://localhost:5173/dashboard/projects"

    project_card = (By.CLASS_NAME, "project-card")
    detail_modal = (By.CLASS_NAME, "detail-modal")
    right_top_close_button = (By.CLASS_NAME, "btn-close")
    edit_btn = (By.CLASS_NAME, "btn-edit")

    def open(self):
        self.driver.get(self.url)

    def get_project_count(self):
        cards = self.finds(self.project_card)
        num = len(cards)
        return num

    def open_project_detail(self, index):
        cards = self.finds(self.project_card)
        cards[index].click()
        # 等待详情弹窗出现
        self.wait.until(EC.visibility_of_element_located(self.detail_modal))

    def close_button(self):
        # 先等待关闭按钮可点击
        self.wait.until(EC.element_to_be_clickable(self.right_top_close_button))
        # 直接点击找到的第一个关闭按钮
        self.click(self.right_top_close_button)

    def wait_for_close_button(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.right_top_close_button))

    def is_detail_visible(self):
        try:
            return self.find(self.detail_modal).is_displayed()
        except:
            return False

    def click_edit(self, index):
        cards = self.finds(self.project_card)
        cards[index].find_element(*self.edit_btn).click()