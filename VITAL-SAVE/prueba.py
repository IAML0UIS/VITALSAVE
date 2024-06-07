import mysql.connector
from datetime import datetime, timedelta
import pyttsx3
import time

def conectar_base_datos():
    try:
        # Conexión a la base de datos
        mydb = mysql.connector.connect(
           host="localhost",  
            user="root",
            password="",
            database="software_vitalsave"
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

def ver_citas_disponibles():
    try:
        mydb = conectar_base_datos()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM citas")
            citas = mycursor.fetchall()
            if citas:
                print("Citas disponibles:")
                for cita in citas:
                    print(f"Fecha: {cita[1]}, Hora: {cita[2]}, Descripción: {cita[3]}, Lugar: {cita[4]}")
            else:
                print("No hay citas disponibles")
    except mysql.connector.Error as err:
        print(f"Error al obtener las citas: {err}")

def agregar_cita():
    try:
        mydb = conectar_base_datos()
        if mydb:
            fecha = input("Ingrese la fecha de la cita (YYYY-MM-DD): ")
            hora = input("Ingrese la hora de la cita (HH:MM:SS): ")
            descripcion = input("Ingrese la descripción de la cita: ")
            lugar = input("Ingrese el lugar de la cita: ")

            mycursor = mydb.cursor()
            sql = "INSERT INTO citas (fecha, hora, descripcion, lugar) VALUES (%s, %s, %s, %s)"
            val = (fecha, hora, descripcion, lugar)
            mycursor.execute(sql, val)
            mydb.commit()

            print("Cita agregada correctamente")

    except mysql.connector.Error as err:
        print(f"Error al agregar la cita: {err}")

def verificar_citas():
    try:
        mydb = conectar_base_datos()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM citas")
            citas = mycursor.fetchall()

            now = datetime.now()
            current_time = now.strftime('%H:%M:%S')

            for cita in citas:
                if cita[2] == current_time:
                    engine = pyttsx3.init()
                    engine.say(f"Recordatorio de cita: {cita[3]} en {cita[4]}")
                    engine.runAndWait()
                    time.sleep(1)  # Evitar que se repita el mensaje en el mismo segundo

    except mysql.connector.Error as err:
        print(f"Error al verificar citas: {err}")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Ver citas disponibles")
        print("2. Agregar una nueva cita")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_citas_disponibles()
        elif opcion == "2":
            agregar_cita()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor seleccione una opción válida.")

# Ejecutar el menú
menu()

# Verificar y recordar citas
while True:
    verificar_citas()
    time.sleep(1)  # Comprobar cada segundo si hay citas para recordar
