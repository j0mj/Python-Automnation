import os

source_dir = "/Users/jordan/Downloads"

with os.scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)

