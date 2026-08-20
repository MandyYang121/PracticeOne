from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. 启动 Chrome 浏览器（确保 chromedriver.exe 在 PATH 或同目录下）
driver = webdriver.Chrome()

try:
    # 2. 打开 Bing
    driver.get("https://www.bing.com")

    # 3. 等待搜索框可交互，输入关键字「牡丹花」
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "sb_form_q"))
    )
    search_box.send_keys("牡丹花")

    # 4. 回车搜索
    search_box.send_keys(Keys.ENTER)

    # 5. 等待搜索结果加载，找到第一个搜索结果链接。
    first_result = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "li.b_algo h2 a"))
    )
    result_title = first_result.text
    print(f"点击搜索结果：{result_title}")

    # 6. 点击该链接，打开详情页
    first_result.click()

    # 7. 等待详情页加载
    time.sleep(3)

    # 如果结果在新窗口/标签页打开，切换到最新的窗口
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])

    print(f"当前页面标题：{driver.title}")
    print("已成功打开详情页！")

finally:
    # 8. 关闭浏览器
    time.sleep(2)
    driver.quit()
    print("浏览器已关闭。")
