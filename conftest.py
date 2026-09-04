import time
from pathlib import Path

import pytest
import undetected_chromedriver as uc


@pytest.fixture(scope="module")
def driver():
    """用 undetected_chromedriver 启动 Chrome(反检测，避免百度安全验证）。

    version_main=144:指定 Chrome 主版本号，让 uc 下载匹配 144 的 chromedriver
    （默认会下载最新版 driver,可能和本机 Chrome 版本不一致）。
    """
    driver = uc.Chrome(driver_executable_path=str(Path(__file__).parent / "chromedriver.exe"), version_main=144)
    yield driver
    # 关闭浏览器
    time.sleep(2)
    driver.quit()
