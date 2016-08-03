import os
import zipfile
import ntpath
import datetime
from time import time

#basedir = r"C:\test\ziptest"
basedir = r"X:\C"

today = datetime.date.today()
now = time()
days = 365 * 3


"""
Zips qualified files.
"""
def zipit(originalFile):
    try:                        
        print "Zipping " + originalFile
        zippedFile = originalFile + ".zip"
        with zipfile.ZipFile(zippedFile, 'w', zipfile.ZIP_DEFLATED,
                             allowZip64=True) as myzip:
            myzip.write(originalFile, path_leaf(originalFile))
        return True
    except:
        print "An error has occurred, keeping original file."
        return False
    
"""
Unzips qualified files.
"""
def unzipit(zippedFile, d):
    try:                        
        print "UnZipping " + zippedFile
        z = zipfile.ZipFile(zippedFile)
        fName, fExt = os.path.splitext(os.path.join(root,f))
        z.extractall(d)
        return True
    except:
        print "An error has occurred, keeping original file."
        return False

"""
Returns filename.
"""
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

"""
File Cleanup
"""
def cleanup(filePath):
    if os.path.isfile(filePath):
        os.remove(filePath)
        print "Removed " + filePath


        

if __name__ == "__main__":
    for root, dirs, files in os.walk(basedir):
        for f in files:
            fName, fExt = os.path.splitext(os.path.join(root,f))
            timediff = (now - os.path.getmtime(os.path.join(root,f)))/86400
##            if fExt != ".zip":
##                ##print fExt
##                print(os.path.join(root,f))
##                if zipit(os.path.join(root,f)):
##                    cleanup(os.path.join(root,f))
            if fExt == ".zip":
                if unzipit(os.path.join(root,f), root):
                    cleanup(os.path.join(root,f))    
                
                    
        
