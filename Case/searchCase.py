import unittest

import allure
import pytest
from selenium import webdriver

from Page.searchPage import Search


class TestSearch(unittest.TestCase):
    """
    1, 打开ceshiren网站
    2, 点击首页的搜索按钮
    3, 点击高级搜搜按钮
    4, 输入搜索信息
    5, 点击搜索
    6, 断言搜索的信息和结果内容是相关的
    """

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)

    # 冒烟测试，测试高级搜索的基本功能是否有缺陷
    @pytest.mark.somke
    def test_search(self):
        search_text = "测试"
        url = "https://ceshiren.com"
        # 创建对象
        s = Search(self.driver, url)
        # 打开被测网站
        s.open_web()
        # 打开高级搜索框
        s.open_higher_search()
        # 输入搜索内容
        s.input_search_content(search_text)
        # 启用高级筛选器
        s.higher_search()
        # 点击搜索按钮
        s.click_search()
        # 检测结果
        check_text = s.check_search()
        # 断言
        try:
            assert search_text in check_text
        except:
            # 异常则截图
            allure.attach.file("image.png", name="hogwarts", attachment_type=allure.attachment_type.PNG)
            raise
        finally:
            print("测试完毕")

    def tearDown(self) -> None:
        self.driver.quit()
