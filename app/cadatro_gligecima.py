from dao.glicemiaDAO import GlicemiaDAO
from datetime import datetime

def tela_glicemia(codigo_paciente):
    # menu_padrao("Home > Glicemia", [])
    pass

def cadastrar_glicemia(codigo_paciente):

    data = input("Informe a data do registro de glicose (dd/mm/aaaa): ")
    conv = datetime.strptime(data, '%d/%m/%Y')
    dia = conv.day
    mes = conv.month
    ano = conv.year
    print("Data registrada: ", conv.day, "/", conv.month, "/", conv.year)

    valor = int(input("Indique o valor de glicose registrada: "))
    print("Valor: ", valor)

    glicemiaDAO = GlicemiaDAO()
    glicemiaDAO.inserirPorDados(codigo_paciente, dia, mes, ano, valor)

