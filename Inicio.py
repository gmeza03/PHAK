import tkinter as tk
from datetime import datetime

# Funciones para abrir ventanas superpuestas
def abrir_acerca():
    ventana = tk.Toplevel(root)
    ventana.title("Acerca del sistema")
    ventana.geometry("400x300")
    tk.Label(ventana, text="Información del sistema", font=("Arial", 14)).pack(pady=20)

def apagar_sistema():
    ventana = tk.Toplevel(root)
    ventana.title("Apagar")
    ventana.geometry("300x200")
    tk.Label(ventana, text="Apagando el sistema...", font=("Arial", 14)).pack(pady=20)

def abrir_clima():
    ventana = tk.Toplevel(root)
    ventana.title("Clima")
    ventana.geometry("400x300")
    tk.Label(ventana, text="Información del clima", font=("Arial", 14)).pack(pady=20)

def abrir_notas():
    ventana = tk.Toplevel(root)
    ventana.title("Bloc de notas")
    ventana.geometry("400x300")
    tk.Label(ventana, text="Notas", font=("Arial", 14)).pack(pady=20)

def abrir_calculadora():
    ventana = tk.Toplevel(root)
    ventana.title("Calculadora")
    ventana.geometry("400x300")
    tk.Label(ventana, text="Calculadora", font=("Arial", 14)).pack(pady=20)

def abrir_musica():
    ventana = tk.Toplevel(root)
    ventana.title("Música")
    ventana.geometry("400x300")
    tk.Label(ventana, text="Reproductor de Música", font=("Arial", 14)).pack(pady=20)

def actualizar_hora():
    hora_actual = datetime.now().strftime("%H:%M:%S")
    fecha_actual = datetime.now().strftime("%d/%m/%y")
    etiqueta_hora.config(text=hora_actual)
    etiqueta_fecha.config(text=fecha_actual)
    root.after(1000, actualizar_hora)

root = tk.Tk()
root.title("Phantom AK 2.0")
root.attributes('-fullscreen', True)  # Pantalla completa
root.configure(bg="blue")

# Barra superior
top_bar = tk.Frame(root, bg="gray", height=50)
top_bar.pack(fill=tk.X)

boton_menu = tk.Label(top_bar, text="☰☰☰", bg="gray", fg="white", font=("Arial", 14))
boton_menu.bind("<Button-1>", lambda e: abrir_acerca())
boton_menu.pack(side=tk.LEFT, padx=10)

boton_apagar = tk.Label(top_bar, text="Apagar", bg="gray", fg="white", font=("Arial", 12))
boton_apagar.bind("<Button-1>", lambda e: apagar_sistema())
boton_apagar.pack(side=tk.LEFT, padx=20)

boton_clima = tk.Label(top_bar, text="Clima", bg="gray", fg="white", font=("Arial", 12))
boton_clima.bind("<Button-1>", lambda e: abrir_clima())
boton_clima.pack(side=tk.LEFT, padx=20)

etiqueta_fecha = tk.Label(top_bar, text="", bg="gray", fg="white", font=("Arial", 12))
etiqueta_fecha.pack(side=tk.RIGHT, padx=10)

# Barra inferior
bottom_bar = tk.Frame(root, bg="gray", height=50)
bottom_bar.pack(side=tk.BOTTOM, fill=tk.X)

boton_notas = tk.Label(bottom_bar, text="Notas", bg="gray", fg="white", font=("Arial", 12))
boton_notas.bind("<Button-1>", lambda e: abrir_notas())
boton_notas.pack(side=tk.LEFT, padx=20)

boton_calculadora = tk.Label(bottom_bar, text="Calculadora", bg="gray", fg="white", font=("Arial", 12))
boton_calculadora.bind("<Button-1>", lambda e: abrir_calculadora())
boton_calculadora.pack(side=tk.LEFT, padx=20)

boton_musica = tk.Label(bottom_bar, text="Música", bg="gray", fg="white", font=("Arial", 12))
boton_musica.bind("<Button-1>", lambda e: abrir_musica())
boton_musica.pack(side=tk.LEFT, padx=20)

etiqueta_hora = tk.Label(bottom_bar, text="", bg="gray", fg="white", font=("Arial", 12))
etiqueta_hora.pack(side=tk.RIGHT, padx=10)

actualizar_hora()
root.mainloop()

