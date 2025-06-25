import tkinter as tk
from tkinter import ttk, colorchooser, messagebox
import time
import threading
import winsound
import os
import sys
import base64
from PIL import Image, ImageTk
import tempfile

# Icono de la aplicación en base64 (un tomate simple)
ICON = """
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
6ELu//9H1n9q7h8sKWrfYwAAAABJRU5ErkJggg=="""

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("400x450")  # Ligeramente más alto para mejor visualización
        self.root.resizable(False, False)
        self.root.config(bg="#f0f0f0")
        
        # Configurar el icono de la aplicación
        self.set_app_icon()
        
        # Timer variables
        self.work_time = 25 * 60  # 25 minutes in seconds
        self.break_time = 5 * 60  # 5 minutes in seconds
        self.current_time = self.work_time
        self.is_work_phase = True
        self.timer_running = False
        self.timer_paused = False
        self.timer_thread = None
        
        # Color variables
        self.work_color = "#f0f0f0"
        self.break_color = "#e8f8f5"
        self.text_color_work = "#e74c3c"
        self.text_color_break = "#2ecc71"
        
        # UI setup
        self.setup_ui()
    
    def set_app_icon(self):
        try:
            # Decodificar el icono base64 y crear un archivo temporal
            icon_data = base64.b64decode(ICON)
            self.icon_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
            self.icon_file.write(icon_data)
            self.icon_file.close()
            
            # Cargar la imagen y establecerla como icono
            icon = Image.open(self.icon_file.name)
            photo = ImageTk.PhotoImage(icon)
            self.root.iconphoto(True, photo)
            
            # Para Windows, establecer el icono en la barra de tareas
            if os.name == 'nt':
                try:
                    import ctypes
                    myappid = 'mycompany.pomodoro.timer.1.0'  # ID único para la aplicación
                    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
                except:
                    pass  # Si falla, continuar sin el ID personalizado
        except Exception as e:
            print(f"Error al configurar el icono: {e}")
    
    def setup_ui(self):
        # Title label
        self.title_label = tk.Label(
            self.root,
            text="POMODORO TIMER",
            font=("Helvetica", 20, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        self.title_label.pack(pady=(20, 0))
        
        # Status label
        self.status_label = tk.Label(
            self.root,
            text="Tiempo de Trabajo",
            font=("Helvetica", 14),
            bg="#f0f0f0",
            fg=self.text_color_work
        )
        self.status_label.pack(pady=(10, 0))
        
        # Timer display
        self.timer_display = tk.Label(
            self.root,
            text=self.format_time(self.current_time),
            font=("Helvetica", 48),
            bg="#f0f0f0",
            fg="#333333"
        )
        self.timer_display.pack(pady=(10, 20))
        
        # Control buttons frame
        self.control_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.control_frame.pack(pady=5)
        
        # Start button
        self.start_button = ttk.Button(
            self.control_frame,
            text="Iniciar",
            command=self.start_timer,
            width=10
        )
        self.start_button.grid(row=0, column=0, padx=5)
        
        # Pause button
        self.pause_button = ttk.Button(
            self.control_frame,
            text="Pausar",
            command=self.pause_timer,
            width=10,
            state=tk.DISABLED
        )
        self.pause_button.grid(row=0, column=1, padx=5)
        
        # Reset button
        self.reset_button = ttk.Button(
            self.control_frame,
            text="Reiniciar",
            command=self.reset_timer,
            width=10
        )
        self.reset_button.grid(row=0, column=2, padx=5)
        
        # Settings frame
        self.settings_frame = tk.LabelFrame(self.root, text="Configuración", bg="#f0f0f0", padx=10, pady=10)
        self.settings_frame.pack(pady=10, fill="x", padx=20)
        
        # Work time setting
        tk.Label(self.settings_frame, text="Tiempo de trabajo (min):", bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=2)
        self.work_time_var = tk.StringVar(value=str(self.work_time // 60))
        self.work_time_entry = ttk.Entry(self.settings_frame, textvariable=self.work_time_var, width=5)
        self.work_time_entry.grid(row=0, column=1, padx=5, sticky="w")
        
        # Break time setting
        tk.Label(self.settings_frame, text="Tiempo de descanso (min):", bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=2)
        self.break_time_var = tk.StringVar(value=str(self.break_time // 60))
        self.break_time_entry = ttk.Entry(self.settings_frame, textvariable=self.break_time_var, width=5)
        self.break_time_entry.grid(row=1, column=1, padx=5, sticky="w")
        
        # Color settings
        tk.Label(self.settings_frame, text="Color trabajo:", bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=2)
        self.work_color_btn = ttk.Button(self.settings_frame, text="Elegir", command=lambda: self.choose_color("work"))
        self.work_color_btn.grid(row=2, column=1, padx=5, sticky="w")
        
        tk.Label(self.settings_frame, text="Color descanso:", bg="#f0f0f0").grid(row=3, column=0, sticky="w", pady=2)
        self.break_color_btn = ttk.Button(self.settings_frame, text="Elegir", command=lambda: self.choose_color("break"))
        self.break_color_btn.grid(row=3, column=1, padx=5, sticky="w")
        
        # Apply settings button
        self.apply_button = ttk.Button(
            self.settings_frame,
            text="Aplicar cambios",
            command=self.apply_settings
        )
        self.apply_button.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Añadir información sobre cómo crear un ejecutable
        self.info_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.info_frame.pack(fill="x", padx=20, pady=(5, 10))
        
        self.info_label = tk.Label(
            self.info_frame,
            text="Para usar esta aplicación como un ejecutable,\ngenera el .exe con el script 'crear_ejecutable.bat'",
            font=("Helvetica", 8),
            bg="#f0f0f0",
            fg="#666666",
            justify=tk.CENTER
        )
        self.info_label.pack()
    
    def choose_color(self, mode):
        color = colorchooser.askcolor(title="Seleccionar color")[1]
        if color:
            if mode == "work":
                self.work_color = color
            else:
                self.break_color = color
                
    def apply_settings(self):
        try:
            work_minutes = int(self.work_time_var.get())
            break_minutes = int(self.break_time_var.get())
            
            if work_minutes <= 0 or break_minutes <= 0:
                messagebox.showerror("Error", "Los valores de tiempo deben ser mayores a 0")
                return
                
            self.work_time = work_minutes * 60
            self.break_time = break_minutes * 60
            
            if not self.timer_running:
                if self.is_work_phase:
                    self.current_time = self.work_time
                else:
                    self.current_time = self.break_time
                self.timer_display.config(text=self.format_time(self.current_time))
            
            # Apply current phase color
            if self.is_work_phase:
                self.update_ui_colors(self.work_color, self.text_color_work)
            else:
                self.update_ui_colors(self.break_color, self.text_color_break)
                
            messagebox.showinfo("Configuración", "Cambios aplicados correctamente")
                
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos")
    
    def update_ui_colors(self, bg_color, text_color):
        self.root.config(bg=bg_color)
        self.title_label.config(bg=bg_color)
        self.status_label.config(bg=bg_color, fg=text_color)
        self.timer_display.config(bg=bg_color)
        self.control_frame.config(bg=bg_color)
        self.settings_frame.config(bg=bg_color)
        for widget in self.settings_frame.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(bg=bg_color)
    
    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"
    
    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.timer_thread = threading.Thread(target=self.run_timer)
            self.timer_thread.daemon = True
            self.timer_thread.start()
        elif self.timer_paused:
            self.timer_paused = False
            self.pause_button.config(text="Pausar")
    
    def pause_timer(self):
        if not self.timer_paused:
            self.timer_paused = True
            self.pause_button.config(text="Reanudar")
        else:
            self.timer_paused = False
            self.pause_button.config(text="Pausar")
    
    def reset_timer(self):
        self.timer_running = False
        self.timer_paused = False
        self.is_work_phase = True
        self.current_time = self.work_time
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED, text="Pausar")
        self.status_label.config(text="Tiempo de Trabajo", fg=self.text_color_work)
        self.update_ui_colors(self.work_color, self.text_color_work)
        self.timer_display.config(text=self.format_time(self.current_time))
    
    def run_timer(self):
        five_sec_alert_played = False
        
        while self.timer_running and self.current_time > 0:
            if not self.timer_paused:
                # Check for 5 seconds remaining to play alert
                if self.current_time <= 5 and not five_sec_alert_played:
                    self.play_countdown_sound()
                    five_sec_alert_played = True
                
                self.current_time -= 1
                self.timer_display.config(text=self.format_time(self.current_time))
                
                if self.current_time <= 0:
                    self.play_completion_sound()
                    self.switch_phase()
                    five_sec_alert_played = False  # Reset for next phase
            
            time.sleep(1)
            
    def switch_phase(self):
        self.is_work_phase = not self.is_work_phase
        
        if self.is_work_phase:
            self.current_time = self.work_time
            self.status_label.config(text="Tiempo de Trabajo", fg=self.text_color_work)
            self.update_ui_colors(self.work_color, self.text_color_work)
        else:
            self.current_time = self.break_time
            self.status_label.config(text="Tiempo de Descanso", fg=self.text_color_break)
            self.update_ui_colors(self.break_color, self.text_color_break)
    
    def play_countdown_sound(self):
        # Sound indicating time is about to end (5 seconds remaining)
        # Higher pitch, shorter duration for urgency
        threading.Thread(target=self._play_countdown_sequence, daemon=True).start()
    
    def _play_countdown_sequence(self):
        for _ in range(3):
            winsound.Beep(1500, 200)
            time.sleep(0.1)
    
    def play_completion_sound(self):
        # Sound indicating phase is complete
        threading.Thread(target=self._play_completion_sequence, daemon=True).start()
    
    def _play_completion_sequence(self):
        # Play a sequence of beeps to indicate completion
        winsound.Beep(1000, 300)
        time.sleep(0.1)
        winsound.Beep(1200, 300)
        time.sleep(0.1)
        winsound.Beep(1500, 500)

if __name__ == "__main__":
    # Verificar si estamos ejecutando como un archivo .py o como un ejecutable congelado
    if getattr(sys, 'frozen', False):
        # Si estamos ejecutando como un ejecutable congelado
        application_path = os.path.dirname(sys.executable)
    else:
        # Si estamos ejecutando como un script .py
        application_path = os.path.dirname(os.path.abspath(__file__))
    
    # Crear la ventana principal
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
    
    # Limpiar el archivo temporal del icono al cerrar
    if hasattr(app, 'icon_file'):
        try:
            os.unlink(app.icon_file.name)
        except:
            pass
