import os
import shutil
import time

path = input("Enter the path of folder to delete: ")
days = 30
seconds = time.time() - (days * 24 * 60 * 60)
path = path + "/"

list_of_files = os.listdir(path)

def file_time(path):
	ctime = os.stat(path).st_ctime
	return ctime


if os.path.exists(path):
    for file in list_of_files:
        if seconds >= file_time(path):
            os.remove(path + file)
            print("Files deleted successfully!")

        else:
            print("File exists less than 30 days. Enter a file path that exists more than 30 days.")
else:
    print("Entered path does not exist")