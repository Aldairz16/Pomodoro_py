@echo off
echo ===============================================
echo         POMODORO TIMER - INICIANDO
echo ===============================================
echo.

:: Verificar instalación de dependencias
python -c "import PIL" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Instalando dependencias necesarias...
    python -m pip install pillow
    if %ERRORLEVEL% NEQ 0 (
        echo Error: No se pudo instalar Pillow.
        echo.
        echo Por favor, instala manualmente ejecutando:
        echo pip install pillow
        pause
        exit /b
    )
    echo Dependencias instaladas correctamente.
    echo.
)

:: Ejecutar el Pomodoro Timer
echo Iniciando Pomodoro Timer...
python "%~dp0pomodoro_timer.py"

:: Si hay un error al ejecutar
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Ha ocurrido un problema al iniciar la aplicación.
    echo Asegúrate de que Python esté instalado correctamente.
    echo.
    echo Para instalar Python:
    echo 1. Visita https://www.python.org/downloads/
    echo 2. Descarga la última versión
    echo 3. Marca la opción "Add Python to PATH" durante la instalación
)

pause
echo No se encontró Python instalado en el sistema.
echo.
echo Por favor, sigue estos pasos para usar Pomodoro Timer:
echo 1. Descarga e instala Python desde https://www.python.org/downloads/
echo 2. IMPORTANTE: Marca la opción "Add Python to PATH" durante la instalación
echo 3. Después de instalar Python, ejecuta install_dependencies.bat
echo 4. Luego vuelve a ejecutar este archivo
echo.
echo ¿Quieres abrir la página de descarga de Python ahora? (S/N)
set /p respuesta=
if /i "%respuesta%"=="S" start https://www.python.org/downloads/

:end
pause
