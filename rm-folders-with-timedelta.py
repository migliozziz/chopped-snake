import datetime
import os
import shutil
import re

#Set a base Dir
basedir = r"\\localhost\d$"


for dirpath, dirnames, filenames in os.walk(basedir):
   for d in dirnames:
      curpath = os.path.join(dirpath, d)
      dir_modified = datetime.datetime.fromtimestamp(os.path.getmtime(curpath))

      # Conditional set to remove folders recursively older than 90 days.
      if datetime.datetime.now() - dir_modified > datetime.timedelta(days=90):          
          shutil.rmtree(curpath)
