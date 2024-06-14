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
		lambda: interagir_tela("Medicacao", [
			"Registrar", 
			lambda: interagir_criar(Medicacao, id_pct),
			"Listar", 
			lambda: listar(Medicacao, por_paciente(id_pct)),
			"Editar", 
			lambda: interagir_editar(Medicacao, id_pct),
			"Remover",
			lambda: interagir_excluir(Medicacao, id_pct),
		]),
		"Glicemia", 
		lambda: interagir_tela("Glicemia", [
			"Registrar", 
			lambda: interagir_criar(Glicemia, id_pct),
			"Listar", 
			lambda: listar(Glicemia, por_paciente(id_pct)),
			"Remover",
			lambda: interagir_excluir(Glicemia, id_pct),
		]),
		"Refeicao", 
		lambda: interagir_tela("Refeicao", [
			"Registrar",
			lambda: interagir_criar(Refeicao, id_pct),
			"Listar",
			lambda: listar(Refeicao, por_paciente(id_pct)),
			"Editar",
			lambda: interagir_editar(Refeicao, id_pct),
			"Remover",
			lambda: interagir_excluir(Refeicao, id_pct),
		]),
	])
	