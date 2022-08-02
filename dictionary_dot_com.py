from dictionary_site import DictionarySite
from select_browser import select_browser
from selenium.webdriver.common.by import By


class DictionaryDotCom(DictionarySite):
    url = "https://www.dictionary.com/"
    wotd_locator = (By.XPATH, "//a[@data-linkid='nx1fkx']")
    search_box_locator = (By.ID, "globalSearch")
    search_button_locator = (By.XPATH, "//button[@aria-label='search']")
    defn_locator = (By.XPATH, "//div[contains(@class,'css-') and @value]")
    no_res_locator = (By.XPATH, "//span[contains(@class,'no-results-title')]")


def main():
    """
    Runs an instance of the DictionaryDotCom class. For testing purposes only.

    :return: None
    """
    browser = select_browser(1)
    m = DictionaryDotCom(browser)
    m.go()
    r = m.search("port")
    for i in r:
        print(f"{i}")

    browser.quit()


if __name__ == "__main__":
    main()