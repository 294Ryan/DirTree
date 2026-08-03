■[中文](#目錄樹工具)    ■[English](#dirtree)

# ***目錄樹工具***

## **目錄**
- [專案概述](#專案概述)
- [重點特色](#重點特色)
- [使用說明](#使用說明)
- [開發須知](#開發須知)
- [使用技術](#使用技術)
- [常見問題](#常見問題)
- [專案結構](#專案結構)
- [備註](#備註)

## **專案概述**
掃描指定目錄，輸出成樹狀結構文字，可依需求忽略隱藏檔案／資料夾，結果可直接複製到剪貼簿。

## **重點特色**
- **樹狀結構輸出**：以 `├─` `└─` 呈現目錄與檔案階層
- **隱藏項目過濾**：可分別選擇是否忽略隱藏資料夾與隱藏檔案，**預設為忽略（Enter 即確認）**
- **符號連結迴圈保護**：偵測到重複路徑會自動跳過，避免無限遞迴
- **權限錯誤處理**：遇到無法讀取的目錄會標註提示，不會中斷程式
- **一鍵複製**：掃描結果可直接複製到剪貼簿

## **使用說明**
請先下載本倉庫內容並將其解壓縮
- 啟動：執行 `.exe` 檔案，如 `main.exe`，或直接執行 `python main.py`
- 功能介紹：
1. 輸入目錄路徑：
    程式會驗證路徑是否為有效目錄，無效則重新輸入
2. 選擇是否忽略隱藏資料夾／隱藏檔案：
    輸入 `y` 或 `n`；直接按 `Enter` 預設為 `Y`（忽略）
3. 輸出目錄樹：
    掃描完成後於終端機顯示完整樹狀結構
4. 複製到剪貼簿：
    選擇 `y` 或按 `Enter` 即可複製，若裝置不支援剪貼簿存取會顯示警告

## **開發須知**
1. 請先閱讀以下開發須知並遵守所用條款。
2. 請運行已下指令複製此倉庫至您的本地電腦：
```
git clone https://github.com/294Ryan/DirTree.git
```
3. 使用語言：
   - Python 3.x
4. 安裝必要工具：
  - Python模組：請運行以下指令
    ```
    pip install -r requirements.txt
    ```
5. 使用技術：請參見[使用技術](#使用技術)
6. 專案結構：請參見[專案結構](#專案結構)

## **使用技術**
- **colorama**：處理跨平台終端機文字色彩（Windows/Linux/macOS 統一顯示）
- **pyperclip**：存取系統剪貼簿以複製掃描結果
- **pathlib**：處理路徑解析、遞迴讀取目錄項目
- **PyInstaller**：透過 `main.spec` 打包成獨立 `.exe` 執行檔

## **常見問題**
- **複製到剪貼簿失敗？**
  部分裝置或環境（如無圖形介面的伺服器）不支援剪貼簿存取，此時請手動複製終端機輸出內容。
- **目錄中有符號連結會怎樣？**
  程式會記錄已走訪過的路徑，若偵測到重複（迴圈）會自動跳過該連結，避免無限遞迴。
- **顯示「Permission denied」是什麼意思？**
  代表該目錄無讀取權限，程式會標註此訊息並跳過該目錄，繼續掃描其餘部分。

## **專案結構**
```
DirTree/
├─.gitignore
├─icon.ico
├─LICENSE
├─main.py
├─main.spec
├─README.md
└─requirements.txt
```

## **備註**
- 維護者: 294Ryan - [Github](https://github.com/294Ryan)
- [!] 本專案供教育研究使用，使用時請尊重所有版權與權利擁有者。
任何因不當使用造成的後果請自負。

---

# ***DirTree***

## **Table of Contents**
- [Overview](#overview)
- [Key Features](#key-features)
- [Usage](#usage)
- [Development Notes](#development-notes)
- [Tech Stack](#tech-stack)
- [FAQ](#faq)
- [Project Structure](#project-structure)
- [Notes](#notes)

## **Overview**
Scans a specified directory and outputs it as a tree structure. Hidden files/folders can be filtered out, and results can be copied straight to the clipboard.

## **Key Features**
- **Tree structure output**: renders hierarchy with `├─` `└─` connectors
- **Hidden item filtering**: choose separately whether to ignore hidden folders and hidden files; **defaults to Yes (press Enter to confirm)**
- **Symlink loop protection**: auto-skips already-visited paths to prevent infinite recursion
- **Permission error handling**: unreadable directories are flagged and skipped without crashing the program
- **One-click copy**: copy scan results directly to clipboard

## **Usage**
Download and extract this repository
- **Run**: execute the `.exe` file, e.g. `main.exe`, or run `python main.py` directly
- **Workflow**:
1. Enter a directory path:
    the program validates the path and re-prompts if it's invalid
2. Choose whether to ignore hidden folders / hidden files:
    enter `y` or `n`; pressing `Enter` defaults to `Y` (ignore)
3. View the directory tree:
    the full tree structure prints to the terminal once scanning finishes
4. Copy to clipboard:
    choose `y` or press `Enter` to copy; a warning appears if the device doesn't support clipboard access

## **Development Notes**
1. Read the notes below and follow the applicable terms first.
2. Clone this repository:
```
git clone https://github.com/294Ryan/DirTree.git
```
3. Language:
   - Python 3.x
4. Required tools:
  - Python modules: run
    ```
    pip install -r requirements.txt
    ```
5. Tech stack: see [Tech Stack](#tech-stack)
6. Project structure: see [Project Structure](#project-structure)

## **Tech Stack**
- **colorama**: cross-platform terminal color handling (consistent output on Windows/Linux/macOS)
- **pyperclip**: accesses the system clipboard to copy scan results
- **pathlib**: path resolution and recursive directory traversal
- **PyInstaller**: bundled into a standalone `.exe` via `main.spec`

## **FAQ**
- **Copy to clipboard fails?**
  Some devices/environments (e.g. headless servers) don't support clipboard access — copy the terminal output manually instead.
- **What happens with symlinks in the directory?**
  Visited paths are tracked; if a loop is detected, that symlink is skipped to avoid infinite recursion.
- **What does "Permission denied" mean?**
  The directory can't be read; the program flags it and continues scanning the rest.

## **Project Structure**
```
DirTree/
├─.gitignore
├─icon.ico
├─LICENSE
├─main.py
├─main.spec
├─README.md
└─requirements.txt
```

## **Notes**
- Maintainer: 294Ryan - [Github](https://github.com/294Ryan)
- [!] This project is for educational and research purposes only. Please respect all copyright and rights holders.
Any consequences resulting from misuse are the user's own responsibility.
