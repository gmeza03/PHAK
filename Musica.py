import tkinter as tk
import os
import pygame

# Inicializar pygame
pygame.init()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Reproductor de Música")

# Carpeta de música
carpeta_musica = os.path.expanduser("~/Documents/Phantom-AK-1.9/Musica")


# Obtener la lista de archivos de música en la carpeta
canciones = [archivo for archivo in os.listdir(carpeta_musica) if archivo.endswith(".mp3")]

# Función para reproducir una canción
def reproducir_cancion():
    seleccion = lista_canciones.curselection()
    if seleccion:
        cancion = canciones[seleccion[0]]
        pygame.mixer.music.load(os.path.join(carpeta_musica, cancion))
        pygame.mixer.music.play()

# Función para detener la reproducción
def detener_reproduccion():
    pygame.mixer.music.stop()

# Función para reproducir la siguiente canción
def siguiente_cancion():
    seleccion = lista_canciones.curselection()
    if seleccion:
        index = seleccion[0] + 1
        if index < len(canciones):
            cancion = canciones[index]
            pygame.mixer.music.load(os.path.join(carpeta_musica, cancion))
            pygame.mixer.music.play()

# Función para reproducir la canción anterior
def cancion_anterior():
    seleccion = lista_canciones.curselection()
    if seleccion:
        index = seleccion[0] - 1
        if index >= 0:
            cancion = canciones[index]
            pygame.mixer.music.load(os.path.join(carpeta_musica, cancion))
            pygame.mixer.music.play()


#Aqui es para estar al aleatorio


def reproducir_cancion_aleatoria():
    import random
    cancion_aleatoria = random.choice(canciones)
    pygame.mixer.music.load(os.path.join(carpeta_musica, cancion_aleatoria))
    pygame.mixer.music.play()

# Lista de canciones
lista_canciones = tk.Listbox(ventana)
lista_canciones.config(height=20, width=50)  # Aumenta el ancho a 80 caracteres
for cancion in canciones:
    lista_canciones.insert(tk.END, cancion)
lista_canciones.pack()


# Botones

marco_botones = tk.Frame(ventana)
marco_botones.pack(side=tk.LEFT)

boton_reproducir = tk.Button(ventana, text="Reproducir", command=reproducir_cancion)
boton_reproducir.pack(side=tk.LEFT)

boton_detener = tk.Button(ventana, text="Detener", command=detener_reproduccion)
boton_detener.pack(side=tk.LEFT)

boton_siguiente = tk.Button(ventana, text="Siguiente", command=siguiente_cancion)
boton_siguiente.pack(side=tk.LEFT)

boton_anterior = tk.Button(ventana, text="Anterior", command=cancion_anterior)
boton_anterior.pack(side=tk.LEFT)

boton_aleatorio = tk.Button(marco_botones, text="Aleatorio", command=reproducir_cancion_aleatoria)
boton_aleatorio.pack(side=tk.LEFT)

# Ejecutar la ventana
ventana.mainloop()
