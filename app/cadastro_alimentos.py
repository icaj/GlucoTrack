from crud.crud_registro_nutricional import inserir_registro_nutricional
from util.util import limpa_tela, nome_sistema
import json
from datetime import datetime

# tela de adição de alimentos (registro nutricional) 
def adicionar_alimento(codigo_usuario):
    limpa_tela()
    nome_sistema()
    print("Registro de Alimentos")
    print("")

    data_hora = datetime.now()
    alimento = input("Nome do alimento        : ")
    carboidratos = float(input("Carboidratos (em gramas): "))
    proteinas = float(input("Proteínas (em gramas)   : "))
    gorduras = float(input("Gorduras (em gramas)    : "))

    calorias = (carboidratos * 4) + (proteinas * 4) + (gorduras * 9)
    print(f"Calorias                : {calorias}")

    resultado = inserir_registro_nutricional(codigo_paciente, alimento, data_hora, calorias, proteinas, gorduras, carboidratos)
    if resultado <= 0:
        input("ERRO na inclusão do registro nutricional !")
    else:
        input("Registro cadastrado com sucesso!")

def editar_alimento(codigo_usuario):
    pass

def excluir_alimento(codigo_usuario):
    pass

def listar_alimentos(codigo_usuario):
    pass