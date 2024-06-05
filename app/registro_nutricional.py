import json
from datetime import datetime
from crud.crud_registro_nutricional import *
from util.util import *
import os

def calc_calorias(pr, go, ca):
    return (ca * 4) + (pr * 4) + (go * 9)

def adicionar_registro(id_pct):
    limpa_tela()
    nome_sistema()
    alimento = input("Nome do alimento: ")
    carboidratos = float(input("Carboidratos (em gramas): "))
    proteinas = float(input("Proteínas (em gramas): "))
    gorduras = float(input("Gorduras (em gramas): "))
    
    calorias = (carboidratos * 4) + (proteinas * 4) + (gorduras * 9)
    print(f"Calorias: {calorias}")

    data_hora = input("Data e hora da ingestao [dd/mes hh:min] : ")
    data_hora = datetime.strptime(data_hora, formato_dh.user)
    
    resultado = inserir_registro_nutricional(id_pct, 
        alimento, data_hora, calorias, proteinas, gorduras, carboidratos)
    
    if resultado <= 0:
        print_wait("ERRO na inclusão do registro nutricional!")
    else:
        print_wait("Registro cadastrado com sucesso!")
    return resultado

def listar_alimentos(id_pct):
    registros = buscar_registro_nutricional_por_codigo_paciente(id_pct)
    print("Refeicoes:")
    listar_dados(registros)
    return registros

def editar_registro(id_pct):
    limpa_tela()
    nome_sistema()
    registros = listar_alimentos(id_pct)
    idx = int(input("Digite o número do registro que deseja editar: "))
    
    reg = [r for r in registros if r.codigo == idx]
    if len(reg) > 0:
        reg = reg[0]
    else:
        print("Nao encontrado!")
        return

    for chave in reg:
        if chave in [ "codigo" ]:
            continue
        novo_valor = input(f"{chave.capitalize()} [atual: {reg[chave]}]: ")
        if novo_valor:
            reg[chave] = novo_valor
        
    reg.calorias = calc_calorias(reg.proteinas, reg.gorduras, reg.carboidratos)
    atualizar_registro_nutricional(idx, id_pct, 
        reg.nome, reg.data, reg.proteinas, reg.gorduras, reg.carboidratos)

def apagar_registro(id_pct):
    limpa_tela()
    nome_sistema()
    registros = listar_registros(id_pct)
    idx = int(input("Digite o número do registro que deseja apagar: "))
    if idx == "":
        print_wait("Operacao cancelada.")
    elif apagar_registro_nutricional(idx):
        print_wait("Apagado com sucesso.")
    else:
        print_wait("Não encontrado.")

def exibir_menu():
    while True:
        limpa_tela()
        nome_sistema()
        print("1 - Registrar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Apagar")
        print("0 - Sair\n")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            registro.adicionar_registro()
        elif opcao == '2':
            registro.listar_registros()
        elif opcao == '3':
            registro.editar_registro()
        elif opcao == '4':
            registro.apagar_registro()
        elif opcao == '0':
            break
        else:
            print("Opção inválida, por favor tente novamente.")
            input("Pressione Enter para continuar...")
