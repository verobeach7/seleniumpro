from selenium import webdriver # web driver는 브라우저 컨트롤에 사용
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options # 자동 꺼짐 방지
from selenium.webdriver.common.by import By # By 사용을 위함
from selenium.webdriver.common.keys import Keys # Keys 사용을 위함

options = Options()
options.add_experimental_option("detach", True) # 자동 꺼짐 방지

browser = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

browser.get("https://google.com")

search_bar = browser.find_element(By.CLASS_NAME, "gLFyf")

search_bar.send_keys("hello!")
search_bar.send_keys(Keys.ENTER)

search_results = browser.find_elements(By.CLASS_NAME, "MjjYud")

print(search_results)