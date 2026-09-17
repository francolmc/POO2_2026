from database.connection import obtener_conexion, crear_tablas

# Creamos la base de datos y las tablas
crear_tablas()

conexion = obtener_conexion()
cursor = conexion.cursor()

# cursor.execute(
#     "INSERT INTO libros VALUES (?, ?, ?)",
#         ('978-0-1', 'Cien años de soledad', 3)
# )

# conexion.commit()

filtro = "' OR 'A' = 'A"
cursor.execute(f"SELECT * FROM libros WHERE isbn LIKE '' OR 'A' = 'A'")
print(cursor.fetchall())

conexion.close()