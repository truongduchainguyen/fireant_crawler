from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.webdriver import WebDriver

def check_exists_by_css_selector(webdriver: WebDriver, css_selector: str):
    flag = False
    text = ""
    try:
        text = webdriver.find_element(By.CSS_SELECTOR, css_selector + " > a").text
    except NoSuchElementException:
        flag = False
    print(text)
    if "Thêm" in text:
        flag = True
    return flag

driver = webdriver.Firefox()
url = "https://fireant.vn/cong-dong/moi-nhat"
driver.get(url)

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # button_css_selector = "#postList > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(3) > div > div.overflow-x-hidden.leading-7 > a"

    # only_button_css_selector = "div.overflow-x-hidden.leading-7 > a"
    # is_existed = check_exists_by_css_selector(webdriver=driver, css_selector=button_css_selector)
    # if is_existed:
    #     source.find_element(By.CSS_SELECTOR, only_button_css_selector).click()
    # print(len(source))
    # for i in range(len(source)):
    #     print("Inner loop at index: ", i)
    #     print(source[i].text)
    # print(source.find_element(By.CSS_SELECTOR, "div.overflow-x-hidden.leading-7").text)
    # Scroll down to the bottom
    # a.cursor-pointer

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait for page to load
    time.sleep(2)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
# //*[@id="postList"]/div[1]/div/div[2]/div[1]/div/div[2]

only_text = "#postList > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(1) > div > div.overflow-x-hidden.leading-7"
# source = driver.find_elements(By.CSS_SELECTOR, "#postList > div:nth-child(1) > div > div:nth-child(2)")
source = driver.find_elements(By.CSS_SELECTOR, only_text)
print(len(source))
# formatted_html = bs(source).prettify()
# with open("main.html", "w") as f:
#     f.write(formatted_html)
driver.close()
