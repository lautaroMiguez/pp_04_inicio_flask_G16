from flask import Flask
import random
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def inicio():
    return "Bienvenido  a nuestro Flask"


@app.route('/dado')
def dado():
    return str(random.randint(1, 6))


@app.route('/fecha')
def fechaAleatoria():
    fechaInicio = datetime(1970, 1, 1)
    fechaFinal = datetime(2100, 12, 1)
    randomFecha = fechaInicio + (fechaFinal - fechaInicio) * random.random()
    return str(randomFecha)


@app.route('/color')
def color():
    colores = [
        "rojo", "azul", "amarillo", "verde", "naranja", "violeta", "rosa",
        "negro", "blanco", "gris"
    ]
    color = random.randint(0, 9)
    return colores[color]


@app.route('/dado/<n>')
def nNumerosDados(n):
    n = int(n)
    if n <= 0 or n > 10:
        return "Error, el numero no es valido"
    else:
        numeros = ""
        for i in range(n):
            numero = str(random.randint(1, 6))
            numeros += numero + " "
    return numeros


@app.route('/fecha/<y>')
def fechaAñoEspecifico(y):
    y = int(y)
    if y < 0 or y > 2022:
        return "Ingrese un año que ya haya pasado"
    else:
        fechaInicio = datetime(y, 1, 1)
        fechaFinal = datetime(y, 12, 1)
        randomFecha = fechaInicio + (fechaFinal -
                                     fechaInicio) * random.random()
        return str(randomFecha)


@app.route('/fecha/<y>/<m>')
def fechaAñoMesEspecifico(y, m):
    y = int(y)
    m = int(m)
    if y < 0 or y > 2022:
        return "Ingrese un año que haya pasado"
    elif m < 1 or m > 12:
        return "Ingrese un mes valido"
    else:
        if m == 2:
            fechaInicio = datetime(y, 2, 1)
            fechaFinal = datetime(y, 2, 28)
            randomFecha = fechaInicio + (fechaFinal -
                                         fechaInicio) * random.random()
            return str(randomFecha)
        elif m == 4 or m == 6 or m == 9 or m == 11:
            fechaInicio = datetime(y, m, 1)
            fechaFinal = datetime(y, m, 30)
            randomFecha = fechaInicio + (fechaFinal -
                                         fechaInicio) * random.random()
            return str(randomFecha)
        else:
            fechaInicio = datetime(y, m, 1)
            fechaFinal = datetime(y, m, 31)
            randomFecha = fechaInicio + (fechaFinal -
                                         fechaInicio) * random.random()
            return str(randomFecha)


app.run(host='0.0.0.0', port=81)
