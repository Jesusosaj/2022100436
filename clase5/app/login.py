from ast import Str
from flask import Blueprint, request, jsonify
import mysql.connector
from mysql.connector import Error

login = Blueprint('login', __name__)

DB_CONFIG = {
    'host': 'mysql-container',
    'user': 'unida',
    'password': 'unida123',
    'database': 'jaguarete'
}

@login.route('/login', methods=['POST'])

def llamarServicioSet():
    global user, password

    user=request.json['user']
    password=request.json['password']
    codRes, menRes, usuario, accion = verificar_credenciales(user, password)

    salida = {'codRes': codRes, 'menRes': menRes, 'usuario': user, 'accion': accion}
    return jsonify(salida)


def verificar_credenciales(user, password):
    codRes = "SIN_ERROR"
    menRes = "OK"
    usuario = None
    try:
       print("Verificar login")
       connection = mysql.connector.connect(**DB_CONFIG)
       cursor=connection.cursor(dictionary=True)

       query="SELECT username FROM users WHERE username= %s AND password = %s"
       cursor.execute(query, (user, password))

       result = cursor.fetchone()

       if result:
           usuario = result['username']
           print("Usuario y contraseña OK")
           accion = "Success"
       else:
           print("Usuario o contraseña incorrecta")
           accion = "Usuario o contraseña incorrecta"
           codRes = "Error"
           menRes = "Credenciales incorrectas"

       cursor.close()
       connection.close()
    except Error as e: 
        print("Error", str(e))
        codRes = 'Error'
        menRes = 'Msg: ' + str(e)
        accion = "Error interno"

    return codRes, menRes, usuario, accion
    