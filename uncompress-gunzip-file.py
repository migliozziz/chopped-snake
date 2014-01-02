import gzip
import os
import shutil
import sys

class Archive:
    def __init__(self, inputFile, outputDir):
        self.inputFile = inputFile
        self.outputDir = outputDir

    def main(self):
        self.uncompressFile()        
        return
    
    def uncompressFile(self):
        fileName, fileExtension = os.path.splitext(self.inputFile)
        compressedFile = gzip.open(self.inputFile, 'rb')
        fileData = compressedFile.read()
        uncompressedFile = file(os.path.join(self.outputDir, fileName),
                                'wb')
        uncompressedFile.write(fileData)
        uncompressedFile.close()
        compressedFile.close()
        if os.path.isfile(os.path.join(self.outputDir,
                                       os.path.basename(fileName))):
            print "File exists... Replacing..."
            os.remove(os.path.join(self.outputDir, os.path.basename(fileName)))

        # Move PDF to Uncompressed Directory.
        print "Moving File:", os.path.basename(fileName), \
                "\n\tTo:", self.outputDir
        shutil.move(fileName, self.outputDir)


if __name__ == "__main__":
    # PDF full file path, Folder to move uncompressed file to.
    # prod = Archive(sys.argv[1], sys.argv[2])
    # prod.main()
    
    test = Archive(r"C:/test/in_name/sample.pdf.gz", r"C:/test/pdf")
    test.main()
