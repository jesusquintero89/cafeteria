import sqlite3

con = sqlite3.connect("brioche.db")
print("Base de datos creada con exito")

con.execute("create table Usuarios ( id BIGINT PRIMARY KEY AUTOINCREMENT, name VARCHAR NOT NULL, email VARCHAR NOT NULL, password VARCHAR NOT NULL, rol VARCHAR")

PRINT("Tabla creada")

con.close()
