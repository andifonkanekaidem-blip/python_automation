\# Folder File Sorter



A simple Python script that monitors a folder on Windows 11 and automatically sorts new files into subfolders based on their file extensions.



---



\## Features



\- Monitors a folder in real-time using `watchdog`.

\- Automatically moves files into folders named after their extensions.

\- Files without extensions go into an `Others` folder.

\- Handles basic errors like missing files or permission issues.

\- Clean, beginner-friendly, and easy to extend.



---



\## Requirements



\- Python 3.x

\- `watchdog` library



Install with pip:



```bash

pip install watchdog





---



Usage



1\. Update the folder path in the script if needed:







SOURCE\_FOLDER = os.path.join(os.environ\["USERPROFILE"], "Documents", "my work")



2\. Run the script:







python file\_sorter.py



3\. The script runs continuously:



New files are automatically moved into subfolders.



Press Ctrl+C to stop safely.











---



Example



Before running the script:



my work/

├── report.docx

├── image.png

├── notes.txt

├── invoice.pdf



After running:



my work/

├── docx/

│   └── report.docx

├── png/

│   └── image.png

├── txt/

│   └── notes.txt

├── pdf/

│   └── invoice.pdf

├── Others/

│   └── README





---



How It Works



Monitoring: watchdog.Observer runs a background thread to detect new files.



Sorting: When a new file appears, the script checks its extension and moves it to the corresponding folder.



Error Handling: Catches common issues like missing files, permission errors, or locked files.







---



Why This Project



Demonstrates real-time automation in Python.



Shows event-driven programming and using external libraries.



Clean and professional code, perfect for a portfolio.







---



License



Open-source, free to use.



---

