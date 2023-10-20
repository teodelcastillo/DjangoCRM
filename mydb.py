import pymysql

# Conéctate a la base de datos MySQL
dataBase = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
)

# Prepara un objeto cursor
cursorObject = dataBase.cursor()

# Crea la base de datos
cursorObject.execute("CREATE DATABASE DjangoCRM")

print('¡Todo listo!')

# Cierra la conexión
dataBase.close()
