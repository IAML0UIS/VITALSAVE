import mysql.connector
from coneccion import conectarse

def recordatorio_prueba():
    prueba = conectarse()  # Llamar a la función para obtener la conexión
    
    if prueba is None:
        print("No se pudo conectar a la base de datos.")
        return
    
    cursor = None  # Asegúrate de definir cursor fuera del bloque try
    try:
        cursor = prueba.cursor()
        
        query = "SELECT * FROM citas"
        
        cursor.execute(query)
        results = cursor.fetchall()
        
        for row in results:
            print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if prueba:
            prueba.close()

if __name__ == "__main__":
    recordatorio_prueba()
