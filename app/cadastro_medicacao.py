from datetime import datetime
from dao.medicacaoDAO import MedicacaoDAO
from entidades.medicacao import Medicacao
from crud.crud_medicacao import inserir_medicacao, buscar_medicacao, apagar_medicacao, buscar_medicacoes_por_paciente, atualizar_medicacao
from crud.crud_paciente import buscar_paciente_por_codigo_usuario
from util.util import listar_dados, limpa_tela, nome_sistema

def nova_medicacao(codigo_paciente):
	codigo = 0
	nome = input("Nome da medicacao: ")
	dosagem = input("Dose prescrita: ")
	print("""\
Insira os horarios de administracao diaria HH:MM,
para encerrar digite algo invalido:\n""")
	i = 1
	horarios = []
	while True:
		try:
			h = input(f"{i}\t").strip()
			if h == "":
				continue
			h = h.split(":")
			h = datetime.time(int(h[0]), int(h[1]))
		except:
			break
		else:
			horarios.append(h)
			i += 1
	horarios.sort(key=lambda t: t.hour*60+t.minute)
	lembrar = input("Deseja configurar alarmes para esses horarios? [s/n]")
	if lembrar == "s":
		lembrar = True
	elif lembrar == "n":
		lembrar = False
	else:
		print("Nao entendi, entao suponho que nao deseja")
		lembrar = False	
	return Medicacao(codigo, codigo_paciente, nome, dosagem, horarios, lembrar)

def listar_medicacoes(codigo_usaurio):
	paciente = buscar_paciente_por_codigo_usuario(codigo_usaurio)
	medicacoes = buscar_medicacoes_por_paciente(paciente['codigo'])

	limpa_tela()
	nome_sistema()
	print("Medicações:")
	listar_dados(medicacoes)
	opcao = input("Deseja alterar (S/N)?: ").upper()
	while opcao != 'S' and opcao != 'N':
		opcao = input("Deseja alterar (S/N)?: ")
	
	if opcao == "S":
		print()
		codigo_medicacao = input("Informe o código da medicacao: ")
		medicacao = buscar_medicacao(int(codigo_medicacao))
		nome = input("Nome: ")
		hora_inicial = input("Hora inicial: ")
		periodicidade = input("Periodicidade: ")
		dosagem = input("Dosagem: ")
		lembrar = input("Lembrar (S/N)?: ")
		resultado = atualizar_medicacao(medicacao['codigo'], medicacao['codigo_paciente'], nome, dosagem, hora_inicial, periodicidade, lembrar)
	
	input("Digite qualquer tecla...")
