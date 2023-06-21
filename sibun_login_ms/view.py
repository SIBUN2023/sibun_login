from multiprocessing.connection import Connection
from flask import Flask, jsonify, request
import os
#from datetime import datetime
#from flask_cors import CORS
import BD.bdConnection as bdConnection
import BD.query as query

connection=bdConnection.bdConnection()
#print(query.register(connection,'cgalvis@unal.edu.co','abc','1234567','cr2','4536456'))

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return jsonify({'Login esta funcionando!': True})

@app.route('/register', methods = ['POST'])
def register():
    request_data=request.get_json()
    dicBody=request_data
    ret=query.registerQuery(connection, dicBody["email"], dicBody["nombre"], dicBody["apellido"],
                            dicBody["usuario"],dicBody["contrasena"],dicBody["direccion"])
    return jsonify({'Estado': ret[0],
    'Detalles': ret[1]})

@app.route('/login', methods = ['POST'])
def login():
    request_data=request.get_json()
    dicBody=request_data
    ret=query.loginUserQuery(connection, dicBody["email"],dicBody["contrasena"])
    return jsonify({'Login': ret})

@app.route('/loginAdmn', methods = ['POST'])
def loginAdmn():
    request_data=request.get_json()
    dicBody=request_data
    ret=query.loginAdmnQuery(connection, dicBody["email"],dicBody["contrasena"])
    return jsonify({'Login': ret})

if __name__ == "__main__" :
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)