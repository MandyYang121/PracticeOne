import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. 用 undetected_chromedriver 启动 Chrome
#    version_main=144：指定 Chrome 主版本号，让 uc 下载匹配 144 的 chromedriver
#    （默认会下载最新版 driver，可能和本机 Chrome 版本不一致）
driver = uc.Chrome(version_main=144)

try:
    # 2. 打开百度
    driver.get("https://www.baidu.com")
    time.sleep(2)

    # 3. 找到搜索框，输入关键字「牡丹花」
    #    说明：百度首页已改版，老的 #kw 表单是隐藏的，新的可见输入框是 #chat-textarea
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "chat-textarea"))
    )
    search_box.send_keys("牡丹")

    # 4. 回车搜索
    search_box.send_keys(Keys.ENTER)

    # 5. 等待搜索结果加载，用 find_elements 拿到所有结果链接，点第二个（下标 1）
    results = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3 a"))
    )
    second_result = results[1]
    result_title = second_result.text
    print(f"点击搜索结果：{result_title}")

    # 6. 点击该链接，打开详情页
    second_result.click()

    # 7. 等待详情页加载；若在新标签页打开则切换过去
    time.sleep(3)
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])

    print(f"当前页面标题：{driver.title}")
    print("已成功打开详情页！")

finally:
    # 8. 关闭浏览器
    time.sleep(2)
    driver.quit()
    print("浏览器已关闭。")
