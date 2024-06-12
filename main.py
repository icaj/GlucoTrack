from app.area_usuario_logado import tela_principal
from app.cadastro_usuario import cadastrar_usuario, logar
from util.util import menu_padrao

def entrar():
    codigo_usuario = logar()
    if codigo_usuario > 0:
        tela_principal(codigo_usuario)
    else:
        input("Usuário/senha inválidos!")

def inicio():
    menu_padrao("Login", [ "Entrar", entrar, "Cadastrar usuário", cadastrar_usuario ])
    print("Obrigado por usar o GlucoTrack.")
    exit()
    
if __name__ == "__main__":
    inicio()
    
