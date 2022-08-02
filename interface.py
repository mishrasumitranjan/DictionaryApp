import threading
import tkinter as tk

from select_browser import select_browser
from tkinter import Menu
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

# Dictionary imports
from oxford_learners import Oxford
from merriam_webster import MerriamWebster
from cambridge import Cambridge
from dictionary_dot_com import DictionaryDotCom
from macmillan import Macmillan


def main():
    root = tk.Tk()
    Interface(root, 4)
    root.mainloop()


class Interface:
    def __init__(self, window, browser_val):
        """
        Creates the entire interface.

        :param window: tkinter Tk object. window in which the interface will reside.
        :param browser_val: the option of the browser.
        """
        self.window = window
        self.browser_val = browser_val
        self.browser = None
        self.window.title("Your Online Dictionary")
        self.window.geometry("1200x600")
        self.window.resizable(False, False)

        self.sites = ["Oxford Learner's Dictionaries",
                      "Dictionary by Merriam-Webster",
                      "Cambridge Dictionary",
                      "Dictionary.com",
                      "Macmillan Dictionary"]

        # Creates the top menu bar.
        self.menubar = Menu(self.window)
        self.window.configure(menu=self.menubar)

        # Creates the File menu in menu bar.
        self.file_menu = Menu(self.menubar, tearoff=0)
        # self.file_menu.add_command(label="Something", command="")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.window.destroy)
        self.menubar.add_cascade(label="File", menu=self.file_menu)

        # Creates the Help menu in menu bar.
        self.help_menu = Menu(self.menubar, tearoff=0)
        self.help_menu.add_command(label="How to Use")
        self.menubar.add_cascade(label="Help", menu=self.help_menu)

        big_frame = tk.Frame(self.window, bg="#206080")
        big_frame.pack(fill="both", expand=True)

        frame_container1 = tk.Frame(self.window, bg="#206080")
        frame_container1.pack(fill="both", side="left")

        frame_container2 = tk.Frame(self.window, bg="#206080")
        frame_container2.pack(fill="both", side="right")

        frame1 = tk.Frame(frame_container1, bg="", )
        frame1.grid(row=0, column=0)

        frame2 = tk.Frame(frame_container1, bg="", )
        frame2.grid(row=1, column=0)

        frame3 = tk.Frame(frame_container1, bg="", )
        frame3.grid(row=2, column=0, rowspan=3)

        frame4 = tk.Frame(frame_container2, bg="", )
        frame4.grid(row=0, column=1, rowspan=10)

        label1 = tk.Canvas(frame1, bg="#206080", width=280, height=70, bd=0, highlightthickness=0)
        label1.create_text(72, 16, text="Select Website:", fill="white", font=("Calibri", 16, "bold"))
        label1.grid(row=0, column=0, padx=5, pady=20)

        self.service = tk.StringVar()
        self.service_selector = ttk.Combobox(label1, width=31, textvariable=self.service, state="readonly",
                                             values=self.sites,
                                             font=("Palatino Linotype", 12)
                                             )
        self.service_selector.current(0)
        self.service_selector.grid(row=0, column=0, pady=(30, 0), padx=5)

        self.window.option_add('*TCombobox*Listbox.font', ("Palatino Linotype", 12))

        label2 = tk.Canvas(frame2, bg="#206080", width=275, height=100, bd=0, highlightthickness=0)
        label2.create_text(65, 16, text="Search Word:", fill="white", font=("Calibri", 16, "bold"))
        label2.grid(row=0, column=0, padx=5, pady=20)

        self.search_word = tk.Entry(label2, width=33, font=("Palatino Linotype", 12, "bold"))
        self.search_word.grid(row=0, column=0, pady=(30, 0), padx=5)

        self.s_button = tk.Button(label2, width=22, text="Search", font=("Calibri", 16, "bold"), command=self.search_start)
        self.s_button.grid(row=1, column=0, padx=10, pady=10)

        label3 = tk.Canvas(frame3, bg="#206080", width=220, height=10, bd=0, highlightthickness=0)
        label3.create_text(85, 16, text="Word of the Day:", fill="white", font=("Calibri", 16, "bold"))
        label3.pack(fill="both")

        self.wotd_box = ScrolledText(label3, font=("Monotype Corsiva", 20, "bold"), state="disabled",
                                     width=20, height=8)
        self.wotd_box.grid(row=0, column=0, padx=(15, 11), pady=(30, 20))

        label4 = tk.Canvas(frame4, bg="#206080", width=840, height=600, bd=0, highlightthickness=0)
        label4.create_text(60, 16, text="Definition:", fill="white", font=("Calibri", 16, "bold"))
        label4.pack(fill="both", expand=True)

        self.defn_box = ScrolledText(label4, font=("Calibri", 16,), state="disabled", width=75, height=20)
        # self.defn_box.grid(row=1, column=0, padx=(10, 30), pady=(30, 30))
        self.defn_box.pack(side="left", padx=(22, 32), pady=(30, 40))
        self.window.bind('<Return>', self.search_start)

    def refresh(self):
        """
        Updates the window object every second. Used for running other operations simultaneously.

        :return: None
        """
        self.window.update()
        self.window.after(1000, self.refresh)

    def search_start(self):
        """
        Calls the refresh function and starts the search function in a new thread.

        :return: None
        """
        self.refresh()
        threading.Thread(target=self.search).start()

    def select_service(self):
        """
        Checks the value selected for dictionary service and returns a Class object accordingly.

        :return: Class instance of the selected service.
        """
        self.browser = select_browser(self.browser_val)
        d_site = str(self.service_selector.get())
        if d_site == self.sites[0]:
            return Oxford(self.browser)
        elif d_site == self.sites[1]:
            return MerriamWebster(self.browser)
        elif d_site == self.sites[2]:
            return Cambridge(self.browser)
        elif d_site == self.sites[3]:
            return DictionaryDotCom(self.browser)
        elif d_site == self.sites[4]:
            return Macmillan(self.browser)
        pass

    def search(self):
        """
        Calls methods for updating the Word of the day field and starts the search.

        :return: None
        """
        self.s_button.configure(state="disabled")
        o = self.select_service()
        o.go()
        self.update_wotd(o)
        self.update_results(o)
        self.browser.quit()
        self.s_button.configure(state="normal")

    def update_wotd(self, dict_object):
        """
        Looks for the word of the day and updates it in the respective field.

        :param dict_object: the class instance
        :return: None
        """
        wotd = dict_object.wotd.text
        self.wotd_box.configure(state="normal")
        self.wotd_box.delete(1.0, tk.END)
        self.wotd_box.insert(tk.INSERT, f"{wotd}")
        self.wotd_box.configure(state="disabled")

    def update_results(self, dict_object):
        """
        Looks for the word mentioned in the search field and enters it in the search field of the site.
        Clicks the search button and updates the results in the definition field.

        :param dict_object: the class instance
        :return: None
        """
        s = self.search_word.get()
        results = dict_object.search(s)
        self.defn_box.configure(state="normal")
        self.defn_box.delete('1.0', tk.END)
        for r in range(len(results)):
            self.defn_box.insert(tk.INSERT, f"- {results[r]}\n\n")
        self.defn_box.configure(state="disabled")


if __name__ == "__main__":
    main()
