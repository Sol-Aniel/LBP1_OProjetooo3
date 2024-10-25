class Usuario:
    def __init__(self, username, senha, admin):
        self.id = id
        self.username = username
        self.senha = senha
        self.admin = admin

usuarios = [Usuario("admin", "admin123", True), Usuario("user", "user123", False)]

def verificarUsuario (user, key):
    for Usuario in usuarios:
        if user == Usuario.username:
            if key == Usuario.senha:
                return True
    return False

def verificarAdmin (user):
    for Usuario in usuarios:
        if user == Usuario.username:
            return Usuario.admin
        
class Fruta:
    def __init__(self, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

class objCarrinho:
    def __init__(self, quant, nome, subtotal):
        self.id = id
        self.quant = quant
        self.nome = nome
        self.subtotal = subtotal

frutas = [Fruta("laranja", 2.50), Fruta("maca", 3.50), Fruta("banana", 1.50), Fruta("uva", 4.50), Fruta("morango", 5.50), Fruta("kiwi", 4.80), Fruta("melancia", 7.90)]

carrinho=[]

def adicionarCarrinho (frutas, quantidade):
    for Fruta in frutas:
        if Fruta.nome == frutas:
            carrinho.append(objCarrinho(Fruta.quantitade, objCarrinho.nome, (Fruta.preco*quantidade)))
