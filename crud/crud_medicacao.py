from entidades.medicacao import Medicacao
import jsonpickle
import os

# caminho para o arquivo de dados no computador
arquivo = 'dados/medicacoes.json'

# função de uso interno
# se arquivo não existir cria um arquivo vazio
def _criar_bd():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            buf = jsonpickle.encode([])
            f.write(buf)

# função de uso interno:
# carrega todos os registros do arquivo
def _ler_todos():
        with open(arquivo, 'r') as f:
            return jsonpickle.decode(f.read())

def _salvar_todos(registros):
    _criar_bd()
    with open(arquivo, 'w') as f:
        buf = jsonpickle.encode(registros)
        f.write(buf)

# insere um registro no banco de dados
# devolve -1 se o registro a ser inserido nao tiver o código do paciente.
# devolve o codigo do registro se operacao comsucesso
def _inserir(medicacao):
    # valida se o campo codigo_paciente está preenchindo
    if medicacao.codigo_paciente == None:
        return -1
      
    medicacoes = _ler_todos()
        
    proximo_codigo = 0
    for r in medicacoes:
        if r['codigo'] > proximo_codigo:
            proximo_codigo = r['codigo']
            
    medicacao_dic = {'codigo': proximo_codigo + 1, 
                     'codigo_paciente': medicacao.codigo_paciente, 
                     'nome': medicacao.nome,
                     'dosagem': medicacao.dosagem, 
                     'hora_inicial': medicacao.hora_inicial, 
                     'periodicidade': medicacao.periodicidade, 
                     'lembrar': medicacao.lembrar}
    
    medicacoes.append(medicacao_dic)
    _salvar_todos(medicacoes)
    return medicacao_dic['codigo']

# atualiza um objeto no banco
# se não encontrar devolve -1
def _atualizar(medicacao):
    encontrou = 1
    medicacoes = _ler_todos()
    for r in medicacoes:
        if r['codigo'] == medicacao.codigo:
            r['codigo_paciente'] = medicacao.codigo_paciente
            r['nome'] = medicacao.nome
            r['dosagem'] = medicacao.dosagem
            r['hora_inicial'] = medicacao.hora_inicial
            r['periodicidade'] = medicacao.periodicidade
            r['lembrar'] = medicacao.lembrar
            encontrou = 1
            break
    _salvar_todos(medicacoes)
    return encontrou

def inserir_medicacao(codigo_paciente, nome, dosagem, hora_inicial, periodicidade, lembrar):
    medicacao = Medicacao(None, codigo_paciente, nome, dosagem, hora_inicial, periodicidade, lembrar)
    return _inserir(medicacao)
    
# faz uma busca do registro no arquivo pelo codigo especificado
def buscar_medicacao(codigo):
        medicacoes = _ler_todos()
        for medicacao in medicacoes:
            if medicacao['codigo'] == codigo:
                return medicacao
        return None

# faz uma busca no arquivo pelo registro com o codigo dopaciente especificado
def buscar_medicacoes_por_paciente(codigo_paciente):
    medicacoes = _ler_todos()
    medicacoes_do_paciente = []
    for medicacao in medicacoes:
        if medicacao['codigo_paciente'] == codigo_paciente:
            medicacoes_do_paciente.append(medicacao)
                
    return medicacoes_do_paciente

def atualizar_medicacao(codigo, codigo_paciente, nome, dosagem, hora_inicial, periodicidade, lembrar):
    medicacao = Medicacao(codigo, codigo_paciente, nome, dosagem, hora_inicial, periodicidade, lembrar)

    return _atualizar(medicacao)

# remove um registro do banco a partir do codigo especificado
def apagar_medicacao(codigo):
    medicacoes = _ler_todos()
    nova_lista_medicacoes = []
    for medicacao in medicacoes:
        if medicacao['codigo'] != codigo:
            nova_lista_medicacoes.append(medicacao)
    
    _salvar_todos(nova_lista_medicacoes)

