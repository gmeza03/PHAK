import getpass
import subprocess
import platform
from datetime import datetime
import time
import sqlite3

def mostrar_menu_apartados():
    print('''
Apartados:

- B1(BLOC DE NOTAS)
- C2(CALCULADORA)
- A3(ACERCA DEL SISTEMA)
- R4(REPRODUCTOR)
- C5 (CLIMA)
- A6(APAGADO)
-S5 (Configuracion del sistema (reportar errores))
    ''')

print('''
 xxxxxxxxxxxxxxxxxxxxxx
 x--------------------x
 x-----Phantom AK------x
 x--------------------x
 xxxxxxxxxxxxxxxxxxxxxx
''')

def verificar_credenciales(username, password):
    try:
        connection = sqlite3.connect(credentials.db)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username =? AND password=?", (username, password))
        user = cursor.fetchone()
        return user is not None
    except sqlite3.Error as error:
        print("Un error ocurrio mientras se verificaban las crendenciales: ", error)
        return False
    finally:
        if connection:
            connection.close()

def verificar_credenciales_default(username, password):
    return username == "root" and password == "root"



print("Bienvenido")
print("Login default, username: root, password: root")

username_input = str(input("Escribe tu nombre:"))
password_input = getpass.getpass("Ingrese el password:")
if verificar_credenciales_default(username_input, password_input):
    print("")
else:
    while not verificar_credenciales(username_input, password_input, dbpath):
        password_input = getpass.getpass("Ingrese correctamente el password: ")


primera_vez = True

while True:
    if primera_vez:
        print("Bienvenido a PhantomAK 1.9")
        print(username_input)
        print("Creado por Gael Meza")
        print("Hoy es:")
        print(time.strftime("%d/%m/%y"))
        hora_actual = datetime.now().strftime("%H:%M:%S")
        print(f"La hora es: {hora_actual}")
        primera_vez = False
    else:
        mostrar_menu_apartados()

    B1 = ('''
El bloc de notas abrirá en un momento
    ''')

    window = str(input("¿Qué apartado deseas abrir (M imprime los apartados) ? : "))

    if window == "":
        print("Por favor, ingrese un apartado.")
        continue

    if window == "B1":
        print(B1)
        import Bloc

    elif window == "S5":
        print ("Configuracion del sistema")
        print("Puede enviar un correo electrónico a g_meza3@icloud.com, para informar sobre el problema.")


    elif window == "C2":
        print("La Calculadora iniciará en un momento...")
        subprocess.run(["python", "calculadora.py"])

    elif window == "A3":
        subprocess.run(["python", "acerca_sistema.py"])

    elif window == "R4":
        import Musica

    elif window == "A6":
        system_platform = platform.system()
        if system_platform == "Windows":
            # Comando para apagar en Windows
            subprocess.run(["shutdown", "/s", "/t", "0"])
        elif system_platform == "Linux" or system_platform == "Darwin":
            # Comando para apagar en Linux o Mac
            subprocess.run(["shutdown", "-h", "now"])
        else:
            print("Apagado no compatible con el sistema: {system_platform}")

    elif window == "C5":
        exec(open("clima.py").read())
