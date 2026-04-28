from selenium.webdriver.common.by import By
from auto_with_POM.pages.base_page import BasePage

class ProjectPage(BasePage):
    url = "http://localhost:5173/dashboard/projects"

    project_cards = (By.CLASS_NAME, "project-card")
    detail_modal = (By.CLASS_NAME, "detail-modal")
    edit_btn = (By.CLASS_NAME, "btn-edit")

    def open(self):
        self.driver.get(self.url)

    def open_project_detail(self, index):
        cards = self.finds(self.project_cards)
        cards[index].click()

    def is_detail_visible(self):
        try:
            return self.find(self.detail_modal).is_displayed()
        except:
            return False

    def click_edit(self, index):
        cards = self.finds(self.project_cards)
        cards[index].find_element(*self.edit_btn).click()