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
        return render_template('home.html')
    else:

        return render_template('login.html')
@app.route("/registro", methods=['GET', 'POST'])
def registro():
    crea_registro = forms.Crearegistro(request.form)
    if request.method == 'POST':
        if crea_registro.validate():
            usuario = Usuario(name = crea_registro.username.data,
                            contraseña= crea_registro.password.data,
                            correo= crea_registro.email.data)

            db.session.add(usuario)
            db.session.commit()

            success_message = 'Usuario registrado con exito'
            flash(success_message)
        else:
            pass

    return render_template('registro.html', form = crea_registro)




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
            apelllido = request.form['apellido']
            email = request.form['email']
            
            with sqlite3.connect("brioche.db") as con:
                cur = con.cursor()
                print("INSERT INTO USUARIOS (NOMBRE,CORREO) VALUES("+nombre+","+email+")")
                cur.execute("INSERT INTO USUARIOS (NOMBRE,CORREO) VALUES('"+nombre+"','"+email+"')")
                con.commit
                msg = "Creado con exito"
        except:
            con.rollback()
            msg = "no se pudo"
        finally:
            return render_template('panel-usuarios-crear.html', msg = msg)
        #rol = request.form['rol']



@app.route("/usuario/modificar", methods=['GET', 'POST'])
def modificarUsuario():

    if request.method == 'POST':
        return render_template('home.html')

    return render_template('panel-usuarios-modificar.html')

@app.route("/producto/crear", methods=['GET', 'POST'])
def crearProducto():

    if request.method == 'POST':

        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        precio = request.form['precio']
        return 'Producto creado con exito'
        #return render_template('home.html')

    return render_template('create-producto.html')

@app.route("/ventas")
def ventas():
    return render_template("Ventas.html")

if __name__ =="__main__":
    app.run(port=5000,debug=True)