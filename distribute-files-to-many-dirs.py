import os
import shutil
import sys

class Resources:
    def __init__(self, resource, resDirsList):
        self.resource 		= resource
        self.resDirsList	= resDirsList
        self.table 		= self._directory_table()

    # Iterate through table and distribute matched resource.
    def Main(self):
        filename = os.path.basename(self.resource)
        for key, relPath in self.table.iteritems():
            if filename.startswith(key) or filename.endswith(key):
                print os.path.basename(self.resource)
                self._copy_resource(relPath)
        return

    # Returns a dictionary.
    def _directory_table(self):
        table = {# AFP/Mix mode
            'X0': r"AFPDSIN\CODEDFNT",
            'T1': r"AFPDSIN\CODEPAGE",
            'C0': r"AFPDSIN\FNTCHAR",
            'F1': r"AFPDSIN\FORMDEF",
            'O1': r"AFPDSIN\OVERLAY",
            'P1': r"AFPDSIN\PAGEDEF",
            'S1': r"AFPDSIN\PAGESEG",
            # LCDS
            '.FNT' : r"Xchange\Xfont",
            '.FRM' : r"Xchange\xform",
            '.IMG' : r"Xchange\ximage",
            '.LGO' : r"Xchange\xlogo" }
        return table

    def _copy_resource(self, relPath):
        for targetResourcePath in self.resDirsList:
            shutil.copy(self.resource, os.path.join(targetResourcePath,
                                                    relPath))
            print "Copied to: ", os.path.join(targetResourcePath, relPath)	

if __name__ == '__main__':
	# Create Production instance.
	prod = Resources(sys.arg[1],
			[	"//127.0.0.1/d$/Resources/Target204",
        			"//127.0.0.1/d$/Resources/Target514",
				"//127.0.0.1/d$/Resources/Default"])
	prod.Main()
