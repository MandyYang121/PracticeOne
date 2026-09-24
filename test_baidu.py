import allure
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


@allure.feature("百度搜索")
@allure.story("搜索并打开详情页")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("搜索「{keyword}」并打开第二个结果详情页")
@pytest.mark.parametrize("keyword", ["牡丹", "猫咪", "大海"])
def test_baidu_search(driver, keyword):
    # 清理上个用例残留的标签页，回到单标签页干净状态
    _close_extra_tabs(driver)

    with allure.step("打开百度首页"):
        home = BaiduHomePage(driver)
        home.open()

    with allure.step(f"搜索关键词「{keyword}」"):
        result_page = home.search(keyword)

    with allure.step("点击第二个搜索结果"):
        current_handles = driver.window_handles
        result_title = result_page.click_result(1)

    with allure.step("切换并等待详情页加载"):
        try:
            WebDriverWait(driver, 10).until(EC.new_window_is_opened(current_handles))
            driver.switch_to.window(driver.window_handles[-1])
        except TimeoutException:
            pass
        WebDriverWait(driver, 10).until(lambda d: d.title)

    assert driver.title, "详情页标题为空，未成功打开详情页"

    # 附加报告信息：详情页标题文本 + 截图
    allure.attach(driver.title, name="详情页标题", attachment_type=allure.attachment_type.TEXT)
    allure.attach(driver.get_screenshot_as_png(), name="详情页截图", attachment_type=allure.attachment_type.PNG)

    print(f"点击搜索结果：{result_title}")
    print(f"当前页面标题：{driver.title}")
