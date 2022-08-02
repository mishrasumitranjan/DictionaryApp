from dictionary_site import DictionarySite
from select_browser import select_browser
from selenium.webdriver.common.by import By


class Macmillan(DictionarySite):
    url = "https://www.macmillandictionary.com/"
    wotd_locator = (By.XPATH, "//h2/a[contains(text(), 'Buzzword')]/"
                              "../following-sibling::div//a[contains(@class, 'word-link card-content-title')]")
    search_box_locator = (By.XPATH, "//div[@id='body']//input[@name='q']")
    search_button_locator = (By.XPATH, "//div[@id='body']//button[@class='search-submit']")
    defn_locator = (By.XPATH, "//span[@class='DEFINITION']")
    no_res_locator = (By.XPATH, "//div[@id='search-results']/h1")


def main():
    """
    Runs an instance of the Macmillan class. For testing purposes only.

    :return: None
    """
    browser = select_browser(1)
    m = Macmillan(browser)
    m.go()
    r = m.search("dsgd")
    for i in r:
        print(f"{i}")

    browser.quit()


if __name__ == "__main__":
    main()
