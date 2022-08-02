from base_element import BaseElement
from dictionary_site import DictionarySite
from select_browser import select_browser

from selenium.webdriver.common.by import By


class Oxford(DictionarySite):
    url = "https://www.oxfordlearnersdictionaries.com/"
    wotd_locator = (By.XPATH, "//div[contains(@class, 'wotd-box')]/a[@class='headword']")
    search_box_locator = (By.XPATH, "//input[@id='q']")
    search_button_locator = (By.XPATH, "//label[@id='search-btn']/input")
    defn_locator = (By.XPATH, "//div[@class='entry']/ol//span[@class='def']")
    no_res_locator = (By.XPATH, "//div[@id='search-results']")


def main():
    """
    Runs an instance of the Oxford class. For testing purposes only.

    :return: None
    """
    query = input("Enter word to search: ").strip()
    browser = select_browser(1)
    o = Oxford(browser)
    o.go()
    print(o.wotd.text)
    results = o.search(query)
    for r in results:
        print(r)
    browser.quit()


if __name__ == "__main__":
    main()
