import logging
import os
import shutil

class Resources:

	def __init__(self, watchDir, doneDir, resDirsList):
		self.watchDir 		= watchDir # Watch Dir.
		self.doneDir 		= doneDir # Post Processing Move to Dir.
		self.resDirsList	= resDirsList # List of Root Resource Dirs.
		self.table 		= self._directory_table() 
		self._logging()

	def Main(self):
		self.check_watch_directory()

	def _logging(self):
		logging.basicConfig(filename='AetnaResources.log',
                                        level=logging.INFO,
                                        format='%(asctime)s \t%(message)s',
                                        datefmt='%m/%d/%Y %H:%M:%S')

	# Returns a dictionary.
	def _directory_table(self):
		# Key: Filename/File Extension
		# Value: Relative path.
		table = {# AFP/Mix mode
                        'X0': "AFPDSIN/CODEDFNT",
                        'T1': "AFPDSIN/CODEPAGE",
                        'C0': "AFPDSIN/FNTCHAR",
                        'F1': "AFPDSIN/FORMDEF",
                        'O1': "AFPDSIN/OVERLAY",
                        'P1': "AFPDSIN/PAGEDEF",
                        'S1': "AFPDSIN/PAGESEG",
                        # LCDS
                        '.FNT' : "Xchange/Xfont",
                        '.FRM' : "Xchange/xform",
                        '.IMG' : "Xchange/ximage",
                        '.LGO' : "Xchange/xlogo" }
		return table

	def check_watch_directory(self):
		""" Iterate through each resource found in Watch Directory.
		Iterate though table and if the resource is matched to key,
		begin to copy resource.

		"""
		for resource in os.listdir(self.watchDir):
			for key, relPath in self.table.iteritems():
				if resource.startswith(key) or resource.endswith(key):
					self._copy_resource(resource, relPath)

	def _copy_resource(self, resource, relPath):
		resPath = os.path.join(self.watchDir, resource)	
		logging.info('Resource found: %s', resPath)
		for targetResourcePath in self.resDirsList:
			shutil.copy(resPath, os.path.join(targetResourcePath, relPath))
			logging.info('Copied to: %s', os.path.join(targetResourcePath, relPath))
		self._move_resource(resPath, resource)

	def _move_resource(self, resPath, resource):
		try:
                        shutil.move(resPath, self.doneDir)
			logging.info('Distribution complete. Moving to: %s',
			 		os.path.join(self.doneDir, resource))
		except WindowsError:
			pass	

if __name__ == '__main__':
	# Create Production instance.
	prod = Resources("//127.0.0.1/d$/Resources/Production/",
	 		"//127.0.0.1/d$/Resources/Prod_done",
			[	"//127.0.0.1/d$/Resources/Target204",
        			"//127.0.0.1/d$/Resources/Target514",
				"//127.0.0.1/d$/Resources/Default"])
	prod.Main()
