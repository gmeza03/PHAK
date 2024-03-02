import requests
import geocoder
from tkinter import Tk, Label, Button, messagebox

def obtener_ubicacion():
    try:
        ubicacion = geocoder.ip('me')
        return ubicacion.city
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo obtener la ubicación.\nError: {str(e)}")

def obtener_temperatura(ciudad):
    try:
        url = f"http://wttr.in/{ciudad}?format=%t"
        response = requests.get(url)
        temperatura = response.text.strip()
        return temperatura
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo obtener la temperatura.\nError: {str(e)}")

def obtener_temperatura_ubicacion_actual():
    ciudad = obtener_ubicacion()
    if ciudad:
        temperatura = obtener_temperatura(ciudad)
        if temperatura is not None:
            messagebox.showinfo("Temperatura", f"La temperatura en {ciudad} es {temperatura}")
    else:
        messagebox.showerror("Error", "No se pudo obtener la ubicación actual.")

app = Tk()
app.title("Weather App")

label_ciudad = Label(app, text="La ubicación actual se determinará automáticamente.")
label_ciudad.pack(pady=10)

btn_obtener_temperatura = Button(app, text="Obtener Temperatura Actual", command=obtener_temperatura_ubicacion_actual)
btn_obtener_temperatura.pack(pady=20)

app.mainloop()

