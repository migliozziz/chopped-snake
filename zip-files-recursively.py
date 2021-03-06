import os
import zipfile
import zlib

basedir = r"C:\folder"
outputdir = r"C:\output"

#Zip up each archive dir individually			
def zipit(archivepath,basedir):
	paths = os.listdir(archivepath)

	for f in paths:
		filename = os.path.join(archivepath,f)
		zip = zipfile.ZipFile(os.path.join(outputdir, f +".zip"), "w", zipfile.ZIP_DEFLATED, allowZip64=True)
		zip.write(filename, f)
		zip.close()
	return

if __name__ == "__main__":
  for root, dir, file in os.walk(basedir):
  	for dirs in dir:
  		if pattern.search(dirs):
  			p = os.path.join(root,dirs)
  			zipit(p,basedir)
