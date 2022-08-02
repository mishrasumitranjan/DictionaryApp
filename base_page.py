class BasePage(object):
    """
    Class containing some basic methods common to all pages.
    """

    url = None

    def __init__(self, driver):
        """
        Initializes the class and assigns the browser instance to a instance attribute.

        :param driver: Webdriver instance
        """
        self.driver = driver

    def go(self):
        """
        Navigates to the specified url.

        :return: None
        """
        self.driver.get(self.url)

    def refresh(self):
        """
        Refreshes the page.

        :return: None
        """
        self.driver.navigate().refresh()

    def forward(self):
        """
        Simulate Forward button

        :return: None
        """
        self.driver.navigate().forward()

    def back(self):
        """
        Simulate Back button

        :return: None
        """
        self.driver.navigate().back()

    @property
    def page_source(self):
        return self.driver.page_source