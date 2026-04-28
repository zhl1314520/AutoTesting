from selenium.webdriver.common.by import By
from auto_with_POM.pages.base_page import BasePage

class DashboardPage(BasePage):

    url = "http://localhost:5173/dashboard"

    refresh_btn = (By.CLASS_NAME, "refresh-btn")
    insight_cards = (By.CLASS_NAME, "insight-card")

    def open(self):
        self.driver.get(self.url)

    def click_refresh(self):
        self.click(self.refresh_btn)

    def is_refreshing(self):
        btn = self.find(self.refresh_btn)
        return "spinning" in (btn.get_attribute("class") or "")

    def click_card(self, index):
        cards = self.finds(self.insight_cards)
        cards[index].click()