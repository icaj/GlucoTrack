from util.util import *
from datetime import datetime

form_glicemia = [
    "Data e hora da afericao [dd/mes/yy hh:min] : ",
    lambda u: datetime.strptime(u, formato_dh.user),
    "Valor registrado: ", float,
]

def glicemia_tela(id_pct):
    menu_padrao("Home > Glicemia", [
        "Nova", 
        lambda: glicemia_nova(id_pct),
        "Listar", 
        lambda: glicemia_listar(id_pct),
        "Apagar",
        lambda: glicemia_apagar(id_pct),
    ])

def glicemia_nova(id_pct):
    dados = form_padrao(form_glicemia)
    return inserir_glicemia(id_pct, *dados)

def glicemia_listar(id_pct, w=True):
    medicacoes = buscar_medicacoes_por_paciente(id_pct)
    print("Medicações: ")
    listar_dados(medicacoes)
    if w:
        print_wait()
    return medicacoes

def glicemia_editar(id_pct):
    registros = glicemia_listar(id_pct, w=False)
    cod = input("ID do que deseja editar: ")
    gli = filter(lambda r: r.codigo == cod, registros)
    if len(gli) > 0:
        gli = gli[0]
    else:
        print("Nao encontrado!")
        return
    resp = form_padrao(form_glicemia, [ 
        gli.data, gli.valor,
    ])
    return atualizar_glicemia(cod, id_pct, *resp)


def glicemia_apagar(id_pct):
    glicemia_listar(id_pct)
    cod = input("ID do quep deseja apagar: ")
    if cod == "":
        print_wait("Operacao cancelada.")
    elif apagar_glicemia(cod):
        print_wait("Apagado com sucesso.")
    else:
        print_wait("Não encontrado.")