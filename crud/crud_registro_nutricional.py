from entidades.registro_nutricional import RegistroNutricional
from datetime import datetime
import json
import pickle
import os


arquivo = 'dados/registros_nutricionais.json'


def _criar_bd():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            buf = jsonpickle.encode([])
            f.write(buf)


def _ler_todos():
        with open(arquivo, 'r') as f:
            buf = f.read()
            return jsonpickle.decode(buf)

def _salvar_todos(registros):
    _criar_bd()
    with open(arquivo, 'w') as f:
        buf = jsonpickle.encode(registros)
        f.write(buf)








def _inserir(registro_nutricional):


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






def inserir_registro_nutricional(codigo_paciente, nome, data, calorias, proteinas, gorduras, carboidratos):
    registro_nutricional = RegistroNutricional(codigo_paciente, nome, data, calorias, proteinas, gorduras, carboidratos)
    return _inserir(registro_nutricional)


def buscar_registro_nutricional_por_codigo(codigo):
    registros_nutricionais = _ler_todos()
    for r in registros_nutricionais:
        if r['codigo'] == codigo:
            return RegistroNutricional(r['codigo'], r['codigo_paciente'], r['nome'], datetime.strptime(r['data'], "%d/%m/%Y %H:%M"), r['calorias'], r['proteinas'], r['gorduras'], r['carboidratos'])
    return None


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
