from dao.usuarioDAO import UsuarioDAO
from entidades.usuario import Usuario
from crud.crud_usuario import *
from app.cadastro_paciente import *
from util.util import *


def cadastrar_usuario():
    
    limpa_tela()
    nome_sistema()

    usuarioDAO = UsuarioDAO()

    print("Cadastro de Usuario")
    print()
    email = input("Informe seu email: ")

    while not validar_email(email):
        print("Email inválido!")
        email = input("Informe seu email: ")
    
    senha = input("Informe sua senha: ")
    while(senha == ''):
        print("Senha inválida!")
        senha = input("Informe sua senha: ")
        
    usuario = Usuario(None, email, senha)

    codigo_usuario = usuarioDAO.inserir(usuario)
    if codigo_usuario == -1:
        print()
        print("Já existe um usuário com este email")
        input("pressione qualquer tecla")
        return
    elif codigo_usuario > 0:
        print()
        print("Usuário cadastrado com sucesso!")
        input("Pressione qualquer tecla para voltar")


        cadastrar_paciente(codigo_usuario)


def logar():
    email = ''
    senha = ''

    limpa_tela()
    nome_sistema()
    while(email == ''):
        email = input("Informe seu e-mail: ")
        if email == '':
            print("e-mail inválido!")
    
    while(senha == ''):
        senha = input("Informe sua senha : ")
        if senha == '':
            print("Senha inválida!")

    resultado = login(email, senha)
    if resultado == -1:
        input("Usuário/senha inválido. Pressione qualquer tecla...")
    
    return resultado
