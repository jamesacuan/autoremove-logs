#!/usr/bin/python

# recreation of screenshots.bat

import subprocess as sp, os, os.path, datetime as dt, glob, math, re

networkpath   = '\\\\germany\logs'
reportpath    = '%userprofile%\Desktop'
skipdirectory = '_For submission'
assignDrive   = 'T:'

month = dt.datetime.now().month
year  = dt.datetime.now().year
dirs = os.listdir( assignDrive )
emptyLogs = [] # list of host without any recent logs
sT = len(dirs)-1  # files in total
sI = 1  # initial
sP = 0  # percent
sD = 0  # delete
sN = 0  # no logs

# map network drive
sp.call('net use ' +assignDrive + ' /delete')
sp.call('net use ' +assignDrive + ' ' + networkpath + ' /P:Yes')

def getMonth(val):
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return month[val-1]   
month = getMonth(month)

def getStatus(pwd, j, k, l, m, n):
    sp.call('cls', shell=True)
    print("\n" + pwd + "\n")
    print("---------------------------\n")
    print(j + " of " + k + " host (" + l + "%)")
    print(m + " outdated logs deleted")
    if int(n) < 2:
        print(n + " host has no recent logs.")
    else:
        print(n + " hosts have no recent logs.")
    print("\n---------------------------\n")
  
# deletion process
sp.call('title Autodelete logs', shell=True)
sp.call('if not exist ' + reportpath + '\logs mkdir ' + reportpath + '\logs', shell=True) # create report dir
reportpath = reportpath + '\\logs'

for pwd in dirs:
    
    tD = 0 # to be deleted?
    if (pwd != skipdirectory):
        qry = assignDrive + "\\" +pwd
        os.chdir(qry)
        sP = math.ceil((sI/sT)*100)
        print(getStatus(pwd, str(sI), str(sT), str(sP), str(sD), str(sN)))
        if os.listdir(qry) == []:
            emptyLogs.append(pwd)
            sN = sN+1
        
        for file in glob.glob("*"):
            if file.find(month)==-1:
                if file.find(str(year))>0:
                    td = 1
                    
            if file.find("html")>0:
                tD = 1
                
            if file.find(".009")>0:               
                tD = 1
                
            if (tD == 1):
                #print(file)
                os.remove(file)
                sD = sD+1

        # create dir log of current directory
        sp.call('dir > ' + reportpath + '\\' + pwd + '.txt', shell=True)
        sI=sI+1
        
print(emptyLogs)

    
