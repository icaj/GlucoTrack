from prettytable import PrettyTable
import pyfiglet
import re
from datetime import date
import os
import json
from entidades.tipo_diabete import TipoDiabete

def limpa_tela():
    os.system("cls" if os.name == "nt" else "clear")
    
def nome_sistema():
    titulo = pyfiglet.figlet_format("GlucoTrack")
    print(titulo, "versão 1.0")
    print()

# exibe os dados de uma variável dicionário na tela no formato de tabela
def listar_dados(dicionario):
    # cria um objeto do tipo tabela
    tabela = PrettyTable()
    # obtem os nomes dos campos da variável dicionario
    campos = list(dicionario[1].keys())
    # define os títulos da tabela
    tabela.field_names = campos

    linha = ""
    for dado in dicionario:
        for campo in campos:
            linha = dado[campo]
        tabela.add_row(linha)

    print(tabela)

# função que valida se uma string contem um endereço de e-mail
# devolve True caso seja um endereço de e-mail ou False caso não seja
def validar_email(email):
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(padrao, email) is not None

# função que retorna a descrição de um tipo de diabetes a partir de seu código
def descricao_tipo_diabete(codigo):
    arquivo = "dados/tipos_diabetes.json"

    if not os.path.exists(arquivo):
        tipos = [ { "codigo": 1, "descricao": "Tipo 1" },
                  { "codigo": 2, "descricao": "Tipo 2" },
                  { "codigo": 3, "descricao": "Gestacional" },
                  { "codigo": 4, "descricao": "Outros"},
                  { "codigo": 5, "descricao": "Não possui"} ]

        with open(arquivo, 'w') as f:
            json.dump(tipos, f, indent=4)

    with open(arquivo, "r") as f:
        tipos = json.load(f)
    
    for r in tipos:
        if r['codigo'] == codigo:
            return r['descricao']

# função que retorna a descrição de um sexo a partir de seu código
def descricao_sexo(codigo):
    arquivo = "dados/sexo.json"

    if not os.path.exists(arquivo):
        tipos = [ { "codigo": "F", "descricao": "Feminino" },
                  { "codigo": "M", "descricao": "Masculino" }]

        with open(arquivo, 'w') as f:
            json.dump(tipos, f, indent=4)

    with open(arquivo, "r") as f:
        tipos = json.load(f)
    
    for r in tipos:
        if r['codigo'] == codigo:
            return r['descricao']

def menu_padrao(titulo, opcoes):
    acoes = opcoes[1::2]
    opcoes = opcoes[0::2]
    while True:
        limpa_tela()
        nome_sistema()
        print(f"# {titulo}\n")
        print("Operacoes:\n")
        for i, op in enumerate(opcoes):
            print(f"{i+1}. {op}")
        print("0. Sair\n")
        choice = input("Digite a desejada: ")
        if choice.isdigit():
            choice = int(choice)
        else:
            continue
        if choice == 0 or choice > len(opcoes):
            return
        print("\n")
        if a := acoes[choice-1]:
            a()

def editar_p