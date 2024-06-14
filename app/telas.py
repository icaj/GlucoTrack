from entidades.todas import *
from crud.io import *


def tela_login():
	def entrar():
		pacientes = listar(Paciente, None)
		if (not pacientes) or len(pacientes) == 0:
			print_wait("Favor cadastrar um usuario para comecar.")
			return
		idx = perguntar(
			"Codigo de usuario: ", 
			lambda k: k if k in pacientes else None, None,
			"Codigo invalido",
		)
		welcome(pacientes[idx])
		tela_principal(idx)
		
	interagir_tela("Login", [
		"Entrar", entrar,
		"Cadastrar usuário",
		lambda: interagir_criar(Paciente, None),
		"Excluir",
		lambda: interagir_excluir(Paciente, None),
	])


def tela_principal(id_pct):
	interagir_tela("Home", [
		"Cadastro", 
		lambda: listar(Paciente, id_pct),
		"Medicacao", 
		lambda: interagir_crud(Medicacao, id_pct),
		"Glicemia", 
		lambda: interagir_crud(Glicemia, id_pct),
		"Refeicao", 
		lambda: interagir_crud(Refeicao, id_pct),
	])
	