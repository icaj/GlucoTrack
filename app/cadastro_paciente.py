from crud.crud_paciente import *
from util.util import *

# cadastra usuario com email e senha
def cadastrar_paciente(codigo_usuario):
    print("Cadastro de Paciente")

    # solicita nome
    nome = input("Nome: ")
    
    # solicita idade
    idade = int(input("Idade: "))

    # solicita genero
    codigo_sexo = input("Sexo (F/M): ")
    while(codigo_sexo.upper() != 'F' and codigo_sexo.upper() != 'M'):
        codigo_sexo = input("Sexo (F/M): ")

    # solicita peso
    peso = int(input("Peso (kg): "))

    # solicita altura
    altura = int(input("Altura (cm): "))

    # solicita tipo de diabetes
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

    # solicita comorbidades
    comorbidades = input("Comorbidades: ")

    # insetre paciente associado ao usuário logado
    resultado = inserir_paciente(codigo_usuario, nome.upper(), idade, codigo_sexo.upper(), peso, altura, codigo_diabete, comorbidades)
    # verifica se operação ocorreu com sucesso
    if resultado == -1:
        print()
        print("Já existe um usuário com este email")
        input("pressione qualquer tecla")
    elif codigo_usuario > 0:
        print()
        print("Usuário cadastrado com sucesso!")
        input("Pressione qualquer tecla para voltar")

# exibe dados cadastrais do paciente na tela
def listar_dados_paciente(codigo_usuario):
    # busca no arquivo dados do paciente a partir do codigo do usuario
    paciente = buscar_paciente_por_codigo_usuario(codigo_usuario)

    # calcula o indice de massa corpórea (IMC)
    imc = ( paciente.peso / ( (paciente.altura/100.0) * (paciente.altura/100.0) ) )

    # exibe informações
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

# Tela para alteração de dados do paciente
def alterar_paciente(codigo_usuario):
    
    print("Alterar de Paciente")
    print()

    # busca no arquivo registro do paciente pelo código do usuario
    paciente = buscar_paciente_por_codigo_usuario(codigo_usuario)

    # solicita nome
    nome = input("Nome: ")
    # se não for digitado nada, assume o valor anterior
    if nome == '':
        nome = paciente.nome

    # solciita idade
    idade = input("Idade: ")
    # se não for digitado nada, assume o valor anterior
    if idade == '':
        idade = paciente.idade
    idade = int(idade)

    # solciita gênero
    codigo_sexo = input("Sexo (F/M): ")
    while(codigo_sexo.upper() != 'F' and codigo_sexo.upper() != 'M' and codigo_sexo != ''):
        codigo_sexo = input("Sexo (F/M): ")
    # se não for digitado nada, assume o valor anterior
    if codigo_sexo == '':
        codigo_sexo = paciente.codigo_sexo

    # solicita peso
    peso = input("Peso (kg): ")
    # se não for digitado nada, assume o valor anterior
    if peso == '':
        peso = paciente.peso
    peso = int(peso)

    # solicita altura
    altura = input("Altura (cm): ")
    # se não for digitado nada, assume o valor anterior
    if altura == '':
        altura = paciente.altura
    altura = int(altura)

    # solicita tipo de diabetes
    print("informe qual o tipo de diabetes é acometido.")
    print("1 - Tipo 1")
    print("2 - Tipo 2")
    print("3 - Gestacional")
    print("4 - Outra")
    print("5 - Não possui")
    codigo_diabete = input("Tipo de diabetes: ")
    while(codigo_diabete < '1' and codigo_diabete > '5' and codigo_diabete != ''):
        codigo_diabete = input("Tipo de diabetes: ")
    # se não for digitado nada, assume o valor anterior
    if codigo_diabete == '':
        codigo_diabete = paciente.codigo_diabete
    codigo_diabete = int(codigo_diabete)

    # solicita comorbidades
    comorbidades = input("Comorbidades: ")
    # se não for digitado nada, assume o valor anterior
    if comorbidades == '':
        comorbidades = paciente.comorbidades

    # atualiza cadastro de paciente
    resultado = atualizar_paciente(paciente.codigo, codigo_usuario, nome.upper(), idade, codigo_sexo.upper(), peso, altura, codigo_diabete, comorbidades)
    # verifica se operação ocorreu com sucesso
    if resultado == True:
        print("Paciente alterado com sucesso!")
        input("Pressione qualquer tecla para voltar")
    else:
        print()
        print("Erro na alteração das informações")
        input("Pressione qualquer tecla para voltar")
