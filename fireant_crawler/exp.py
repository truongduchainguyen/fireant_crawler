from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import InvalidArgumentException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Crawler:
    def __init__(self):
        self.driver = None

    def init_browser(self):
        pass

    def close_browser(self) -> None:
        self.driver.quit()

    def find_element_by_css_selector(self, obj: WebElement | WebDriver, selector: str) -> WebElement | None:
        element = None
        try:
            element = obj.find_element(By.CSS_SELECTOR, selector)
        except NoSuchElementException:
            print("No suitable element found")

        return element

    def get_all_data_in_tag(self, webelement: WebElement) -> str:
        text = webelement.text
        elem = webelement.find_element(By.CSS_SELECTOR, "a.cursor-pointer")
        try:
            time.sleep(2)
            text = elem.text
        except NoSuchElementException:
            return text

        if "Thêm".encode("utf-8") in text.encode("utf-8"):
            time.sleep(2)
            driver.execute_script("arguments[0].click();", elem)
            return text
        return text

    def crawl(self):
        pass


def get_all_data_in_tag(webelement: WebElement) -> str:
    result = ""
    try:
        result += webelement.text
    except InvalidArgumentException:
        return result

    try:
        elem = webelement.find_element(By.CSS_SELECTOR, "a.cursor-pointer")
    except NoSuchElementException:
        return result

    time.sleep(2)
    attempt = 3
    while attempt > 0:
        try:
            result += elem.text
        except StaleElementReferenceException:
            attempt -= 1
            continue
        return result

    attempt = 3
    if "Thêm".encode("utf-8") in result.encode("utf-8"):
        time.sleep(2)
        attempt = 3
        while attempt > 0:
            try:
                driver.execute_script("arguments[0].click();", elem)
                result += elem.text
            except StaleElementReferenceException:
                attempt -= 1
        return result

    return result


options = webdriver.FirefoxOptions()
options.add_argument("--no-sandbox")
options.set_preference("detach", True)
driver = webdriver.Firefox(options=options)
url = "https://fireant.vn/cong-dong/moi-nhat"
driver.get(url)
result = []

wait = WebDriverWait(driver, 20)

last_height = driver.execute_script("return document.body.scrollHeight")
popup_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Để sau')]")))
popup_btn.click()
while True:
    parent_selector = "#postList > div:nth-child(1) > div > div:nth-child(2)"
    parent = driver.find_element(By.CSS_SELECTOR, parent_selector)
    for idx in range(1, 4):
        attempt = 3
        while attempt > 0:
            tmp = {}
            selector_str = f"div:nth-child({idx}) > div > div.overflow-x-hidden.leading-7"
            try:
                child = parent.find_element(By.CSS_SELECTOR, selector_str)
            except (StaleElementReferenceException, NoSuchElementException) as err:
                if "Unable to locate element" in str(err):
                    attempt = 0
                else:
                    attempt -= 1
                continue
            text = get_all_data_in_tag(child)
            tmp["comment"] = text
            print(tmp)
            result.append(tmp)
            attempt = 0

    print(len(result))
    print("Next page")
    print("---------------------------------------")
    # Scroll down to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait for page to load
    time.sleep(2)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break
    last_height = new_height

driver.close()
