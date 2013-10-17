import os
import shutil

"""
Move any file from the source directory to the remote directory.

"""
class Filemove:
    def __init__(self, sourceDir, remoteDir):
        self.source = sourceDir
        self.remote = remoteDir

    def main(self):
        path = os.listdir(self.source)
        for f in path:
            self._createTextFile(f)
            self.move(os.path.join(self.source, f))

    def move(self, fullpath):
        try:
            shutil.move(fullpath, self.remote)
        except WindowsError, e:
            print "ERROR %s" % e
        return

if __name__ == '__main__':
    localtest = Filemove(r"\\localhost\source",r"\\localhost\remote")
    localtest.main()

