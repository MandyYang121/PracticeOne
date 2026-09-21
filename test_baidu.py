import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.baidu_page import BaiduHomePage


def _close_extra_tabs(driver):
    """关闭除第一个标签页外的所有标签页，并切回第一个。

    三个参数化用例共享同一个浏览器(module scope)，每个用例点完结果后会把详情页
    留在新标签页里；清理后每个用例都从单标签页的干净状态开始，避免标签页累积。
    """
    while len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
    driver.switch_to.window(driver.window_handles[0])


@pytest.mark.parametrize("keyword", ["牡丹", "猫咪", "大海"])
def test_baidu_search(driver, keyword):
    # 清理上个用例残留的标签页，回到单标签页干净状态
    _close_extra_tabs(driver)

    # 首页搜索
    home = BaiduHomePage(driver)
    home.open()
    result_page = home.search(keyword)

    # 点第二个结果，若新开标签页则切换过去
    current_handles = driver.window_handles
    result_title = result_page.click_result(1)
    try:
        WebDriverWait(driver, 10).until(EC.new_window_is_opened(current_handles))
        driver.switch_to.window(driver.window_handles[-1])
    except TimeoutException:
        pass

    # 等详情页加载完成（标题非空）
    WebDriverWait(driver, 10).until(lambda d: d.title)
    assert driver.title, "详情页标题为空，未成功打开详情页"
    print(f"点击搜索结果：{result_title}")
    print(f"当前页面标题：{driver.title}")
