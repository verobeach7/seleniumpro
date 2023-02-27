import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options # 자동 꺼짐 방지
from selenium.webdriver.chrome.service import Service as ChromeService


options = Options()
options.add_experimental_option("detach", True) # 자동 꺼짐 방지

browser = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

browser.get("https://nomadcoders.co")
browser.maximize_window()

sizes = [480, 960, 1366, 1920]

print(browser.get_window_size())

for size in sizes:
    browser.set_window_size(size, 1415)
    time.sleep(3)