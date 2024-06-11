from entidades.medicacao import Medicacao
import jsonpickle
import os


arquivo = 'dados/medicacoes.json'




def _criar_bd():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            buf = jsonpickle.encode([])
            f.write(buf)




def _ler_todos():
        with open(arquivo, 'r') as f:
            return jsonpickle.decode(f.read())

def _salvar_todos(registros):
    _criar_bd()
    with open(arquivo, 'w') as f:
        buf = jsonpickle.encode(registros)
        f.write(buf)






def _inserir(medicacao):


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


def buscar_medicacao(codigo):
        medicacoes = _ler_todos()
        for medicacao in medicacoes:
            if medicacao['codigo'] == codigo:
                return medicacao
        return None


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


def apagar_medicacao(codigo):
    medicacoes = _ler_todos()
    nova_lista_medicacoes = []
    for medicacao in medicacoes:
        if medicacao['codigo'] != codigo:
            nova_lista_medicacoes.append(medicacao)
    
    _salvar_todos(nova_lista_medicacoes)

