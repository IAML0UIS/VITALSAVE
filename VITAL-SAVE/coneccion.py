import mysql.connector

def conectarse():
    try:
        connection = mysql.connector.connect(
            host="localhost",  
            user="root",
            password="",
            database="software_vitalsave"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None
