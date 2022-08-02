from base_element import BaseElement
from base_page import BasePage
from selenium.webdriver.common.by import By


class DictionarySite(BasePage):
    wotd_locator = ()
    search_box_locator = ()
    search_button_locator = ()
    defn_locator = ()
    no_res_locator = ()

    @property
    def wotd(self):
        return BaseElement(self.driver, *self.wotd_locator)

    @property
    def search_box(self):
        return BaseElement(self.driver, *self.search_box_locator)

    @property
    def search_button(self):
        return BaseElement(self.driver, *self.search_button_locator)

    @property
    def defn(self):
        return BaseElement(self.driver, *self.defn_locator).locate_all()

    @property
    def no_res(self):
        return BaseElement(self.driver, *self.no_res_locator)

    def search(self, query):
        """
        Takes a query as argument and returns the result as a list of strings.
        :param query: string.
        :return: list of strings
        """
        self.search_box.type(query)
        self.search_button.click()
        results = []
        if len(self.defn) > 0:
            for r in self.defn:
                results.append(r.text)
            return results
        else:
            return [self.no_res.text]
