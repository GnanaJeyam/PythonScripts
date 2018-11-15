#author - GnanaJeyam

# Usage Details :
# Run the Script Using python pythonFileName filePath.
# Ex : python /home/gnanajeyam/PythonScripts/downloadBills.py /home/gnanajeyam/error.txt 

import requests
import re
import sys
import os

filePath = sys.argv[1]
filePathLen = filePath.rfind('/')
folder_path = filePath[:filePathLen]
grepped_errorFile = folder_path+"/ERROR_BILLS"

if not os.path.exists(grepped_errorFile):    
    os.mkdir(grepped_errorFile)
os.chdir(grepped_errorFile)
print ( "FileName:  "+ filePath[filePathLen:-1])
print ( "Folder:  "+ filePath[:filePathLen])

filename = open(filePath,'r').read()
errorGrep = re.findall('https:\/\/skylight.urjanet.net\/statementsearch\/getfile\?id=\w+.pdf',filename)
# Replace your SKYLIGHT Username and Password.
# SKYLIGHT Username and Password
params = {
    'username':'your_username',
    'password':'your_password'
}

# Sending the POST req with login parameters.
rs = requests.post("https://skylight.urjanet.net/login",data = params)
i=0

for line in errorGrep:
    if line:
        rp = requests.get(line,cookies=rs.cookies,stream=True)
        i = i+1
        with open(str(i)+".pdf","wb") as pdfF:
            for chk  in rp.iter_content(chunk_size=1024):
                if chk:
                    pdfF.write(chk)

print ("Totally "+ str(i) +" Downloaded.")
          