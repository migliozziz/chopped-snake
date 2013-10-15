# Check for empty files and delete
for txtfile in outputDir:
   # http://docs.python.org/2/library/os.html#os.stat
   if os.stat(txtfile)[6]==0
       os.remove(os.path.join(outputDir, txtfile))
