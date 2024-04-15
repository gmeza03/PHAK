import getpass
import subprocess
import platform
from datetime import datetime
import time
import sqlite3
import os

def limpiar_consola():
    if platform.system() == "Windows":
        os.system('cls')  # Limpiar consola en Windows
    else:
        os.system('clear')  # Limpiar consola en Unix (Linux, macOS)

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
-T7 (TERMINAL)
-C8 (Cerrar Sesipn)
    ''')

print('''
 xxxxxxxxxxxxxxxxxxxxxx
 x--------------------x
 x-----Phantom AK------x
 x--------------------x
 xxxxxxxxxxxxxxxxxxxxxx
''')

def verificar_credenciales(username, password, dbpath):
    try:
        connection = sqlite3.connect(dbpath)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username =? AND password=?", (username, password))
        user = cursor.fetchone()
        return user is not None
    except sqlite3.Error as error:
        print("Un error ocurrió mientras se verificaban las credenciales: ", error)
        return False
    finally:
        if connection:
            connection.close()

def crear_usuario(username, password, dbpath):
    try:
        connection = sqlite3.connect(dbpath)
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
        cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        connection.commit()
        print("Usuario creado exitosamente.")
    except sqlite3.Error as error:
        print("Error al crear usuario: ", error)
    finally:
        if connection:
            connection.close()

def verificar_credenciales_default(username, password):
    return username == "root" and password == "root"

def realizar_preconfiguracion(dbpath):
    if os.path.exists(dbpath):
        print("...")
        return True
    else:
        print("Bienvenido a la preconfiguracion")
        username = input("Ingrese el nombre de usuario: ")
        password = getpass.getpass("Ingrese la contraseña: ")
        crear_usuario(username, password, dbpath)
        return True

def realizar_login(dbpath):
    username_input = str(input("Escribe tu nombre:"))
    password_input = getpass.getpass("Ingrese el password:")
    if verificar_credenciales_default(username_input, password_input):
        return True
    else:
        while not verificar_credenciales(username_input, password_input, dbpath):
            password_input = getpass.getpass("Ingrese correctamente el password: ")
        return True

def inicio_sesion(db_path):
    while True:
        if realizar_preconfiguracion(db_path):
            print("Bienvenido")
            print("Login default, username: root, password: root")
            if realizar_login(db_path):
                limpiar_consola()  # Limpiar la consola solo antes de mostrar el menú
                while True:
                    print("Bienvenido a PhantomAK feather")
                    print("username_input")
                    print("Creado por Gael Meza")
                    print("Hoy es:")
                    print(time.strftime("%d/%m/%y"))
                    hora_actual = datetime.now().strftime("%H:%M:%S")
                    print(f"La hora es: {hora_actual}")

                    mostrar_menu_apartados()

                    window = str(input("¿Qué apartado deseas abrir (M imprime los apartados) ? : "))

                    if window == "":
                        print("Por favor, ingrese un apartado.")
                        continue

                    if window == "B1":
                        limpiar_consola()
                        print("El bloc de notas abrirá en un momento")
                        # Aquí iría la lógica para abrir el bloc de notas

                    elif window == "S5":
                        limpiar_consola()
                        print("Configuración del sistema")
                        print("Puede enviar un correo electrónico a g_meza3@icloud.com, para informar sobre el problema.")

                    elif window == "C2":
                        limpiar_consola()
                        print("La Calculadora iniciará en un momento...")
                        subprocess.run(["python", "calculadora.py"])

                    elif window == "A3":
                        limpiar_consola()
                        subprocess.run(["python", "acerca_sistema.py"])

                    elif window == "R4":
                        limpiar_consola()
                        print("Reproductor iniciará en un momento...")
                        # Aquí iría la lógica para iniciar el reproductor

                    elif window == "A6":
                        limpiar_consola()
                        system_platform = platform.system()
                        if system_platform == "Windows":
                            # Comando para apagar en Windows
                            subprocess.run(["shutdown", "/s", "/t", "0"])
                        elif system_platform == "Linux" or system_platform == "Darwin":
                            # Comando para apagar en Linux o Mac
                            subprocess.run(["shutdown", "-h", "now"])
                        else:
                            print(f"Apagado no compatible con el sistema: {system_platform}")

                    elif window == "C5":
                        limpiar_consola()
                        print("La aplicación de clima se abrirá en un momento...")
                        # Aquí iría la lógica para abrir la aplicación de clima

                    elif window == "T7":
                        limpiar_consola()
                        if platform.system()== "Windows":
                            subprocess.run("cmd")
                        else:
                            subprocess.run("bash")


                    elif window == "C8":
                        limpiar_consola()
                        print("Cerrando sesión...")
                        break  # Salir del bucle interno y volver al inicio de sesión

inicio_sesion('credentials.db')
