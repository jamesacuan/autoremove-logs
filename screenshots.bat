@echo off
cls
set CURR = chdir
set /a i = 01
set LOG=%userprofile%\Documents\._\logs
set GRP=COS
set LIMIT=238
set IPADD=172.16.41.
set /a beforeTotal = 0;
set /a afterTotal = 0;
set /a totalTotal = 0;
set /a totalPercent = 0;

:start
cls
echo Successfully deleted %TotalTotal% out of %beforeTotal% files (%totalPercent% percent)

if %GRP%==COS (
  if %i%==238 (
    set GRP=EDITORIAL
    set /a i = 01
    set LIMIT=40
    goto :start
  )
)

if %GRP%==EDITORIAL (
  if %i%==40 (
    set GRP=CCG
    set /a i = 01
    set LIMIT=57
    goto :start
  )
)

if %GRP%==CCG (
  if %i%==58 (
    set GRP=CSSG
    set /a i = 01
    set LIMIT=68
    goto :start
  )
)

if %GRP%==CSSG (
  if %i%==68 (
    set GRP=GALE
    set /a i = 39
    set LIMIT=42
    goto :start
  )
)

if %GRP%==GALE (
  if %i%==42 (
    set GRP=PROD
    set /a i = 09
    set LIMIT=43
    goto :start
  )
)

if %GRP%==PROD (
  if %i%==43 (
    set GRP=RESEARCH
    set /a i = 19
    set LIMIT=43
    goto :start
  )
)

for /f "tokens=1-4 delims=/ " %%i in ("%date%") do (
     set dow=%%i
     set month=%%j
     set day=%%k
     set year=%%l
)
set datestr=%month%-%day%-%year%


if %GRP%==RESEARCH (
  if %i%==43 (goto :END)
)
goto :exist

:notx
echo %GRP%-%i%,Can't access,,,%datestr% > %LOG%\temp.csv
type %LOG%\temp.csv >> %LOG%\final.csv
del %LOG%\temp.csv  
set /a i = %i%+01
goto :start



:exist
T:
if %i% LSS 8 (set i=0%i%)

IF NOT EXIST "T:\%GRP%-%i%" (
echo %GRP%-%i%,Can't access folder,,,%datestr% > %LOG%\temp.csv
type %LOG%\temp.csv >> %LOG%\final.csv
del %LOG%\temp.csv  
set /a i = %i%+1
goto :start
)

echo Accessing T:\%GRP%-%i% of %LIMIT%:
cd T:\%GRP%-%i%

:du -n | find "Size"

echo Number of Files:
dir /a-d * | find /C "/"
for /f %%A in ('dir ^| find "File(s)"') do set beforecnt=%%A
set /a beforeTotal = %beforecnt%+%beforeTotal%

:echo Current User:
:WMIC /NODE:"%GRP%-%i%" COMPUTERSYSTEM GET USERNAME

if exist *_2016* (
  echo Deleting screenshots from last year...
  dir /a-d "*_2016*" | find /C "/"
  del *_2016*
  echo DONE.
)


if exist *.html (
  echo Deleting arbritary files...
  dir /a-d "*.html" | find /C "/"
  del *.009 *.html
  echo DONE.
)

for /f %%A in ('dir ^| find "File(s)"') do set aftercnt=%%A

set /a afterTotal = %aftercnt%+%afterTotal%
set /a TotalTotal = %beforeTotal%-%afterTotal%
set /a totalPercent = (%TotalTotal%/%beforeTotal%)*100

if not exist Screen_JUL_* (
  echo %GRP%-%i%,NO SCREENSHOTS FOR JULY 2016,%beforecnt%,%aftercnt%,%datestr% > %LOG%\temp.csv
  type %LOG%\temp.csv >> %LOG%\final.csv
  del %LOG%\temp.csv
  set /a i = %i%+1
  goto :start
)

echo Generating DIR report...
dir /a-d * | find /C "/"


dir > %LOG%\%GRP%-%i%.txt
echo %datestr%,%beforeTotal%,%TotalTotal% > %LOG%\_a.csv
echo %GRP%-%i%,DONE,%beforecnt%,%aftercnt%,%datestr% > %LOG%\temp.csv
type %LOG%\temp.csv >> %LOG%\final.csv
del %LOG%\temp.csv
set /a i = %i%+1
goto :start

cd CURR

:end
cls
echo Done.
pause