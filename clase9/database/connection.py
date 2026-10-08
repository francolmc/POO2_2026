import sqlite3
from .conector import Conector

RUTA_DB = 'biblioteca.db'

def obtener_conexion():
    # Unico lugar del proyecto que abre la conexion con la bd
    return sqlite3.connect(RUTA_DB)

def crear_tablas(conn: Conector):
    conexion = conn.obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY,
        isbn TEXT NOT NULL,
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
    # conexion.close()