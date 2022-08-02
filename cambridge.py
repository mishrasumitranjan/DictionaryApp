import datetime
import time

from dictionary_site import DictionarySite
from selenium import webdriver
from selenium.webdriver.common.by import By


class Cambridge(DictionarySite):
    url = "https://dictionary.cambridge.org/"
    wotd_locator = (By.XPATH, "//p[contains(text(),'Word of the Day')]/following-sibling::p/a")
    search_box_locator = (By.ID, "searchword")
    search_button_locator = (By.XPATH, "//button[@title='Search']")
    defn_locator = (By.XPATH, "//div[contains(@class,'pr dsense ')]//div[@class='def ddef_d db']")
    no_res_locator = (By.XPATH, "//h1[@class='lpb-10 lbb']")


def main():
    """
    Runs an instance of the Cambridge class. For testing purposes only.

    :return: None
    """
    start = datetime.datetime.now()
    driver = webdriver.Firefox()
    finish = datetime.datetime.now()
    print(finish - start)
    c = Cambridge(driver)
    c.go()
    print(c.wotd.text)
    for r in c.search("port"):
        print(f"{r}")
    time.sleep(3)
    driver.quit()


if __name__ == "__main__":
    main()
