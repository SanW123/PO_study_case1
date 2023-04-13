'''
实现步骤:(1)继承basepage,(2)元素传参,(3)调取方法
'''
from selenium.webdriver.common.by import By
from Base.basePage import BasePage


class Search(BasePage):

    def __init__(self, driver, url):
        BasePage.__init__(self, driver, url)

    # 进入网站
    def open_web(self):
        self.get()

    # 打开高级搜索框
    def open_higher_search(self):
        self.left_click(By.ID, 'search-button')
        self.left_click(By.CLASS_NAME, 'searching')

    # 输入搜索内容
    def input_search_content(self, text):
        self.send_text(text, By.CSS_SELECTOR, '.full-page-search')

    # 启用高级筛选器
    def higher_search(self):
        # 分类选择：学习笔记
        self.left_click(By.XPATH, "//*[text()='所有类别']")
        self.left_click(By.XPATH, "//*[text()='学习笔记']")
        # 话题选择：公开
        self.left_click(By.CSS_SELECTOR, '#search-status-options-header > div')
        self.left_click(By.XPATH, "//*[text()='公开']")
        # 拥有改标签选择：面经
        self.left_click(By.CSS_SELECTOR, '#search-with-tags-header > div')
        self.left_click(By.XPATH, "//*[text()='面经']")
        self.left_click(By.CSS_SELECTOR, '#search-with-tags-header > div')

    # 点击搜索按钮
    def click_search(self):
        self.left_click(By.CSS_SELECTOR, '.btn-primary')

    # 检测结果
    def check_search(self):
        text = self.get_element(By.CLASS_NAME, 'topic-title').text
        return text
