import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz Dinámica")

# Variable para mantener el estado de la vista actual
vista_anterior = None

def cambiar_vista(boton_numero):
    global vista_anterior

    # Limpiar la ventana actual
    for widget in ventana.winfo_children():
        widget.destroy()

    # Si estamos cambiando a una nueva vista, guardamos la vista anterior
    if boton_numero != 0:
        vista_anterior = boton_numero

    # Mostrar el mensaje correspondiente dependiendo del botón
    label = tk.Label(ventana, text=f"Vista del Botón {boton_numero}", font=("Arial", 14))
    label.pack(pady=20)

    # Botones de navegación para cambiar entre vistas
    if boton_numero == 0:
        boton1 = tk.Button(ventana, text="Botón 1", command=lambda: cambiar_vista(1))
        boton1.pack(pady=5)

        boton2 = tk.Button(ventana, text="Botón 2", command=lambda: cambiar_vista(2))
        boton2.pack(pady=5)

        boton3 = tk.Button(ventana, text="Botón 3", command=lambda: cambiar_vista(3))
        boton3.pack(pady=5)

        boton4 = tk.Button(ventana, text="Botón 4", command=lambda: cambiar_vista(4))
        boton4.pack(pady=5)

    # Botón de salida para regresar a la vista anterior
    boton_regreso = tk.Button(ventana, text="Volver", command=volver_vista)
    boton_regreso.pack(pady=10)

def volver_vista():
    global vista_anterior
    # Limpiar la ventana antes de volver a la vista anterior
    for widget in ventana.winfo_children():
        widget.destroy()

    # Si hay una vista anterior, ir a ella, si no, volver a la vista inicial
    if vista_anterior is not None:
        cambiar_vista(vista_anterior)
    else:
        cambiar_vista(0)

# Vista inicial
cambiar_vista(0)

# Iniciar el loop de la ventana
ventana.mainloop()