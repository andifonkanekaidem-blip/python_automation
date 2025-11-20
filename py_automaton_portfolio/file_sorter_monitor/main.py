import os
import time
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Folder to monitor
SOURCE_FOLDER =  r"C:\Users\USER\Desktop\T\New folder" #Input the actual folder you intend to monitor

# Simple logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
def move_file(src,dest,retries=3,delay=1):
    for _ in range(retries):
        try:
            if os.path.isfile(src):
                shutil.move(src,dest)
                return True
        except PermissionError:
            time.sleep(delay)
    logging.info(f"File {src} in use")
    return False
class FileSorter(FileSystemEventHandler):
    """Sort files into folders based on extension when they are created."""

    def on_created(self, event):
        if event.is_directory:
            return
        self.sort(event.src_path)

    def sort(self, file_path):
        if not os.path.exists(file_path):
            logging.warning(f"Skipped missing file: {file_path}")
            return

        file_name = os.path.basename(file_path)
        ext = os.path.splitext(file_name)[1][1:].strip() or "Others"
        dest_folder = os.path.join(SOURCE_FOLDER, ext)

        try:
            os.makedirs(dest_folder, exist_ok=True)
        except Exception as e:
            logging.error(f"Could not create folder {dest_folder}: {e}")
            return

        try:
            move_file(file_path,os.path.join(dest_folder, file_name))
            logging.info(f"Moved {file_name} to {dest_folder}")
        except Exception as e:
            logging.error(f"Could not move {file_name}: {e}")


if __name__ == "__main__":
    event_handler = FileSorter()
    observer = Observer()

    try:
        observer.schedule(event_handler, SOURCE_FOLDER, recursive=False)
        observer.start()
        logging.info(f"Monitoring {SOURCE_FOLDER}...")
    except Exception as e:
        logging.error(f"Failed to start observer: {e}")
        exit(1)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Stopping...")
        observer.stop()
    observer.join()
    logging.info("Observer stopped. Exiting.")