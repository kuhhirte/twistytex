@ECHO off
ECHO Converting CSV to TEX . . .
python script\CSV2cube.py cubes
ECHO Generating collective TEX for cubes . . .
python script\generateAlph.py cubes Shape
ECHO Resizing images . . .
IF EXIST "%programfiles%\IrfanView\i_view64.exe" GOTO iviewtrue
ECHO WARNING: IrfanView (64 bit) not found!
ECHO Copying images . . .
1>NUL COPY "%cd%\pictures\*.JPG" %cd%\script\TEMPpictures\*.JPG"
GOTO iviewend
:iviewtrue
"%programfiles%\IrfanView\i_view64.exe" "%cd%\pictures\*.JPG" /resize=(500,500) /resample /aspectratio /convert="%cd%\script\TEMPpictures\*.JPG"
:iviewend
ECHO Generating PDF (1st time) . . .
pdflatex.exe main.tex >nul 2>&1
ECHO Generating PDF (2nd time) . . .
pdflatex.exe main.tex >nul 2>&1
ECHO Deleting auxilliary files . . .
DEL /F /Q *.aux >nul 2>&1
DEL /F /Q *.bbl >nul 2>&1
DEL /F /Q *.bcf >nul 2>&1
DEL /F /Q *.blg >nul 2>&1
DEL /F /Q *.log >nul 2>&1
DEL /F /Q *.out >nul 2>&1
DEL /F /Q *.xml >nul 2>&1
DEL /F /Q *.toc >nul 2>&1
REN TwistyPuzzles_%date:~6,4%%date:~3,2%%date:~0,2%.pdf TwistyPuzzles_%date:~6,4%%date:~3,2%%date:~0,2%_old.pdf >nul 2>&1
REN main.pdf TwistyPuzzles_%date:~6,4%%date:~3,2%%date:~0,2%.pdf >nul 2>&1
DEL /F /Q *old.pdf >nul 2>&1
RMDIR /S /Q script\TEMPcubes >nul 2>&1
RMDIR /S /Q script\TEMPpictures >nul 2>&1
DEL /F /Q script\cubes.tex >nul 2>&1
ECHO Done.