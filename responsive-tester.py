from math import ceil
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options # 자동 꺼짐 방지
from selenium.webdriver.chrome.service import Service as ChromeService

options = Options()
options.add_experimental_option("detach", True) # 자동 꺼짐 방지

BROWSER_HEIGHT = 1415

browser = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

browser.get("https://nomadcoders.co")
browser.maximize_window()

sizes = [480, 960, 1366, 1920]

for size in sizes:
    browser.set_window_size(size, BROWSER_HEIGHT)
    time.sleep(2)
    scroll_size = browser.execute_script("return document.body.scrollHeight")
    total_sections = ceil(scroll_size / BROWSER_HEIGHT)
    for section in range(total_sections):
        browser.execute_script(f"window.scrollTo(0, {section * BROWSER_HEIGHT})")
        time.sleep(1)
        browser.save_screenshot(f"screenshots/{size}x{section}.png")