from crud.crud_registro_nutricional import *
from util.util import *
import json
from datetime import datetime


form_alimentos = [
    "Nome do alimento: ",
    "Data e hora da ingestao [dd/mes hh:min] : ", 
    lambda u: datetime.strptime(u, formato_dh.user),
    "Proteínas (em gramas): ", float,
    "Gorduras (em gramas): ", float,
    "Carboidratos (em gramas): ", float,
]

def alimentos_tela(id_pct):
    menu_padrao("Home > Refeicoes", [
        "Registrar",
        lambda: alimentos_novo(id_pct),
        "Listar",
        lambda: alimentos_listar(id_pct),
        "Excluir",
        lambda: alimentos_apagar(id_pct),
        "Editar",
        lambda: alimentos_editar(id_pct),
    ])

def calc_calorias(pr, go, ca):
    return (ca * 4) + (pr * 4) + (go * 9)

# tela de adição de alimentos (registro nutricional) 
def alimentos_novo(id_pct):
    dados = form_padrao(form_alimentos)
    calorias = calc_calorias(*dados[1:])
    print(f"Calorias: {calorias}")
    resultado = inserir_registro_nutricional(id_pct, 
        *dados[:2], calorias, *dados[2:])
    if resultado <= 0:
        print_wait("ERRO na inclusão do registro nutricional!")
    else:
        print_wait("Registro cadastrado com sucesso!")
    return resultado


def alimentos_listar(id_pct, w=True):
    registros = buscar_registro_nutricional_por_codigo_paciente(id_pct)
    print("Refeicoes:")
    listar_dados(registros)
    if w:
        print_wait()
    return registros

def alimentos_editar(id_pct):
    registros = alimentos_listar(id_pct, w=False)
    cod = input("ID do que deseja editar: ")
    reg = filter(lambda r: r.codigo == cod, registros)
    if len(reg) > 0:
        reg = reg[0]
    else:
        print("Nao encontrado!")
        return
    resp = form_padrao(form_alimentos, [ 
        reg.nome, reg.data, reg.proteinas, reg.gorduras, reg.carboidratos
    ])
    atualizar_registro_nutricional(cod, id_pct, 
        *resp[:2], calc_calorias(*resp[2:]), *resp[2:])


def alimentos_apagar(id_pct):
    alimentos_listar(id_pct)
    cod = input("ID do que deseja apagar: ")
    if cod == "":
        print_wait("Operacao cancelada.")
    elif apagar_registro_nutricional(cod):
        print_wait("Apagado com sucesso.")
    else:
        print_wait("Não encontrado.")
    
    
