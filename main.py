import sys
import os
import os.path
import tkinter.messagebox as tkm
from colorama import init, Fore, Back, Style

class TextTheme:
    ERROR       = Back.RESET + Fore.LIGHTRED_EX
    INFO        = Back.RESET + Fore.CYAN
    WARNING     = Back.RESET + Fore.YELLOW
    APP_TITLE   = Back.RESET + Fore.BLUE
    PROMPT      = Back.RESET + Fore.LIGHTBLACK_EX
    INPUT       = Back.RESET + Fore.CYAN
    OUTPUT      = Back.RESET + Fore.WHITE
    USER_LABEL  = Back.LIGHTBLUE_EX + Fore.BLACK
    NONE        = Back.RESET + Fore.RESET
    HELP        = Back.RESET + Fore.LIGHTBLACK_EX


def resourcePath(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def showInfo(msg, msgboxTitle = ""):
    printMsg = f"\n[Info] {msg}"
    print(TextTheme.INFO + printMsg)
    if msgboxTitle:
        tkm.showinfo(msgboxTitle, printMsg)

def showWarning(msg, msgboxTitle = ""):
    printMsg = f"\n[Warning] {msg}"
    print(TextTheme.WARNING + printMsg)
    if msgboxTitle:
        tkm.showwarning(msgboxTitle, printMsg)

def showError(msg, msgboxTitle = ""):
    printMsg = f"\n[Error] {msg}"
    print(TextTheme.ERROR + printMsg)
    if msgboxTitle:
        tkm.showerror(msgboxTitle, printMsg)

def firstPage():
    print(TextTheme.APP_TITLE + "<< Directory Walker >>")
    print(TextTheme.PROMPT + 
"""\n
-Product: Directory Walker
-Function: A tool used to scan a specified directory and output the results as a tree structure.
-Version: v1.0.0
-Developer: 294Ryan
""")

def main():
    init()
    firstPage()




if __name__ == "__main__":
    main()