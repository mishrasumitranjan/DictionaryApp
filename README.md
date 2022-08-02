# DictionaryApp

#### Description:

This project is a GUI application that can be used to search for the definition
of a  word in any of the five online dictionary services provided inside.

The application uses Tkinter for the UI part and Selenium to navigate through
the sites and  display the results. By default the application uses Chrome
in headless mode to perform the task. This can be changed by changing
an argument passed to the Interface class in the `main.py` file (See the
file for more information).

It has been designed using the Page-Object model and the files
`base_element.py` and `base_page.py` contain the base classes in use.
The `dictionary_site.py` file inherits the `BasePage` class from `base_page.py`
and adds common methods that can be used in all of the dictionary services
used in the application.

The application is capable of displaying results from the following sites:
- Oxford Learner's Dictionaries (https://www.oxfordlearnersdictionaries.com/)
- Dictionary by Merriam-Webster (https://www.merriam-webster.com/)
- Cambridge Dictionary (https://dictionary.cambridge.org/)
- Dictionary.com (https://www.dictionary.com/)
- Macmillan Dictionary (https://www.macmillandictionary.com/)