"""百度首页 / 搜索结果页的 Page Object。"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaiduHomePage:
    """百度首页：封装 URL、搜索框定位与搜索动作。"""

    URL = "https://www.baidu.com"
    # 百度搜索框有 A/B 两套动态切换：新版 #chat-textarea / 经典版 #kw
    _SEARCH_BOX_SELECTORS = ("#chat-textarea", "#kw")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """打开百度首页。"""
        self.driver.get(self.URL)
        return self

    def search(self, keyword):
        """输入关键词并回车，返回结果页对象。"""
        box = WebDriverWait(self.driver, 10).until(
            lambda d: self._find_visible_search_box()
        )
        box.send_keys(keyword)
        box.send_keys(Keys.ENTER)
        return BaiduResultPage(self.driver)

    def _find_visible_search_box(self):
        """返回当前可见且可点的那个搜索框，找不到返回 None。"""
        for selector in self._SEARCH_BOX_SELECTORS:
            try:
                el = self.driver.find_element(By.CSS_SELECTOR, selector)
            except Exception:
                continue
            if el.is_displayed() and el.is_enabled():
                return el
        return None


class BaiduResultPage:
    """百度搜索结果页：封装结果链接定位与点击。"""

    def __init__(self, driver):
        self.driver = driver

    def get_results(self):
        """等待并返回所有结果标题链接。"""
        return WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3 a"))
        )

    def click_result(self, index):
        """点击第 index 个结果链接，返回它的标题。"""
        results = self.get_results()
        assert len(results) > index, f"搜索结果不足 {index + 1} 条，无法点击"
        result = results[index]
        title = result.text
        assert title, "搜索结果标题为空"
        result.click()
        return title
