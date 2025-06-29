@echo off
echo ===============================================
echo         POMODORO TIMER - INICIANDO
echo ===============================================
echo.

:: Verificar si Python está instalado y en el PATH
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python no se encuentra en el PATH o no está instalado.
    echo.
    echo Por favor, sigue estos pasos:
    echo 1. Descarga e instala Python desde https://www.python.org/downloads/
    echo 2. IMPORTANTE: Marca la opcion "Add Python to PATH" durante la instalacion.
    echo 3. Vuelve a ejecutar este script.
    echo.
    echo Quieres abrir la pagina de descarga de Python ahora? (S/N)
    set /p respuesta=
    if /i "%respuesta%"=="S" start https://www.python.org/downloads/
    pause
    exit /b
)
echo Python encontrado.
echo.

:: Verificar e instalar dependencias (Pillow)
echo Verificando dependencias...
python -c "import PIL" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Instalando dependencias necesarias (Pillow)...
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
) else (
    echo Dependencias ya satisfechas.
)
echo.

:: Ejecutar el Pomodoro Timer
echo Iniciando Pomodoro Timer...
python "%~dp0pomodoro_timer.py"

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Ha ocurrido un problema al ejecutar la aplicacion Pomodoro Timer.
    echo Verifica la consola para mas detalles si es posible.
)

echo.
echo La aplicacion Pomodoro Timer ha finalizado.
pause
