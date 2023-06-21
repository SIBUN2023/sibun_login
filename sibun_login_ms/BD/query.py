def registerQuery(connection, email, nombre, apellido, usuario, contrasena, direccion):
    mycursor = connection.cursor()
    mycursor.execute("SELECT `E_MAIL` FROM `sibunlogin`.`usuario`")

    myresult = mycursor.fetchall()

    for x in myresult:
        
        if(email==x[0]):
            return (False,"El E-mail ya esta registrado")
    mycursor = connection.cursor()
 
    mycursor.execute('''INSERT INTO `sibunlogin`.`USUARIO` (`E_MAIL`, `NOMBRE`, `APELLIDO`, `USUARIO`, `CONTRASEÑA`, `DIRECCION`) 
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s')'''%(email, nombre,apellido,usuario,contrasena,direccion))
    connection.commit()
    return (True,"Usuario registrado correctamente")

def loginUserQuery(connection, emailUser,contrasenaUser):
    mycursor = connection.cursor()
    mycursor.execute("SELECT `E_MAIL` FROM `sibunlogin`.`USUARIO`;")

    myresult = mycursor.fetchall()

    for x in myresult:
        if(emailUser==x[0]):
            
            mycursor = connection.cursor()
            mycursor.execute("SELECT `CONTRASENA` FROM `loveinbox`.`usuario` WHERE `E_MAIL` = '"+ emailUser 
            + "';")

            myresult2 = mycursor.fetchall()

            for y in myresult2:
                if(contrasenaUser==y[0]):
                    return True
    return False 

def loginAdmnQuery(connection, emailAdmn, contrasenaAdmn):
    #ToDo: Ni idea de como agregar desde el React
    mycursor = connection.cursor()
    mycursor.execute("SELECT `E_MAIL` FROM `loginusuario`.`USUARIO`;")

    myresult = mycursor.fetchall()

    for x in myresult:
        if(emailAdmn==x[0]):
            
            mycursor = connection.cursor()
            mycursor.execute("SELECT `CONTRASENA` FROM `loginusuario`.`ADMINISTRADOR` WHERE `E_MAIL` = '"+ emailAdmn + "';")

            myresult2 = mycursor.fetchall()

            for y in myresult2:
                if(contrasenaAdmn==y[0]):
                    return True
    return False 
    