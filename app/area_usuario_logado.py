from util.util import *
from app.cadastro_paciente import *
from app.cadastro_medicacao import *
from app.cadastro_glicemia import *
from app.cadastro_usuario import *
from app.cadastro_alimento import *
from crud.crud_paciente import *

def tela_principal(codigo_usuario):
    codigo_paciente = buscar_paciente_por_codigo_usuario(codigo_usuario)
    menu_padrao("Home", [
        "Dados Cadastrais",
        lambda: listar_dados_paciente(codigo_usuario),
        "Medicacoes", 
        lambda: tela_medicacao(codigo_paciente),
        "Glicemia", 
        lambda: tela_glicemia(codigo_paciente),
        "Alimentos", 
        lambda: tela_alimentos(codigo_paciente),
    ])
    
    