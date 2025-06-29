@echo off
setlocal
echo ===============================================
echo     CREADOR DE ACCESO DIRECTO - POMODORO TIMER
echo ===============================================
echo.

:: Define el nombre del script a enlazar y el nombre del acceso directo
set TARGET_SCRIPT_NAME=ejecutar_pomodoro.bat
set SHORTCUT_NAME=Pomodoro Timer

:: Obtiene la ruta completa del script de destino
set TARGET_SCRIPT_PATH="%~dp0%TARGET_SCRIPT_NAME%"

:: Define la ruta del escritorio del usuario actual
set DESKTOP_PATH=%USERPROFILE%\Desktop
set SHORTCUT_PATH="%DESKTOP_PATH%\%SHORTCUT_NAME%.lnk"

echo Creando acceso directo para: %TARGET_SCRIPT_PATH%
echo En la ubicacion: %SHORTCUT_PATH%
echo.

:: Crea un script VBS temporal para generar el acceso directo
set VBS_SCRIPT="%TEMP%\CreateShortcut_%RANDOM%.vbs"

echo Set oWS = WScript.CreateObject("WScript.Shell") > %VBS_SCRIPT%
echo sLinkFile = %SHORTCUT_PATH% >> %VBS_SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %VBS_SCRIPT%
echo oLink.TargetPath = %TARGET_SCRIPT_PATH% >> %VBS_SCRIPT%
echo oLink.Arguments = "" >> %VBS_SCRIPT%
echo oLink.WorkingDirectory = "%~dp0" >> %VBS_SCRIPT%
echo oLink.WindowStyle = 1 >> %VBS_SCRIPT%
echo oLink.IconLocation = "shell32.dll,21" >> %VBS_SCRIPT%
REM Icono genérico de reloj/tiempo. Para un icono personalizado, se necesitaría un .ico
REM Ejemplo con icono personalizado: echo oLink.IconLocation = "%~dp0app_icon.ico,0" >> %VBS_SCRIPT%
echo oLink.Description = "Acceso directo para Pomodoro Timer" >> %VBS_SCRIPT%
echo oLink.Save >> %VBS_SCRIPT%

:: Ejecuta el script VBS y luego lo elimina
cscript //nologo %VBS_SCRIPT% >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: No se pudo crear el acceso directo.
    echo Asegurate de que tienes permisos para escribir en el Escritorio.
    if exist %VBS_SCRIPT% del %VBS_SCRIPT%
    pause
    exit /b
)

if exist %VBS_SCRIPT% del %VBS_SCRIPT%

if exist %SHORTCUT_PATH% (
    echo.
    echo Acceso directo "%SHORTCUT_NAME%" creado/actualizado en tu Escritorio.
) else (
    echo.
    echo ERROR: El acceso directo no pudo ser creado.
)

echo.
pause
endlocal
