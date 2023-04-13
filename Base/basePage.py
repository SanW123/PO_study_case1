from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url

    # 进入网址
    def get(self):
        self.driver.get(self.base_url)

    # 元素定位,替代八大定位
    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    # 模拟鼠标点击
    def left_click(self, *locator):
        ActionChains(self.driver).click(self.get_element(*locator)).perform()

    # 输入文本
    def send_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    # 清除
    def clear_text(self, *locator):
        self.driver.find_element(*locator).clear()

    # 显示等待
    def web_wait(self, *locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                *locator
            )
        )


