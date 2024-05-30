from util.util import limpa_tela, nome_sistema
from crud.crud_paciente import buscar_paciente_por_codigo_usuario

def tela_principal(codigo_usuario):
    limpa_tela()
    nome_sistema()
    paciente = buscar_paciente_por_codigo_usuario(codigo_usuario)
    print(paciente.nome)
    print()
    menu_principal()
    print()
    opcao = input("Digite sua opção: ")

    match opcao:
        case '1':
            print("opcao 1")
            input("pressione qualquer tecla")
            pass
        case '2':
            print("opcao 1")
            input("pressione qualquer tecla")
            pass
        case '3':
            print("opcao 1")
            input("pressione qualquer tecla")
            pass
        case '0':
            pass
        case _:
            tela_principal(codigo_usuario)

def menu_principal():
    print("1. Dados Cadastrais")
    print("2. Medicacoes")
    print("3. Glicemia")
    print("4. Alimentos")
    print("0. Sair")
    