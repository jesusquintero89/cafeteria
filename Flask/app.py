from flask import Flask, render_template, request, redirect, flash
#from wtforms import Form
#from Flask.grupob import forms
#from Flask.grupob.database import db_session
#from Flask.grupob.models import Usuario
import sqlite3

app = Flask(__name__)

@app.route("/login", methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        try:
            username_login = request.form['username']
            password_login = request.form['password']
            with sqlite3.connect("brioche.db") as con:
                cur = con.cursor()
                cur.execute("SELECT COUNT(*) FROM USUARIOS WHERE NOMBRE = '" + username_login + "' AND CONTRASENA = '" + password_login + "' AND ESTADO = 'activo'")
                data = cur.fetchone()[0]
                if data == 0:
                    msg = 'Usuario Invalido'
                else:
                    msg = 'Usuario Valido'
        except:
            con.rollback()
            msg = 'Error'
        finally:
            if msg == 'Usuario Valido':
                return render_template('home.html', msg = msg)
            elif msg == 'Usuario Invalido':
                return render_template('login.html', msg = msg)
            else:
                return render_template('login.html', msg = msg)
    else:
        return render_template('login.html')

# @app.route("/registro", methods=['GET', 'POST'])
# def registro():
#     crea_registro = forms.Crearegistro(request.form)
#     if request.method == 'POST':
#         if crea_registro.validate():
#             usuario = Usuario(name = crea_registro.username.data,
#                             contraseña= crea_registro.password.data,
#                             correo= crea_registro.email.data)

#             db.session.add(usuario)
#             db.session.commit()

#             success_message = 'Usuario registrado con exito'
#             flash(success_message)
#         else:
#             pass

#     return render_template('registro.html', form = crea_registro)




@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/usuario/crear", methods=['GET', 'POST'])
def crearUsuario():
    if request.method == 'GET':
        return render_template('panel-usuarios-crear.html')
    else:
        try:
            nombre = request.form['nombre']
            contrasena = request.form['contrasena']
            email = request.form['email']
            # rol = request.form['rol']
            rol = 'Cajero'
            
            with sqlite3.connect("brioche.db") as con:
                cur = con.cursor()
                print("INSERT INTO USUARIOS (NOMBRE,CONTRASENA,CORREO,ROL,ESTADO) VALUES('"+nombre+"','"+contrasena+"','"+email+"','"+rol+"','activo')")
                cur.execute("INSERT INTO USUARIOS (NOMBRE,CONTRASENA,CORREO,ROL,ESTADO) VALUES('"+nombre+"','"+contrasena+"','"+email+"','"+rol+"','activo')")
                con.commit
                msg_1 = "Creado con exito"
        except:
            con.rollback()
            msg_1 = "no se pudo"
        finally:
            return render_template('panel-usuarios-crear.html', msg = msg_1)
        #rol = request.form['rol']



@app.route("/usuario/modificar", methods=['GET', 'POST'])
def modificarUsuario():

    if request.method == 'POST':
        return render_template('home.html')

    return render_template('panel-usuarios-modificar.html')

@app.route("/producto/crear", methods=['GET', 'POST'])
def crearProducto():

    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            cantidad = request.form['cantidad']
            precio = request.form['precio']

            with sqlite3.connect("brioche.db") as con:
                cur = con.cursor()
                # print("INSERT INTO PRODUCTO (NOMBRE,CANTIDAD,PRECIO_UNITARIO) VALUES('"+nombre+"',"+cantidad+","+precio+")
                print("INSERT INTO PRODUCTO (NOMBRE,CANTIDAD,PRECIO_UNITARIO) VALUES('"+nombre+"',"+cantidad+","+precio+")")
                cur.execute("INSERT INTO PRODUCTO (NOMBRE,CANTIDAD,PRECIO_UNITARIO) VALUES('"+nombre+"',"+cantidad+","+precio+")")
                con.commit
                msg = "Creado con producto con exito"
        except:
            con.rollback()
            msg = "no se pudo"
        finally:
            return render_template('create-producto.html', msg = msg)
        #return render_template('home.html')
    else:
        return render_template('create-producto.html')

@app.route("/producto/listar", methods=['GET', 'POST'])
def listarProducto():
    return render_template("list-producto.html")

@app.route("/ventas")
def ventas():
    return render_template("Ventas.html")

if __name__ =="__main__":
    app.run(port=5000,debug=True)