#!/usr/bin/python

import subprocess as sp, os, os.path, datetime, glob, math, re

networkpath   = '\\\\germany\logs'
reportpath    = '%userprofile%\Desktop'
skipdirectory = '_For submission'
assignDrive   = 'T:'

# map network drive
sp.call('net use ' +assignDrive + ' /delete')
sp.call('net use ' +assignDrive + ' ' + networkpath + ' /P:Yes')

# get current month and year
def getMonth(val):
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return month[val-1]   
month = getMonth(datetime.datetime.now().month)
year  = datetime.datetime.now().year

# constructors
dirs = os.listdir( assignDrive )
sT = len(dirs)-1
sI = 1
sP = 0
sD = 0
sN = 0

def getStatus(pwd, j, k, l, m, n):
    sp.call('cls', shell=True)
    print(pwd)
    print("---------------------------")
    print(j + "/" + k + " host (" + l + "%)")
    print(m + " deleted")
    print(n + " hosts have no recent logs.")
    
# deletion
for pwd in dirs:
    if (pwd != skipdirectory):
        qry = assignDrive + "\\" +pwd
        os.chdir(qry)
        sP = math.ceil((sI/sT)*100)
        print(getStatus(pwd, str(sI), str(sT), str(sP), str(sD), str(sN)))

          
        for file in glob.glob("*"):
            if file.find(month)==-1:
                if file.find(str(year))>0:     
                    sD = sD+1
            if file.find("html")>0:
                sD=sD+1
            if file.find(".009")>0:
                sD=sD+1
            sp.call("if not exist Screen_"+month)
                #sN=sN+1
        #if os.path.isfile(glob.glob(month))==true:
            #print("true")
        #sp.call("if not exist Screen_"
        sI=sI+1
        #for file in glob.glob("Screen_
        #subprocess.call('del *.009 *.html')
        


    
