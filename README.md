# Python Website Opener

This simple Python project automatically opens multiple websites listed in a text file (Sites.txt) using your default web browser.

## How It Works  
When you run the script, it reads all the URLs stored in Sites.txt and opens each one in a new browser tab on your computer.

## Requirements  
- Python 3.x installed
- A file named Sites.txt in the same directory as the script (Each line in Sites.txt should contain one website link, for example: https://www.google.com)

## Usage  
1. Clone or download the repository.
2. Add your desired websites inside Sites.txt.
3. Run the script in your terminal:
   python3 main.py
4. The listed websites will open automatically in your default browser.

# Website Opener Script

This Python script opens multiple websites automatically by reading them from a text file or predefined configuration.

## 🔧 Current Features
- Opens a list of websites from `file.txt`
- Normalizes URLs (adds `http://` if missing)
- Opens each website in a new browser tab

## 🚀 Upcoming Update
I will add a function that prevents the script from opening websites that are already open.
For example, if you run the script for the code category but GitHub is already open in your browser, the script will detect this and will not open a duplicate tab.

## License  
This project is open-source and free to use." > README.md
