import tkinter as tk
import time
import random
from PIL import Image, ImageTk


class AnimatedCircleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Estimulación Visual para Bebés")
        self.root.resizable(False, False)

        # Parámetros iniciales
        self.width, self.height = 600, 400
        self.position_x = self.width // 2
        self.position_y = self.height // 2
        self.direction_x = 1
        self.direction_y = 1
        self.circle_size = 50
        self.speed = 2
        self.start_time = time.time()
        self.last_color_change = time.time()
        self.last_position_change = time.time()
        self.fade_alpha = 255  # Opacidad para la fase 4

        self.size_direction = 1 

        # Colores
        self.bg_color = "#FFFFFF"
        self.fg_color = "#000000"

        # Crear lienzo
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg=self.bg_color)
        self.canvas.pack()

        # Iniciar rutina de estimulación
        self.phase = 1
        self.run_visual_stimulation()

    def draw_circle(self, color, alpha=255):
        """Dibujar círculo con borde negro y opcionalmente difuminado"""
        self.canvas.create_oval(
            self.position_x - self.circle_size, self.position_y - self.circle_size,
            self.position_x + self.circle_size, self.position_y + self.circle_size,
            outline="black", width=3, fill=color
        )

    def phase_1_patterns(self):
        """Patrones de alto contraste"""
        if time.time() - self.last_color_change > 5:
            self.last_color_change = time.time()
            self.fg_color = random.choice(["#000000", "#FF0000", "#0000FF", "#FFFF00"])
        self.canvas.delete("all")
        self.draw_circle(self.fg_color)
        if time.time() - self.start_time < 60:
            self.root.after(16, self.phase_1_patterns)
        else:
            self.phase = 2
            self.phase_2_movement()

    def phase_2_movement(self):
        """Movimiento suave con 60 FPS"""
        if self.phase == 2:
            self.canvas.delete("all")
            self.position_x += self.direction_x * self.speed
            self.position_y += self.direction_y * self.speed

            if self.position_x - self.circle_size <= 0 or self.position_x + self.circle_size >= self.width:
                self.direction_x *= -1
            if self.position_y - self.circle_size <= 0 or self.position_y + self.circle_size >= self.height:
                self.direction_y *= -1

            self.draw_circle(self.fg_color)
            if time.time() - self.start_time < 120:
                self.root.after(16, self.phase_2_movement)
            else:
                self.phase = 3
                self.phase_3_random_positions()

    def phase_3_random_positions(self):
        """Movimiento aleatorio con desvanecimiento"""
        if self.phase == 3:
            elapsed_time = time.time() - self.last_position_change

            if elapsed_time < 1:  # Desvanecimiento
                self.fade_alpha = int(255 * (1 - elapsed_time))  # Reducir opacidad
            elif elapsed_time >= 10:  # Cambio de posición y reaparece
                self.fade_alpha = 255
                self.last_position_change = time.time()
                self.position_x = random.randint(100, 500)
                self.position_y = random.randint(100, 300)

            self.canvas.delete("all")
            self.draw_circle(self.fg_color)

            if time.time() - self.start_time < 180:
                self.root.after(16, self.phase_3_random_positions)
            else:
                self.phase = 4
                self.phase_4_size_variation()

    def phase_4_size_variation(self):
       """Cambio de tamaño gradual"""
       if self.phase == 4:
        self.canvas.delete("all")

        # Centrar el círculo al inicio
        if time.time() - self.start_time < 240:
            self.position_x, self.position_y = self.width // 2, self.height // 2

        # Cambio de tamaño gradual
        self.circle_size += self.size_direction * 2

        # Invertir la dirección del cambio si alcanza los límites
        if self.circle_size >= 100 or self.circle_size <= 30:
            self.size_direction *= -1  # 👈 Cambia de dirección al alcanzar los límites

        self.draw_circle(self.fg_color)

        if time.time() - self.start_time < 240:
            self.root.after(16, self.phase_4_size_variation)
        else:
            self.phase = 5
            self.phase_5_contrast_variation()

    def phase_5_contrast_variation(self):
        """Fase 5: Cambio de contraste en 10 segundos de forma opuesta"""
        if self.phase == 5:
            elapsed_time = time.time() - self.last_position_change
            cycle_time = 10  # 10 segundos por transición completa

            if elapsed_time >= 15:
                self.last_position_change = time.time()

            phase_ratio = (elapsed_time % cycle_time) / cycle_time  # Normaliza a 0-1 en 10 seg

            # Variación opuesta del contraste
            bg_gray = int(255 * phase_ratio)  # Fondo pasa de negro a blanco
            fg_gray = 255 - bg_gray  # Círculo pasa de blanco a negro

            if time.time() - self.start_time >= 290:
                # Últimos 10 segundos: Fondo negro y círculo desaparece
                fade_ratio = (time.time() - self.start_time - 290) / 10
                bg_gray = 0
                fg_gray = int(255 * (1 - fade_ratio))

            self.bg_color = f'#{bg_gray:02X}{bg_gray:02X}{bg_gray:02X}'
            self.fg_color = f'#{fg_gray:02X}{fg_gray:02X}{fg_gray:02X}'

            self.canvas.config(bg=self.bg_color)
            self.canvas.delete("all")
            self.draw_circle(self.fg_color)

            if time.time() - self.start_time < 300:
                self.root.after(16, self.phase_5_contrast_variation)
            else:
                print("🎉 Rutina finalizada.")
                self.root.destroy()

    def run_visual_stimulation(self):
         print("\n Iniciando rutina de estimulación visual...\n")
         self.phase_1_patterns()

def visuales():
    # Crear una nueva ventana para la animación
    ventana_animacion = tk.Toplevel()
    app = AnimatedCircleApp(ventana_animacion)  

root = tk.Tk()
root.title("Estimulador Sensorial")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(True, True)

image_path = r"C:\Users\felip\OneDrive\Escritorio\9no_semestre\pds\cunero\images_ssindex\1.png"
original_image = Image.open(image_path)

canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack(fill=tk.BOTH, expand=True)

def resize_bg(event):
    new_width = event.width
    new_height = event.height
    resized_image = original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0, 0, image=bg_image, anchor=tk.NW)
    canvas.image = bg_image

bg_image = ImageTk.PhotoImage(original_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS))
canvas.create_image(0, 0, image=bg_image, anchor=tk.NW)

root.bind("<Configure>", resize_bg)

# Funciones para cada botón
def masaje():
    print("Masaje activado")

def auditivos():
    print("Estimulación auditiva activada")

def acerca_de():
    print("Información sobre el sistema")

def salir():
    root.quit()

button_width = 15 * 10  
button_height = 2 * 20  
x_center = (screen_width - button_width) // 2
y_start = screen_height // 3
spacing = 80

# Crear botones centrados
boton_masaje = tk.Button(root, text="Masaje", command=masaje, width=15, height=2)
boton_masaje.place(x=x_center, y=y_start)

boton_visuales = tk.Button(root, text="Visuales", command=visuales, width=15, height=2)
boton_visuales.place(x=x_center, y=y_start + spacing)

boton_auditivos = tk.Button(root, text="Auditivos", command=auditivos, width=15, height=2)
boton_auditivos.place(x=x_center, y=y_start + 2 * spacing)

boton_acerca = tk.Button(root, text="Acerca de", command=acerca_de, width=15, height=2)
boton_acerca.place(x=x_center, y=y_start + 3 * spacing)

boton_salir = tk.Button(root, text="Salir", command=salir, width=15, height=2)
boton_salir.place(x=x_center, y=y_start + 4 * spacing)

root.mainloop()