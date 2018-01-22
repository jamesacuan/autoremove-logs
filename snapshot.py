#!/usr/bin/python

import subprocess as sp, os, os.path, datetime as dt, glob, math, re

networkpath   = '\\\\germany\logs'
reportpath    = '%userprofile%\Desktop'
skipdirectory = '_For submission'
assignDrive   = 'T:'

month = dt.datetime.now().month
day   = dt.datetime.now().day
year  = dt.datetime.now().year
dirs = os.listdir(assignDrive)
redo = 'y'
red0 = 1
emptyLogs = [] # list of host without any recent logs
sT = len(dirs)-1  # dirs in total
sI = 1  # initial
fD = 0  # delete
fN = 0  # no logs
fT = 0  # files in total

# map network drive
sp.call('net use ' +assignDrive + ' /delete')
sp.call('net use ' +assignDrive + ' ' + networkpath + ' /P:Yes')

def getMonth(val):
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return month[val-1]   
month = getMonth(month)

def getStatus(pwd, j, k, m, o):
    sp.call('cls', shell=True)
    print("\n" + pwd + "\n")
    print("---------------------------\n")
    print(j + " of " + k + " host (" + str(math.ceil((int(j)/int(k))*100)) + "%)")
    print(m + " of " + o + " (" + str(math.ceil(int(o)-int(m))) +" rem.) files have been deleted.")
    print("\n---------------------------\n")
  
# deletion process
sp.call('title Autodelete logs ('+ month + " " + str(year) + ")", shell=True)
sp.call('if not exist ' + reportpath + '\logs mkdir ' + reportpath + '\logs', shell=True) # create report dir
reportpath = reportpath + '\\logs'
#sp.call('copy /y NUL '+ reportpath +'\\_report.txt >NUL', shell=True)
#sp.call('explorer.exe '+ assignDrive)
#sp.call('echo ' + str(year) + ' ' + str(day), shell=True)
#sp.call('pause', shell=True)

while(red0==1):
    for pwd in dirs:        
        tD = 0 # to be deleted?
        if (pwd != skipdirectory):
            qry = assignDrive + "\\" +pwd
            os.chdir(qry)
            print(getStatus(pwd, str(sI), str(sT), str(fD), str(fT)))
            if fN == 0:
                print('')
            elif fN < 2:
                print(str(fN) + " host has no recent logs:")
                print(emptyLogs)
            else:
                print(str(fN) + " hosts have no recent logs.")
                print(emptyLogs)
                
            if os.listdir(qry) == []:
                sp.call('echo ' + pwd + '>>"'+reportpath + '\\_report.txt"', shell=True)
                emptyLogs.append(pwd)
                fN += 1
            
            for file in glob.glob("*"):
                i = 1
                fT += 1

                #previous months
                if file.find("_"+month+"_")==-1:
                    tD = 1

                #last year        
                if file.find("_"+str(year)+"_")==-1:
                    tD = 1

                #html    
                if file.find(".html")>0:
                    tD = 1

                #thumbs.db    
                if file.find(".db")>0:
                    tD = 0
                    
                #arbitrary
                while(i<=9):
                    if file.find(".00"+str(i))>0:
                        tD = 1
                    i+=1
                    
                if(os.path.isdir(file)):
                    tD = 0
                    
                if (tD == 1):
                    # print(os.stat(file).st_size) get file size
                    os.remove(file)
                    #print(file)
                    fD += 1
                    tD = 0

                    
                '''j=1
                while(j<=day):
                    if(j<10):
                        sD = '0'+str(j)
                    else:
                        sD = str(j)
                    folder = month + sD + str(year)
                    print(folder)
                    #print('*_' + month + '_' + str(j) + '_'+ str(year) + '_*')
                    #sp.call('echo ' + folder, shell=True)
                    #sp.call('pause')
                    if file.find(".jpg") > 0:
                        if(file.find('_' + month + '_' + sD + '_'+ str(year) + '_'))>0:
                            print('true')
                            sp.call('if not exist ' + folder + ' (mkdir ' + folder + ')', shell=True)
                            sp.call('move /Y *_' + month + '_' + sD + '_'+ str(year) + '_* %CD%\\' + folder, shell=True)
                        #else:
                            #print('false')
                    j += 1
                    #print(j)
                    #dont mind me
                    sp.call('if exist *_' + month + '_' + str(i) + '_'+ str(year) + '_* (if not exist ' + folder + ' mkdir ' + folder + ')', shell=True)
                    sp.call('move /Y *_' + month + '_' + str(i) + '_'+ str(year) + '_* %CD%\\' + folder, shell=True)'''
                
                    
                
            # create dir log of current directory
            sp.call('dir > D:\jecsacuan\Desktop\logs\\' + pwd + '.txt', shell=True)
            #sp.call('dir > ' + reportpath + '\\' + pwd + '.txt', shell=True)
            
            sI += 1

    # rescan
    sp.call('cls', shell=True)
    redo = input("Do you wish to rescan the logs folder? [y/n]: ")
    if redo in ['y','Y']:
        red0=1
    else: red0=0
    
#sp.call('cls', shell=True)    
print("Finished scanning logs folder. check this directory for info:")
sp.call('echo '+reportpath, shell=True)
sp.call('pause')
