from util.util import *
from app.cadastro_paciente import *
from app.cadastro_medicacao import *
from app.cadastro_glicemia import *
from app.cadastro_usuario import *
from app.registro_nutricional import *
from crud.crud_paciente import *

def tela_principal(id_usr):
	id_pct = buscar_paciente_por_codigo_usuario(id_usr)
	menu_padrao("Home", [
		"Dados Cadastrais",
		lambda: listar_dados_paciente(id_usr),
		"Medicacoes", 
		lambda: medicacao_tela(id_pct),
		"Glicemia", 
		lambda: glicemia_tela(id_pct),
		"Alimentos", 
		lambda: alimentos_tela(id_pct),
	])
	
	