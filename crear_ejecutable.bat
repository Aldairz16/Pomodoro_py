@echo off
setlocal
echo ===============================================
echo         CREADOR DE EJECUTABLE - POMODORO TIMER
echo ===============================================
echo.

:: Nombre del script de Python a empaquetar y nombre del ejecutable final
set PYTHON_SCRIPT_NAME=pomodoro_timer.py
set EXECUTABLE_NAME=PomodoroTimer

:: Ruta completa al script de Python
set PYTHON_SCRIPT_PATH="%~dp0%PYTHON_SCRIPT_NAME%"

:: Verifica si Python está instalado
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python no se encuentra en el PATH o no está instalado.
    echo Debes tener Python instalado para crear el ejecutable.
    echo Visita https://www.python.org/downloads/
    pause
    exit /b
)
echo Python encontrado.
echo.

:: Verifica si PyInstaller está instalado, si no, lo instala
echo Verificando PyInstaller...
python -m PyInstaller --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo PyInstaller no encontrado. Intentando instalar PyInstaller...
    echo Esto puede tomar unos momentos.
    python -m pip install pyinstaller
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: No se pudo instalar PyInstaller.
        echo Por favor, instala PyInstaller manualmente ejecutando: pip install pyinstaller
        pause
        exit /b
    )
    echo PyInstaller instalado correctamente.
) else (
    echo PyInstaller ya está instalado.
)
echo.

echo Creando ejecutable para %PYTHON_SCRIPT_NAME%...
echo Esto puede tardar varios minutos dependiendo de tu sistema.
echo Se generará un archivo %EXECUTABLE_NAME%.exe en la carpeta 'dist'.
echo.

:: Opciones de PyInstaller:
:: --onefile: Crea un solo archivo ejecutable.
:: --noconsole (o --windowed): Evita que se abra una ventana de consola al ejecutar la aplicacion GUI.
:: --name: Nombre del ejecutable.
:: --icon: Para añadir un icono personalizado (ej: --icon="ruta/a/tu/icono.ico").
::         PyInstaller intentará usar el icono definido en Tkinter si es posible.
::         Para este proyecto, el icono está embebido en base64 y cargado en tiempo de ejecución,
::         por lo que PyInstaller debería manejarlo bien para el .exe.
::         Si se desea un icono específico para el archivo .exe en el explorador, se puede agregar --icon="path/to/icon.ico"

python -m PyInstaller --onefile --noconsole --name %EXECUTABLE_NAME% %PYTHON_SCRIPT_PATH%

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Ha ocurrido un problema durante la creacion del ejecutable.
    echo Revisa los mensajes anteriores para mas detalles.
    pause
    exit /b
)

echo.
echo =====================================================
echo         EJECUTABLE CREADO CON EXITO
echo =====================================================
echo.
echo El archivo %EXECUTABLE_NAME%.exe se encuentra en la carpeta:
echo %~dp0dist
echo.
echo Puedes copiar %EXECUTABLE_NAME%.exe desde la carpeta 'dist'
echo a cualquier otra ubicacion si lo deseas.
echo.

pause
endlocal
