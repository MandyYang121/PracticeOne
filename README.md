Search Automation Demo
基于 Python + Selenium 的搜索引擎自动化测试脚本，支持 百度搜索​ 与 Bing 搜索​ 的自动化操作。

项目简介:
本项目使用 Python 和 Selenium WebDriver，实现对主流搜索引擎（百度、Bing）的自动化搜索流程。主要用于演示 Web 自动化测试的基本能力，包括元素定位、页面等待、结果验证等关键技术。

功能特性:
a. 百度搜索自动化：自动打开百度首页，输入关键词并执行搜索
b. Bing 搜索自动化：自动打开 Bing 首页，输入关键词并执行搜索
c. 智能等待机制：使用显式等待（Explicit Wait）确保页面元素加载完成
d. 结果验证：验证搜索结果页是否正确加载

技术栈:
Python 3.x
Selenium WebDriver
ChromeDriver（需自行下载并配置）
VS Code（开发环境）

项目结构:
.
├── testBaidu.py          # 百度搜索自动化脚本
├── testBing.py           # Bing 搜索自动化脚本
├── README.md             # 项目说明文档

脚本说明:
testBaidu.py: 自动化打开百度首页，搜索指定关键词，验证搜索结果
testBing.py: 自动化打开 Bing 首页，搜索指定关键词，验证搜索结果

涉及的技术要点:
Selenium WebDriver 元素定位（ID、CSS 选择器、XPath）
显式等待与隐式等待的使用场景
浏览器自动化操作的异常处理
页面加载状态的判断与处理

关于作者:
作者：Mandy Yang
GitHub：https://github.com/MandyYang121
