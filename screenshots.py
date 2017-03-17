#!/usr/bin/python

import subprocess, os, datetime, glob

networkpath   = '\\\\germany\logs'
reportpath    = '%userprofile%\Desktop'
skipdirectory = '_For submission'
assignDrive   = 'T:'

#Map network drive
subprocess.call('net use ' +assignDrive + ' /delete')
subprocess.call('net use ' +assignDrive + ' ' + networkpath + ' /P:Yes')

#get current month and year
def getMonth(val):
    if (val==1):
        return 'Jan'
    elif (val==2):
        return 'Feb'
    elif (val==3):
        return 'Mar'
    elif (val==4):
        return 'Apr'
    elif (val==5):
        return 'May'
    elif (val==6):
        return 'Jun'
    elif (val==7):
        return 'Jul'
    elif (val==8):
        return 'Aug'
    elif (val==9):
        return 'Sep'
    elif (val==10):
        return 'Oct'
    elif (val==11):
        return 'Nov'
    else:
        return 'Dec'
    
month = getMonth(datetime.datetime.now().month)
year  = datetime.datetime.now().year

dirs = os.listdir( assignDrive )
#test deletion
for pwd in dirs:
    if (pwd != skipdirectory):
        qry = assignDrive + "\\" +pwd
        os.chdir(qry)
        print(pwd)
        for file in glob.glob("*.html"):
            os.remove(file)
            print(file)
        #subprocess.call('del *.009 *.html')
        


    
