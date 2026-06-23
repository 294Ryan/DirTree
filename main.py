import sys
import os.path
import pyperclip as pc
from pathlib import Path
from colorama import init, Fore, Back

class TextTheme:
    ERROR       = Back.RESET + Fore.LIGHTRED_EX
    WARNING     = Back.RESET + Fore.YELLOW
    INFO        = Back.RESET + Fore.LIGHTBLACK_EX
    APP_TITLE   = Back.RESET + Fore.CYAN
    PROMPT      = Back.RESET + Fore.LIGHTBLACK_EX
    INPUT       = Back.RESET + Fore.CYAN
    NONE        = Back.RESET + Fore.RESET


def showInfo(msg):
    printMsg = f"\n[Info] {msg}"
    print(TextTheme.INFO + printMsg)

def showWarning(msg):
    printMsg = f"\n[Warning] {msg}"
    print(TextTheme.WARNING + printMsg)

def showError(msg):
    printMsg = f"\n[Error] {msg}"
    print(TextTheme.ERROR + printMsg)

def firstPage():
    print(TextTheme.APP_TITLE + "<< Directory Walker >>")
    print(TextTheme.PROMPT + 
"""\n
- Product: Directory Walker
- Function: A tool used to scan a specified directory and output the results as a tree structure.
- Version: v1.0.0
- Developer: 294Ryan
""")

def getInput():
    temp = input(TextTheme.INPUT + ">>")
    return temp

def p(arg):
    print(TextTheme.NONE + arg, end = "")
    return arg

def newLine():
    print(TextTheme.NONE + "")
    return "\n"

def printTree(oPath, prefix=""):
    """ ├ │ └ ─ """
    global fullTree
    fullPath = oPath.resolve()
    files = sorted([x for x in oPath.iterdir() if x.is_file()])
    dirs = sorted([x for x in oPath.iterdir() if x.is_dir()])    
    
    fullTree += p(fullPath.name)
    fullTree += p(r"/")
    fullTree += newLine()
    
    items = dirs + files
    total = len(items)
    
    for idx, item in enumerate(items):
        isLast = idx == total - 1
        fullTree += p(prefix)
        fullTree += p("└─" if isLast else "├─")
        childPrefix = prefix + ("   " if isLast else "│  ")
        if item.is_dir():
            printTree(item, childPrefix)
        else:
            fullTree += p(item.name)
            fullTree += newLine()
    
def main():
    global fullTree
    init()
    firstPage()
    
    while True:
        print(TextTheme.INPUT + "Enter a directory path")
        path = Path(getInput())
        if path.is_dir():
            break
        else:
            showError(f'Path "{path.resolve()}" is not a directory.')
    
    print(TextTheme.PROMPT + "\nDirectory tree: \n")
    fullTree = ""
    printTree(path)
    showInfo("Directory scaned.")
    
    while True:
        print(TextTheme.INPUT + "\nWould you like to copy this directory tree to the clipboard? (y/n)?")
        _input = getInput()
        if len(_input) == 1 and _input.lower() in ["y", "n"]:
            if _input.lower() == "y":
                try:
                    pc.copy(fullTree)
                    showInfo("Copied.")
                except:
                    showWarning("Copy failed. Your device may not support clipboard access. Please copy it manually.")
            break
    
    input(TextTheme.PROMPT + "\nPress [Enter] to exit.")
    sys.exit()
    
if __name__ == "__main__":
    main()
