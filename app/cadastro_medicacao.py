from datetime import datetime
from crud.crud_medicacao import inserir_medicacao, buscar_medicacao, apagar_medicacao, buscar_medicacoes_por_paciente, atualizar_medicacao
from crud.crud_paciente import buscar_paciente_por_codigo_usuario
from util.util import listar_dados, limpa_tela, nome_sistema

def tela_medicacao(codigo_paciente):
	menu_padrao("Home > Medicacao", [
		"Nova", 
		lambda: nova_medicacao(codigo_paciente),
		"Listar", 
		lambda:	listar_medicacoes(codigo_paciente),
		"Editar", 
		lambda: editar_medicacao(codigo_paciente),
	])


def nova_medicacao(codigo_paciente):
	nome = input("Nome da medicacao: ")
	dosagem = input("Dose prescrita: ")
	horario = input("Horario diario inicial: ")
	intervalo = input("Tomar a cada quantas horas: ")
	
	lembrar = input("Deseja configurar alarmes para esses horarios? [s/n]")
	match lembrar:
		case "s" | "S": 
			lembrar = True 
		case "n" | "N":
			lembrar = False
		case _: 
			lembrar = False
			print("Nao entendi, entao suponho que nao deseja")
	
	inserir_medicacao(codigo_paciente, nome, 
		dosagem, horario, intervalo, lembrar)

def listar_medicacoes(codigo_paciente):
	medicacoes = buscar_medicacoes_por_paciente(codigo_paciente)
	print("Medicações")
	listar_dados(medicacoes)
	input("pressione Enter para continuar...")

def editar_medicacao():
	pass