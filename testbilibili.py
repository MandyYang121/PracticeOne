from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. 启动 Chrome 浏览器
driver = webdriver.Chrome()  # 确保 chromedriver 在 PATH 里或同目录下

# 2. 打开哔哩哔哩
driver.get("https://www.bilibili.com") 

# 3. 找到搜索框，输入关键字
search_box = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.ID, "kw"))
)
search_box.send_keys("测试开发")

# 4. 点击“哔哩哔哩”按钮
search_button = driver.find_element(By.ID, "su")
search_button.click()

# 5. 等待结果加载
time.sleep(2)

# 6. 断言页面标题包含“测试开发”
assert "测试开发" in driver.title, f"断言失败，页面标题为：{driver.title}"
print("测试通过！")

# 7. 关闭浏览器
driver.quit()