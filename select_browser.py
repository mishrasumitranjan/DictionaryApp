from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOpt
from selenium.webdriver.chrome.options import Options as ChromeOpt


def main():
    ...


def select_browser(option: int):
    """
    Takes an input number and returns a browser instance according to the selected number.
    Options:

    1 - Firefox

    2 - Firefox with Headless mode

    3 - Chrome

    4 - Chrome with Headless mode

    Defaults to Option 4 on detecting invalid entry.

    :param option: The number to select browser.
    :return: WebDriver: Returns Webdriver object based on user's choice.
    """

    try:
        if option not in [1, 2, 3, 4]:
            raise ValueError
    except ValueError:
        print("Not a valid option. Defaulting to option 4.")
        option = 4

    # Regular Firefox
    if option == 1:
        browser = webdriver.Firefox()
    # Headless Firefox
    elif option == 2:
        f_options = FirefoxOpt()
        f_options.headless = True
        browser = webdriver.Firefox(options=f_options)
    # Regular Chrome
    elif option == 3:
        browser = webdriver.Chrome()
    # Headless Chrome
    elif option == 4:
        c_options = ChromeOpt()
        c_options.headless = True
        browser = webdriver.Chrome(options=c_options)
    else:
        pass

    return browser


if __name__ == '__main()__':
    main()
