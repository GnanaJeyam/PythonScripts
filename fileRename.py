#Rename a filename to filenam + ".pdf " using python_script
#importing two required modules os and system
import os
import sys

# Passing folder path as an argument that contains list of files
def main(path):
#change directory that contains list of files !
   os.chdir(path)
   for fname in os.listdir(path):
      os.rename(fname,fname+".pdf")

#Mentioning the main method to the interpreter
#Passing folder_path as an sytem argument during the runtime.
if __name__ == "__main__":
    main(sys.argv[1])
    
