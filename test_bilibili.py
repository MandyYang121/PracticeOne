from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_bilibili_search(driver):
    # 打开哔哩哔哩
    driver.get("https://www.bilibili.com")

    # 找到搜索框，输入关键字
    # 说明：bilibili 顶部搜索框是 .nav-search-input（旧的 #kw/#su 是百度选择器，这里不能用）
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav-search-input"))
    )
    search_box.send_keys("测试开发")

    # 回车搜索（bilibili 会在新标签页打开搜索结果）
    current_handles = driver.window_handles
    search_box.send_keys(Keys.ENTER)

    # 等新标签页打开并切换过去
    try:
        WebDriverWait(driver, 10).until(
            EC.new_window_is_opened(current_handles)
        )
        driver.switch_to.window(driver.window_handles[-1])
    except TimeoutException:
        pass

    # 断言搜索结果页标题包含关键字
    WebDriverWait(driver, 10).until(lambda d: "测试开发" in d.title)
    assert "测试开发" in driver.title, f"断言失败，页面标题为：{driver.title}"
    print(f"当前页面标题：{driver.title}")
