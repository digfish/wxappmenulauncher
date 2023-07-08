@echo off
set VIRTUALENV=%1
set CD=.
echo Using %VIRTUALENV%
%VIRTUALENV%\Scripts\activate && pyinstaller --onefile --windowed --name WxAppMenuLauncher ^
     --paths . -i %CD%\app-menu-launcher.ico ^
     --add-data "%CD%\app-menu-launcher.ico;%CD%" ^
    --workpath %CD%\build --distpath %CD%\dist --specpath  %CD% %CD%\wxessay1WxAppMenuLauncherEssay1.py
D:\venvs\wxvenv
