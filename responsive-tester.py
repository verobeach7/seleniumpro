from math import ceil
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options # 자동 꺼짐 방지
from selenium.webdriver.chrome.service import Service as ChromeService
from urllib.parse import urlparse
import re
import os

options = Options()
options.add_experimental_option("detach", True) # 자동 꺼짐 방지

class ResponsiveTester:
    def __init__(self, urls):
        self.browser = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        self.browser.maximize_window()
        self.urls = urls
        self.sizes = [480, 960, 1366, 1920]

    def screenshot(self, url, dir):
        BROWSER_HEIGHT = self.browser.get_window_size().get("height")
        self.browser.get(url)
        for size in self.sizes:
            self.browser.set_window_size(size, BROWSER_HEIGHT)
            self.browser.execute_script("window.scrollTo(0, 0)")
            INNER_HEIGHT = self.browser.execute_script("return window.innerHeight")
            time.sleep(1)
            scroll_size = self.browser.execute_script("return document.body.scrollHeight")
            total_sections = ceil(scroll_size / INNER_HEIGHT)
            for section in range(total_sections + 1):
                self.browser.execute_script(f"window.scrollTo(0, {section * INNER_HEIGHT})")
                time.sleep(0.5)
                self.browser.save_screenshot(f"screenshots/{dir}/{dir}_{size}x{section}.png")

    def start(self):
        for url in self.urls:
            parsed = urlparse(url).netloc.replace("www.", "")
            dir = re.sub(r'\.\w*', "", parsed)
            check_path = os.path.isdir(f'./screenshots/{dir}')
            if not check_path:
                os.mkdir(f'./screenshots/{dir}')
            else:
                pass
            self.screenshot(url, dir)

tester = ResponsiveTester(["https://nomadcoders.co", "https://www.naver.com"])
tester.start()