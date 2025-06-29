==== POMODORO TIMER ====

Esta aplicación te ayuda a gestionar tus sesiones de trabajo y descanso
usando la técnica Pomodoro.

=== ARCHIVOS INCLUIDOS ===

*   `pomodoro_timer.py`: El código fuente principal de la aplicación Pomodoro Timer.
*   `ejecutar_pomodoro.bat`: Script principal para iniciar la aplicación. Verifica Python y las dependencias necesarias (Pillow) y las instala si es necesario.
*   `crear_acceso_directo.bat`: Script para crear un acceso directo de "Pomodoro Timer" en tu escritorio, facilitando el inicio de la aplicación.
*   `crear_ejecutable.bat`: Script para generar un archivo ejecutable (`.exe`) independiente de la aplicación usando PyInstaller. Esto te permite ejecutar Pomodoro Timer sin necesidad de tener Python instalado explícitamente (una vez creado el `.exe`).
*   `README.txt`: Este archivo de instrucciones.

=== CÓMO USAR ===

1.  **Ejecutar la aplicación directamente:**
    *   Haz doble clic en `ejecutar_pomodoro.bat`.
    *   La primera vez que lo ejecutes, podría tardar un momento si necesita descargar e instalar dependencias (como Pillow).
    *   Si no tienes Python instalado, el script te guiará para descargarlo.

2.  **Crear un acceso directo en el escritorio (Recomendado para uso frecuente):**
    *   Haz doble clic en `crear_acceso_directo.bat`.
    *   Esto creará un icono llamado "Pomodoro Timer" en tu escritorio.
    *   Usa este acceso directo para iniciar la aplicación fácilmente.

3.  **Anclar a la barra de tareas:**
    *   Primero, crea el acceso directo en el escritorio usando `crear_acceso_directo.bat`.
    *   Luego, haz clic derecho sobre el acceso directo "Pomodoro Timer" en tu escritorio.
    *   Selecciona "Anclar a la barra de tareas".

=== CONFIGURACIÓN DENTRO DE LA APLICACIÓN ===

Una vez que la aplicación esté en funcionamiento:
*   **Tiempos:** Puedes cambiar la duración de los periodos de trabajo y descanso directamente en la interfaz.
*   **Colores:** Personaliza los colores de fondo para las fases de trabajo y descanso.
*   **Sonidos:** La aplicación te alertará con sonidos cuando termine cada fase y 5 segundos antes de que finalice una fase.
*   No olvides presionar "Aplicar cambios" después de modificar la configuración.

=== CREAR UN EJECUTABLE INDEPENDIENTE (.EXE) ===

Si deseas crear un archivo `.exe` que puedas usar en otras máquinas con Windows sin instalar Python y Pillow por separado, o simplemente prefieres un ejecutable:

1.  **Ejecuta `crear_ejecutable.bat`:**
    *   Este script verificará si tienes PyInstaller. Si no, intentará instalarlo (necesitarás conexión a internet).
    *   Luego, empaquetará la aplicación. Este proceso puede tardar varios minutos.
2.  **Encuentra el ejecutable:**
    *   Una vez finalizado, encontrarás `PomodoroTimer.exe` dentro de una nueva carpeta llamada `dist`.
    *   Puedes mover este archivo `PomodoroTimer.exe` a otra ubicación si lo deseas.

¡Disfruta de tu productividad con Pomodoro Timer!
