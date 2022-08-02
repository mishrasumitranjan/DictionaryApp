import tkinter as tk

from interface import Interface


def main():
    root = tk.Tk()
    Interface(root, 3)
    # The argument '3' in the above line is used to specify the browser being used.
    # 1 is Firefox, 2 is Firefox in Headless mode, 3 is Chrome, and 4 is Chrome in Headless mode.
    # Change this value to test other options.
    root.mainloop()


if __name__ == "__main__":
    main()