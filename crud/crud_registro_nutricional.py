from entidades.registro_nutricional import RegistroNutricional
from datetime import datetime
import json
import os

# caminho para o arquivo de dados no computador
arquivo = 'dados/registros_nutricionais.json'

# se não existir o arquivo, cria um arquivo vazio
def _criar_bd():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f)

# carrega todos os registros do arquivo
def _ler_todos():
    _criar_bd()
    with open(arquivo, 'r') as f:
        return json.load(f)

# grava todos os registos para o arquivo
def _salvar_todos(registros):
    _criar_bd()
    with open(arquivo, 'w') as f:
        json.dump(registros, f, indent=4)

# insere um registro no arquivo.
# devolve o código se gravou com sucesso.
# devolve -1 se registro nao contem o codigo do paciente
# devolve um valor maior que 0 se cadastrado com sucesso
def _inserir(registro_nutricional):
    # valida se o campo codigo_paciente está preenchindo
    if registro_nutricional.codigo_paciente == None:
        return -1
      
    registros_nutricionais = _ler_todos()
        
    proximo_codigo = 0
    for r in registros_nutricionais:
        if r['codigo'] > proximo_codigo:
            proximo_codigo = r['codigo']
            
    registro_nutricional_dic = {'codigo': proximo_codigo + 1, 
                                'codigo_paciente': registro_nutricional.codigo_paciente, 
                                'nome': registro_nutricional.nome, 
                                'data': datetime(registro_nutricional.data).strftime("%d/%m/%Y %H:%M"), 
                                'calorias': registro_nutricional.calorias,
                                'proteinas': registro_nutricional.proteinas,
                                'gorduras': registro_nutricional.gorduras,
                                'carboidratos': registro_nutricional.carboidratos}
    registros_nutricionais.append(registro_nutricional_dic)
    _salvar_todos(registros_nutricionais)
    return registro_nutricional_dic['codigo']

# atualiza um registro no banco
# se não encontrar devolve -1
def _atualizar(registro_nutricional):
    encontrou = False
    registros_nutricionais = _ler_todos()
    for r in registros_nutricionais:
        if r['codigo'] == registro_nutricional.codigo:
            r['nome'] = registro_nutricional.nome
            r['data'] = datetime(registro_nutricional.data).strftime("%d/%m/%Y %H:%M")
            r['calorias'] = registro_nutricional.calorias
            r['proteinas'] = registro_nutricional.proteinas
            r['gorduras'] = registro_nutricional.gorduras
            r['carboidratos'] = registro_nutricional.carboidratos
            encontrou = True
            break

    if encontrou:
        _salvar_todos(registros_nutricionais)

    return encontrou

# insere um registro no arquivo.
# devolve o código se gravou com sucesso.
# devolve -1 se registro pesquisado nao contem o codigo do paciente
def inserir_registro_nutricional(codigo_paciente, nome, data, calorias, proteinas, gorduras, carboidratos):
    registro_nutricional = RegistroNutricional(codigo_paciente, nome, data, calorias, proteinas, gorduras, carboidratos)
    return _inserir(registro_nutricional)

# faz uma busca do registro no arquivo pelo codigo especificado
def buscar_registro_nutricional_por_codigo(codigo):
    registros_nutricionais = _ler_todos()
    for r in registros_nutricionais:
        if r['codigo'] == codigo:
            return RegistroNutricional(r['codigo'], r['codigo_paciente'], r['nome'], datetime.strptime(r['data'], "%d/%m/%Y %H:%M"), r['calorias'], r['proteinas'], r['gorduras'], r['carboidratos'])
    return None

# faz uma busca no arquivo pelo registro com o codigo dopaciente especificado
def buscar_registro_nutricional_por_codigo_paciente(codigo_paciente):
    registros = _ler_todos()
    registros_do_paciente = []
    for r in registros:
        if r['codigo_paciente'] == codigo_paciente:
            registro_do_paciente = RegistroNutricional(r['codigo'], r['codigo_paciente'], r['nome'], datetime.strptime(r['data'], "%d/%m/%Y %H:%M"), r['calorias'], r['proteinas'], r['gorduras'], r['carboidratos'])
            registros_do_paciente.append(registro_do_paciente)
                
    return registros_do_paciente

def atualizar_registro_nutricional(codigo, codigo_paciente, nome, data, calorias, proteinas, gorduras, caboidratos):
    registro_nutricional = RegistroNutricional(codigo, codigo_paciente, nome, data, calorias, proteinas, gorduras, caboidratos)
    return _atualizar(registro_nutricional)

# remove um registro do banco a partir do codigo especificado
def apagar_registro_nutricional(codigo):
    registros_nutricionais = _ler_todos()
    nova_lista_registros_nutricionais = []
    done = False
    for r in registros_nutricionais:
        if r['codigo'] != codigo:
            nova_lista_registros_nutricionais.append(r)
        else:
            done = True
    _salvar_todos(registros_nutricionais)
    return True
