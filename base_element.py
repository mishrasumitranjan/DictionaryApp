import selenium.webdriver.support.expected_conditions as ec
import selenium.common.exceptions as exc

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement:
    """
    Base class for web elements. Contains methods for handling actions related to web elements.
    """
    def __init__(self, *args):
        """
        Constructor for BaseElement class.

        Parameters:
                    driver: webdriver instance

                    element: WebElement

        -OR-

        Parameters:
                    driver: webdriver instance

                    by: By class object from 'selenium.webdriver.common.by'

                    value: string. Used to locate the element.

        :param args: list  of arguments to pass. Refer to above description.
        """
        if len(args) == 2:
            self.driver = args[0]
            self.element = args[1]
            self.locator = None
            self.by = None
            self.value = None
        elif len(args) == 3:
            self.element = None
            self.driver = args[0]
            self.by = args[1]
            self.value = args[2]
            self.locator = (self.by, self.value)
            self.locate()
        else:
            raise IndexError("Invalid Arguments")

    def locate(self):
        """
        Locates the element according to arguments provided if element is located using By class.
        Returns True is element is found. Else returns false.

        :return: bool
        """
        try:
            self.element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.locator))
        except exc.TimeoutException:
            return False
        else:
            return True

    def locate_all(self):
        """
        Creates a list of all elements located using the locators provided and returns a list of
        BaseElement instances of the located elements.

        :return: list of BaseElement instances
        """
        stack = self.driver.find_elements(self.by, self.value)
        elements = [BaseElement(self.driver, element) for element in stack]
        return elements

    def click(self):
        """
        Clicks the element.

        :return: None
        """
        # self.element = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.locator))
        self.element.click()

    @property
    def text(self):
        return self.element.text

    def type(self, txt):
        """
        Types in the provided argument into the element.

        :param txt: string. Text to be typed.
        :return: None
        """
        # self.locate()
        self.element.send_keys(txt)

    def attribute(self, attr_name):
        """
        Retrieves the value of the attribute provided as argument.

        :param attr_name: string. Name of the attribute to retrieve
        :return: string
        """
        attribute = self.element.get_attribute(attr_name)
        return attribute

    def child(self, by, value):
        """
        Locates a child element based on 'by' and 'value' attributes.
        Creates a new BaseElement object of the child element and returns it.

        :param by: By class object from 'selenium.webdriver.common.by'
        :param value: string. Used to locate the child element.
        :return: BaseElement object.
        """
        child_node = self.element.find_element(by, value)
        child_element = BaseElement(self.driver, child_node)
        return child_element

    def scroll(self, scroll_x, scroll_y):
        """
        Scrolls the page to the specified scroll position.
        Untested and likely not working.

        :param scroll_x:
        :param scroll_y:
        :return: None
        """
        ActionChains(self.driver).scroll_by_amount(scroll_x, scroll_y).perform()

    def move_to_element(self):
        """
        Scrolls the page till the element is comes into view.

        :return: None
        """
        # ActionChains(self.driver).scroll_to_element(self.element).perform()
        self.driver.execute_script("arguments[0].scrollIntoView();", self.element)