from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_bing_search(driver):
    # 打开 Bing
    driver.get("https://www.bing.com")

    # 等待搜索框可交互，输入关键字「牡丹花」
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "sb_form_q"))
    )
    search_box.send_keys("牡丹花")

    # 回车搜索
    search_box.send_keys(Keys.ENTER)

    # 等待搜索结果加载，找到第一个搜索结果链接
    first_result = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "li.b_algo h2 a"))
    )
    result_title = first_result.text
    assert result_title, "第一个搜索结果标题为空"
    print(f"点击搜索结果：{result_title}")

    # 点击该链接，打开详情页
    current_handles = driver.window_handles
    first_result.click()

    # 等待详情页加载；若新开标签页则切换过去，否则同页跳转
    try:
        WebDriverWait(driver, 10).until(
            EC.new_window_is_opened(current_handles)
        )
        driver.switch_to.window(driver.window_handles[-1])
    except TimeoutException:
        pass

    assert driver.title, "详情页标题为空，可能未成功打开详情页"
    print(f"当前页面标题：{driver.title}")
