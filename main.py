from selenium import webdriver # web driver는 브라우저 컨트롤에 사용
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC # wait을 사용하기 위해서(javascript로 작동하여 로딩하는데 시간이 걸리는 경우)
from selenium.webdriver.support.ui import WebDriverWait # wait 사용
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options # 자동 꺼짐 방지
from selenium.webdriver.common.by import By # By 사용을 위함
from selenium.webdriver.common.keys import Keys # Keys 사용을 위함

options = Options()
options.add_experimental_option("detach", True) # 자동 꺼짐 방지

class GoogleKeywordScreenshotter:
    def __init__(self, keyword, screenshots_dir):
        self.browser = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        self.keyword = keyword
        self.screenshots_dir = screenshots_dir
    def start(self):
        self.browser.get("https://google.com")
        search_bar = self.browser.find_element(By.CLASS_NAME, "gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)
        try:
            shitty_element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "g-blk"))
            )
            self.browser.execute_script(
                """
            const shitty = arguments[0];
            shitty.parentElement.removeChild(shitty)
            """, 
                shitty_element
            )
        except Exception:
            pass
        search_results = self.browser.find_elements(By.CLASS_NAME, "g")
        for index, search_result in enumerate(search_results):
            class_name = search_result.get_attribute("class")
            title = search_result.find_element(By.TAG_NAME, "h3")
            if title.size['height'] != 0 and "liYKde" not in class_name:
                    search_result.screenshot(f"{self.screenshots_dir}/{self.keyword}x{index}.png")
    def finish(self):
        self.browser.quit()

domain_competitors = GoogleKeywordScreenshotter("finalcut", "screenshots")
domain_competitors.start()
domain_competitors.finish()
python_competitors = GoogleKeywordScreenshotter("python book", "screenshots")
python_competitors.start()
python_competitors.finish()