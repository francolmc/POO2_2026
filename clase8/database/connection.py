import sqlite3

RUTA_DB = 'biblioteca.db'

def obtener_conexion():
    # Unico lugar del proyecto que abre la conexion con la bd
    return sqlite3.connect(RUTA_DB)

def crear_tablas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS libros (
        isbn TEXT PRIMARY KEY,
        titulo TEXT NOT NULL,
        copias_disponible INTEGER
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS socios (
        numero_socio INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL
    )
    """)
    conexion.commit()
    conexion.close()