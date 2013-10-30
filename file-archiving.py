from datetime import datetime, timedelta
import os
import shutil
from zipfile import ZipFile, BadZipfile


class Archive:
    def __init__(self, sourceDir, outputDir, stagingDir):
        self.sourceDir = sourceDir
        self.outputDir = outputDir
        self.stagingDir = stagingDir
        self.extension = ".zip"

    def main(self):
        eligible = self.collectEligibleFileList()
        archived = self.compressFile(eligible)
        self.removeArchived(archived)
        self._sendToArchive()
        
        return

    """
    Find files and return list of fullpaths of files.

    """
    def collectEligibleFileList(self):
        toArchive = []
        for p, d, f in os.walk(self.sourceDir):
            for job in f:
                mtime = datetime.fromtimestamp(
                            os.path.getmtime(os.path.join(p, job)))
                if datetime.now() - mtime > timedelta(days=2):
                    toArchive.append(os.path.join(os.path.join(p, job)))
        return toArchive
    
    """
    Compress files in list. Return list of successful files archived.

    """
    def compressFile(self, to_archive_list):
        archived = []
        for f in to_archive_list:
            name = os.path.basename(f)
            try:
                archive = ZipFile(os.path.join(self.stagingDir,
                                    os.path.basename(f)) + self.extension,
                                    "w", allowZip64=True)
                archive.write(f, os.path.basename(f))
                archive.close()
                archived.append(os.path.basename(f))
            except BadZipfile:
                print BadZipfile
            except:
                print "An error occurred."
        return archived

    """
    Remove all local printfiles that have been archived.

    """
    def removeArchived(self, archived_list):
        for f in archived_list:
            if f in os.listdir(self.sourceDir):
                os.remove(os.path.join(self.sourceDir, f))          
    
    """
    Move all files in staging directory (.zip) to output directory.

    """
    def _sendToArchive(self):
        for f in os.listdir(self.stagingDir):
            if os.path.isfile(os.path.join(self.outputDir, f)):
                os.remove(os.path.join(self.stagingDir, f))
            else:
                shutil.move(os.path.join(self.stagingDir, f), self.outputDir)
        return

    
if __name__ == "__main__":
    test = Archive(r"C:\test\named",
                   r"C:\test\output",
                   r"C:\test\staging")    
    test.main()
