import csv
import os
import zipfile
from zipfile import ZipFile

def unzipFile(fileName):
    archiveDir = r"\\localhost\Prod_Archive"
    outputDir = r"\\localhost\outputdir"
    print "fileName: ", fileName[:-4] # File name is .zip stripped.
    for f in os.listdir(d):
        fullpath = os.path.join(d, f)
        if f[:-4] == fileName[:-4]:
            # Log file found
            logfile = open('files_processed.txt', 'w+')
            logfile.write("{0} - FOUND".format(f))
            # Unzip file
            zipfile = ZipFile(fullpath)
            print "extracting file: %s" % f
            zipfile.extractall(output)
            print "file moved to output"
            
            logfile.close()
            
    
    
# CSV file of filenames to be searched and unzipped.
with open(r"C:\Users\bob\Desktop\PDFFileNames.csv", 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        #Unzip the file
        print "row", row
        unzipFile(row[0])

