HERE I WILL B E ANNOTATING THE BUILDING PROCESS AND WHAT THE THINKING WAS

Goal: When I download an image or video, it should be sent to it's own folder.

How I should I achieve this?

1. Need a way for our python code to access files in our computer.
2. Google it!
3. Import os library. The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.
4. the github repo for the OS library https://github.com/python/cpython/blob/3.10/Lib/os.py
5. .scandir() method to return list of the files in that folder
6. create a for loop on the entries list, printing the names.

```
with os.scandir(source_dir) as entries:
    for entry in entries:
    print(entry.name)
```

7. Next step is to do something whenever a file is added. Google search it, and we end up finding an API library watchdog.
8. pip3 install watchdog. Its a Python API library and shell utilities to monitor file system events.
9. To figure it out run with the Quickstart option within the link:

```
The following example program will monitor the current directory recursively for file system changes and simply log them to the console:
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```

10. Google how to move files throuh directories, and end up finding the shutil module. https://docs.python.org/3/library/shutil.html
11. Follow Documentation of Code in fileAutomation.py
12. Can be ran in the terminal by actually changing to the directory and running python3. THIS MUST BE CHANGED
13. Lets create a .bash script instead that can automate the process of changing directories and running the python3 command.
