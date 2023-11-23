from flask import Flask

# Creamos una instancia de la clase Flask para crear nuestra aplicación
app = Flask(__name__) 

# Ruta principal, debe estar asociada a una función que representa una 
# vista en nuestra función
@app.route('/') 
def hello():
    return 'Hola Mundo'

# Podemos configurar variables en rutas
@app.route('/hello')
def index(name):
    # Como le enviamos valor a la  variable?
    
    # Almacenamos la variable, esta tiene que entrar comoparametro de la funcion
    
    return 'Hola zorra'

