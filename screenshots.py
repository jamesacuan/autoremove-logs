#!/usr/bin/python

import subprocess, os

networkpath = '\\\\germany\logs'
reportpath  = '%userprofile%\Desktop'
skipdirectory = '_For submission'

#Map network drive
subprocess.call('net use x: /delete')
subprocess.call('net use T: ' + networkpath + ' /P:Yes')

dirs = os.listdir( networkpath )

#print all files
for file in dirs:
    if (file != skipdirectory):
        print (file)
