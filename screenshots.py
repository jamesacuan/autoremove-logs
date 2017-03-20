#!/usr/bin/python

import subprocess as sp, os, os.path, datetime as dt, glob, math, re

networkpath   = '\\\\germany\logs'
reportpath    = '%userprofile%\Desktop'
skipdirectory = '_For submission'
assignDrive   = 'T:'

month = dt.datetime.now().month
year  = dt.datetime.now().year
dirs = os.listdir( assignDrive )
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
    print(pwd)
    print("---------------------------")
    print(j + "/" + k + " host (" + l + "%)")
    print(m + " deleted")
    if int(n) < 2:
        print(n + " host has no recent logs.")
    else:
        print(n + " hosts have no recent logs.")
    print("---------------------------\n")
  
# deletion
for pwd in dirs:
    if (pwd != skipdirectory):
        qry = assignDrive + "\\" +pwd
        os.chdir(qry)
        sP = math.ceil((sI/sT)*100)

        
        for file in glob.glob("*"):
            if file.find(month)==-1:
                if file.find(str(year))>0:
                    print(getStatus(pwd, str(sI), str(sT), str(sP), str(sD), str(sN)))
                    print(file)
                    os.remove(file)
                    sD = sD+1
                    
            if file.find("html")>0:
                print(getStatus(pwd, str(sI), str(sT), str(sP), str(sD), str(sN)))
                print(file)
                os.remove(file)
                sD=sD+1
                
            if file.find(".009")>0:
                print(getStatus(pwd, str(sI), str(sT), str(sP), str(sD), str(sN)))
                print(file)
                os.remove(file)
                sD=sD+1
             
        sI=sI+1
        print (file)
        break
        


    
