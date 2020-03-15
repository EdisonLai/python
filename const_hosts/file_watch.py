#authut: edison Lai
#mail: edison@cstrail.com

import sys
import pyinotify
import file_lib
from My_event import MyEvent

def main(path):
    original_contents = file_lib.read_file_as_str("/etc/hosts")

    wm = pyinotify.WatchManager()
    ev = MyEvent(path, original_contents)

    notifier = pyinotify.Notifier(wm, ev)
    wm.add_watch(path, pyinotify.ALL_EVENTS, rec = True)
    notifier.loop()

if __name__ == "__main__":
    path = "/etc"
    main(path)

