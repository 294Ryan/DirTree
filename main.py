import sys
import os
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
    print(TextTheme.APP_TITLE + 
r"""
 ____  _     _____              
|  _ \(_)_ _|_   _| __ ___  ___ 
| | | | | '__|| || '__/ _ \/ _ \
| |_| | | |   | || | |  __/  __/
|____/|_|_|   |_||_|  \___|\___|

""")
    print(TextTheme.PROMPT + 
"""\n
* Name     : DirTree
* Function : A tool used to scan a specified directory and output the results as a tree structure.
* Version  : v1.0.0
* Developer: 294Ryan
""")

def getInput(prompt = ""):
    temp = input(TextTheme.INPUT + f"{prompt}\n>> ").strip()
    return temp

def p(arg):
    print(TextTheme.NONE + arg, end = "")
    return arg

def newLine():
    print(TextTheme.NONE + "")
    return "\n"

def printTree(oPath, treeNow:str, ignoreHiddenDir:bool, ignoreHiddenFile:bool, prefix:str="", visited = None):
    """ ├ │ └ ─ """

    if visited is None:
        visited = set()

    fullPath = oPath.resolve()
    
    treeNow += p(fullPath.name)
    treeNow += p(r"/")

    # symlink check
    if fullPath in visited:
        treeNow += p("  [Skip this symlink]  ")
        treeNow += newLine()
        return treeNow
    visited.add(fullPath)

    # catch PermissionError
    try:
        entries = list(oPath.iterdir())
        files = sorted(x for x in entries if x.is_file())
        if ignoreHiddenFile:
            files = [x for x in files if not x.name.startswith(".")]
        dirs = sorted(x for x in entries if x.is_dir())
        if ignoreHiddenDir:
            dirs = [x for x in dirs if not x.name.startswith(".")]
    
    except OSError:
        treeNow += p(f"  [Cannot read this directory. Permission denied]  ")
        treeNow += newLine()
        return treeNow
    
    treeNow += newLine()
    
    items = dirs + files
    total = len(items)
    
    for idx, item in enumerate(items):
        isLast = idx == total - 1
        treeNow += p(prefix)
        treeNow += p("└─" if isLast else "├─")
        childPrefix = prefix + ("   " if isLast else "│  ")
        if item.is_dir():
            treeNow = printTree(item, treeNow, ignoreHiddenDir, ignoreHiddenFile, childPrefix, visited)
        else:
            treeNow += p(item.name)
            treeNow += newLine()
    
    return treeNow
    
def main():
    os.system("cls" if os.name == "nt" else "clear")
    init()
    firstPage()
    
    while True:
        path = Path(getInput("Enter a directory path"))
        if path.is_dir():
            break
        else:
            showError(f'Path "{path.resolve()}" is not a directory.')
    
    ignoreHiddenDir = None
    while ignoreHiddenDir == None:
        _input = getInput('Ignore hidden directories? (Directories starting with ".") [Y/n]')
        if _input.lower() == "y" or _input == "":
            ignoreHiddenDir = True
            break
        elif _input.lower() == "n":
            ignoreHiddenDir = False

    ignoreHiddenFile = None
    while ignoreHiddenFile == None:
        _input = getInput('Ignore hidden files? (Files starting with ".") [Y/n]')
        if _input.lower() == "y" or _input == "":
            ignoreHiddenFile = True
            break
        elif _input.lower() == "n":
            ignoreHiddenFile = False


    print(TextTheme.PROMPT + "\nDirectory tree: \n")
    fullTree = printTree(path, "", ignoreHiddenDir, ignoreHiddenFile)
    showInfo("Directory scaned.")


    _input = None
    while _input == None:
        _input = getInput('Ignore hidden files? (Files starting with ".") [Y/n]')
        if _input.lower() == "y"  or _input == "":
            try:
                pc.copy(fullTree)
                showInfo("Copied.")
            except:
                showWarning("Copy failed. Your device may not support clipboard access. Please copy it manually.")
            break
        elif _input.lower() == "n":
            break

    
    input(TextTheme.PROMPT + "\nPress [Enter] to exit.")
    sys.exit()
    
if __name__ == "__main__":
    main()
