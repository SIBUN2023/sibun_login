class Usuario:

    def __init__(
        self, email, nombre, apellido, usuario, contrasena, direccion
    ):
        self.email = email
        self.nombre = nombre
        self.direccion = direccion
        self.apellido = apellido
        self.contrasena = contrasena
        self.usuario = usuario