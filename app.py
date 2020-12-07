from flask import Flask, render_template,request,flash
from formulario import Contactenos

import utils
import os #Agregue la libreria os
import yagmail as yagmail

app = Flask(__name__)

#Ocurrio un eror: The session is unavailable because no secret key was set.
# Set the secret_key on the application to something unique and secret.
app.secret_key = os.urandom(24)
#Esta linea nos va a permitir realizar las peticiones cliente servidor de forma segura por medio de una
#contraseña cifrada, en este caso mande una contraseña que viniera del Sistema operativo de manera aleatoria
#de 24 caracteres

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/home/')
def myHome():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contactenos')
def contactus():
    formulario = Contactenos()
    return render_template('contactenos.html',titulo='Contactenos', form= formulario)

@app.route('/register', methods=('GET','POST'))
def register():
    try:
        if request.method == 'POST':
            username = request.form['usuario']
            password = request.form['password']
            email = request.form['email']
            error = None

            if not utils.isUsernameValid(username):
                error = "El usuario debe ser alfanumerico"
                flash(error)
                return render_template('register.html')

            if not utils.isEmailValid(email):
                error = 'Correo inválido'
                flash(error)
                return render_template('register.html')

            if not utils.isPasswordValid(password):
                error = 'La contraseña debe tener por los menos una mayúcscula y una mínuscula y 8 caracteres'
                flash(error)
                return render_template('register.html')

            serverEmail = yagmail.SMTP('ejemplomisiontic@gmail.com', 'Maracuya1234')

            serverEmail.send(to=email, subject='Activa tu cuenta',
                             contents='Bienvenido, usa este link para activar tu cuenta')

            flash('Revisa tu correo para activar tu cuenta')

            return render_template('login.html')

        return render_template('register.html')
    except Exception as e:
        #print("Ocurrio un eror:", e)
        return render_template('register.html')

if __name__ == '__main__':
    app.run()