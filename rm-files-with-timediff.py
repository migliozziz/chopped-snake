# Remove files in listed directories older than X days.

import datetime
import os
from time import time

today = datetime.date.today()
now = time()
days = 1
dlist = [r"\\localhost\d$\folder1",
         r"\\localhost\d$\folder2"]

for d in dlist:
    path = os.listdir(d)
    for files in path:
        fullpath = os.path.join(d, files)
        if os.path.isfile(fullpath):
            timediff = (now - os.path.getmtime(full))/86400
            if timediff > days:    # Older than x days.
                os.remove(fullpath)
