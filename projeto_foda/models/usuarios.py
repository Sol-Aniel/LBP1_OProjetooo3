class Usuario:
    def __init__(self, id, username, senha):
        self.id = id
        self.username = username
        self.senha = senha

usuarios = [Usuario(0, "admin", "admin123")]

def verificarUsuario (user, key):
    for Usuario in usuarios:
        if user == Usuario.username:
            if key == Usuario.senha:
                return True
            else:
                return False
        else:
            return False