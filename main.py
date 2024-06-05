from app.area_usuario_logado import *
from app.cadastro_usuario import *
from util.util import *
from app.cadastro_usuario import *

def inicio():
    def entrar():
        sucesso = logar()
        if sucesso > 0:
            tela_principal(sucesso)
    menu_padrao("Login", [
        "Entrar", entrar,
        "Cadastrar usuário", cadastrar_usuario,
    ])
    print("Obrigado por usar o GlucoTrack.\n")
    exit()
    
if __name__ == "__main__":
    inicio()
    
