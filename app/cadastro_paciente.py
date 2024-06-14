from crud.crud_paciente import *
from util.util import *


def cadastrar_paciente(codigo_usuario):
    print("Cadastro de Paciente")


    nome = input("Nome: ")


    idade = int(input("Idade: "))


    codigo_sexo = input("Sexo (F/M): ")
    while(codigo_sexo.upper() != 'F' and codigo_sexo.upper() != 'M'):
        codigo_sexo = input("Sexo (F/M): ")


    peso = int(input("Peso (kg): "))


    altura = int(input("Altura (cm): "))


    print("informe qual o tipo de diabetes é acometido:")
    print("1 - Tipo 1")
    print("2 - Tipo 2")
    print("3 - Gestacional")
    print("4 - Outra")
    print("5 - Não possui")
    codigo_diabete = input("Tipo de diabetes: ")
    while(codigo_diabete < '1' and codigo_diabete > '5'):
        codigo_diabete = input("Tipo de diabetes: ")
    codigo_diabete = int(codigo_diabete)


    comorbidades = input("Comorbidades: ")


    resultado = inserir_paciente(codigo_usuario, nome.upper(), idade, codigo_sexo.upper(), peso, altura, codigo_diabete, comorbidades)


    if resultado == -1:
        print()
        print("Já existe um usuário com este email")
        input("pressione qualquer tecla")
    elif codigo_usuario > 0:
        print()
        print("Usuário cadastrado com sucesso!")
        input("Pressione qualquer tecla para voltar")


def listar_dados_paciente(codigo_usuario):


    paciente = buscar_paciente_por_codigo_usuario(codigo_usuario)


    imc = ( paciente.peso / ( (paciente.altura/100.0) * (paciente.altura/100.0) ) )


    print("Nome:          ", paciente.nome)
    print("Idade:         ", paciente.idade)
    print("Sexo:          ", paciente.codigo_sexo,"-",descricao_sexo(paciente.codigo_sexo))
    print("Peso:          ", paciente.peso)
    print("Altura:        ", paciente.altura)
    print("IMC:           ", f"{imc:.2f}", )
    print("Tipo diabetes: ", paciente.codigo_diabete, "-", descricao_tipo_diabete(paciente.codigo_diabete))
    print("Comorbidades:  ", paciente.comorbidades)
    print()
    
    if pergunta_sn("Deseja alterar?"):
        alterar_paciente(codigo_usuario)


def alterar_paciente(codigo_usuario):
    
    print("Alterar de Paciente")
    print()


    paciente = buscar_paciente_por_codigo_usuario(codigo_usuario)


    nome = input("Nome: ")


    if nome == '':
        nome = paciente.nome


    idade = input("Idade: ")


    if idade == '':
        idade = paciente.idade
    idade = int(idade)


    codigo_sexo = input("Sexo (F/M): ")
    while(codigo_sexo.upper() != 'F' and codigo_sexo.upper() != 'M' and codigo_sexo != ''):
        codigo_sexo = input("Sexo (F/M): ")


    if codigo_sexo == '':
        codigo_sexo = paciente.codigo_sexo


    peso = input("Peso (kg): ")


    if peso == '':
        peso = paciente.peso
    peso = int(peso)


    altura = input("Altura (cm): ")


    if altura == '':
        altura = paciente.altura
    altura = int(altura)


    print("informe qual o tipo de diabetes é acometido.")
    print("1 - Tipo 1")
    print("2 - Tipo 2")
    print("3 - Gestacional")
    print("4 - Outra")
    print("5 - Não possui")
    codigo_diabete = input("Tipo de diabetes: ")
    while(codigo_diabete < '1' and codigo_diabete > '5' and codigo_diabete != ''):
        codigo_diabete = input("Tipo de diabetes: ")


    if codigo_diabete == '':
        codigo_diabete = paciente.codigo_diabete
    codigo_diabete = int(codigo_diabete)


    comorbidades = input("Comorbidades: ")


    if comorbidades == '':
        comorbidades = paciente.comorbidades


    resultado = atualizar_paciente(paciente.codigo, codigo_usuario, nome.upper(), idade, codigo_sexo.upper(), peso, altura, codigo_diabete, comorbidades)


    if resultado == True:
        print("Paciente alterado com sucesso!")
        input("Pressione qualquer tecla para voltar")
    else:
        print()
        print("Erro na alteração das informações")
        input("Pressione qualquer tecla para voltar")
