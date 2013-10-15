today = datetime.date.today()
now = time()
f = strftime("FileList.%Y%m%d.%H%M%S.txt")
minutes = 10
dlist = [r"\\localhost\example",
         r"\\localhost\example2"]
outputDir = r"\\localhost\outputdata"
logfile = open(os.path.join(outputDir, f), "w+")
for d in dlist:
   path = os.listdir(d)
   for files in path:
       fullpath = os.path.join(d, files)
       if os.path.isfile(fullpath):
           #print files
           timediff = (now - os.path.getmtime(fullpath))/60
           if timediff < minutes: # Newer than x minutes.
               print "file: {0}\t{1}".format(files, timediff)
               logfile.write(files + '\n')
logfile.close()
