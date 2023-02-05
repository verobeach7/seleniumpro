from selenium import webdriver # web driver는 브라우저 컨트롤에 사용
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("https://google.com")