from dictionary_site import DictionarySite
from selenium import webdriver
from selenium.webdriver.common.by import By


def process(definitions):
    for i in range(len(definitions)):
        definitions[i] = definitions[i].replace(":", "").strip()


class MerriamWebster(DictionarySite):
    url = "https://www.merriam-webster.com/"
    wotd_locator = (By.XPATH, "//div[@class='wotd-promo__body']//a[@class='header-wht']")
    search_box_locator = (By.XPATH, "//input[@id='s-term']")
    search_button_locator = (By.XPATH, "//span[@class='search-icon']")
    defn_locator = (By.XPATH, "//span[@class='dtText']")       # text()[not(parent::strong)]
    no_res_locator = (By.XPATH, "//p[@class='spelling-suggestion-text']")

    def search(self, term):
        results = super().search(term)
        process(results)
        return results


def main():
    """
    Runs an instance of the MerriamWebster class. For testing purposes only.

    :return: None
    """
    driver = webdriver.Firefox()
    m = MerriamWebster(driver)
    m.go()
    print(m.wotd.text)
    r = m.search("port")
    for i in r:
        print(f"{i}")
    driver.quit()


if __name__ == "__main__":
    main()
