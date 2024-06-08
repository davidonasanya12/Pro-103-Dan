import os
import shutil
import time
import random 
import sys

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="C:/Users/thesl/OneDrive/Desktop/Daniel/Pro-103-Daniel/source"
destination="C:/Users/thesl/OneDrive/Desktop/Daniel/Pro-103-Daniel/destination"

dirtree={
    "Image_Files":[".gif",".png",".jpg"],
    "Video_Files":[".mp4",".mov",".avi"],
    "Document_Files":[".ppt",".txt",".csv"],
    "SetUp_Files":[".exe",".bin",".cmd"]
}

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_modified(self, event):
        print(f"Hey, {event.src_path} has been modified!")

    def on_moved(self, event):
        print(f"Hey, {event.src_path} has been moved to {event.dest_path}!")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")
   
event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopped by user")
    observer.stop()

observer.join()

   


