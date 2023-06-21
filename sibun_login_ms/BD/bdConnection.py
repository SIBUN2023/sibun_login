import mysql.connector

def bdConnection():
    try:
        connection=mysql.connector.connect(
            host='docker.host.internal',
            port='5959',
            user='root',
            password='12345',
            db='sibunlogin'
        )

        if connection.is_connected():
            print("Conexión exitosa con MySQL")
            info_server=connection.get_server_info()
            print(info_server)
            cursor=connection.cursor()
            cursor.execute("SELECT DATABASE()")
            row=cursor.fetchone()
            print('Conectado a la base de datos {}'.format(row))
            return connection
    except Exception as ex:
        return print(ex)
    