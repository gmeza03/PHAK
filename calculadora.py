import tkinter as tk

def click_boton(valor):
    entrada.insert(tk.END, valor)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

ventana = tk.Tk()
ventana.title("Calculadora")

entrada = tk.Entry(ventana, font=('Arial', 20))
entrada.grid(row=0, column=0, columnspan=4)

botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for boton in botones:
    tk.Button(ventana, text=boton, padx=20, pady=20, font=('Arial', 20), command=lambda val=boton: click_boton(val) if val != '=' else calcular()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

ventana.mainloop()
