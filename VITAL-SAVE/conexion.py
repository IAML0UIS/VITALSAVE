import mysql.connector

# Conectarse a la base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="software_vitalsave"
)

# Crear un cursor
mycursor = mydb.cursor()

# Insertar una nueva cita
sql = "INSERT INTO citas (fecha, hora, descripcion, lugar) VALUES (%s, %s, %s, %s)"
val = ("2022-06-10", "08:00:00", "Consulta médica", "Hospital")
mycursor.execute(sql, val)

# Confirmar la inserción
mydb.commit()

print("Cita insertada correctamente")
