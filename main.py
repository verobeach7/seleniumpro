from selenium import webdriver # web driver는 브라우저 컨트롤에 사용
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options # 자동 꺼짐 방지
from selenium.webdriver.common.by import By # By 사용을 위함
from selenium.webdriver.common.keys import Keys # Keys 사용을 위함

options = Options()
options.add_experimental_option("detach", True) # 자동 꺼짐 방지

KEYWORD = "finalcut"

# open browser
browser = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# go to site
browser.get("https://google.com")

# find search-bar
search_bar = browser.find_element(By.CLASS_NAME, "gLFyf")

# input keyword and send key
search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

# find elements
search_results = browser.find_elements(By.CLASS_NAME, "g")

# find element what I want to
for index, search_result in enumerate(search_results):
    class_name = search_result.get_attribute("class")
    if "g-blk" not in class_name:
        title = search_result.find_element(By.TAG_NAME, "h3")
        if title.size['height'] != 0 and "liYKde" not in class_name:
            search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")

browser.quit()