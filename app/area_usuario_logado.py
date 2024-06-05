from util.util import limpa_tela, nome_sistema
from app.cadastro_paciente import listar_dados_paciente
from app.cadastro_medicacao import listar_medicacoes
from crud.crud_paciente import buscar_paciente_por_codigo_usuario

def tela_principal(codigo_usuario):
    limpa_tela()
    nome_sistema()
    paciente = buscar_paciente_por_codigo_usuario(codigo_usuario)
    print("Usuário: ", paciente['nome'])
    print()
    menu_principal()
    print()
    opcao = input("Digite sua opção: ")

    match opcao:
        case '1':
            listar_dados_paciente(codigo_usuario)
            tela_principal(codigo_usuario)
            
        case '2':
            listar_medicacoes(codigo_usuario)
            tela_principal(codigo_usuario)
            
        case '3':
            listar_alimentacao(codigo_usuario)
            tela_principal(codigo_usuario)
            
        case '4':
            listar_glicemia(codigo_usuario)
            tela_principal(codigo_usuario)
            
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
    