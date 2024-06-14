from util.util import menu_padrao
from app.cadastro_paciente import buscar_paciente_por_codigo_usuario, listar_dados_paciente
from app.cadastro_medicacao import medicacao_tela
from app.cadastro_glicemia import glicemia_tela
from app.registro_nutricional import alimentos_tela

def tela_principal(codigo_usuario):
	codigo_paciente = buscar_paciente_por_codigo_usuario(codigo_usuario)
	print(codigo_paciente.nome)
	menu_padrao("Home", ["Dados Cadastrais", lambda: listar_dados_paciente(codigo_usuario),
						 "Medicacoes", lambda: medicacao_tela(codigo_paciente),
						 "Glicemia", lambda: glicemia_tela(codigo_paciente),
						 "Alimentos", lambda: alimentos_tela(codigo_paciente),
	])
	
	