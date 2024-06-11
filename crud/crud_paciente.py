from entidades.paciente import Paciente
import jsonpickle
import os


arquivo = 'dados/pacientes.json'


def _criar_bd():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            buf = jsonpickle.encode([])
            f.write(buf)


def _ler_todos():
    _criar_bd()

    with open(arquivo, 'r') as f:
        return jsonpickle.decode(f.read())

def _salvar_todos(registros):
    _criar_bd()
    with open(arquivo, 'w') as f:
        buf = jsonpickle.encode(registros)
        f.write(buf)








def _inserir(paciente):


    if paciente.codigo_usuario == None:
        print("Paciente sem códico de usuário")
        return -2
      
    pacientes = _ler_todos()


    for r in pacientes:
        if r['codigo_usuario'] == paciente.codigo_usuario:
            print("Já existe um paciente com este usuário cadastrado")
            return -1


    proximo_codigo = 0
    for r in pacientes:
        if r['codigo'] > proximo_codigo:
            proximo_codigo = r['codigo']
            
    paciente_dic = { 'codigo':         proximo_codigo + 1, 
                     'codigo_usuario': paciente.codigo_usuario, 
                     'nome':           paciente.nome, 
                     'idade':          paciente.idade, 
                     'codigo_sexo':    paciente.codigo_sexo, 
                     'peso':           paciente.peso, 
                     'altura':         paciente.altura,
                     'codigo_diabete': paciente.codigo_diabete,
                     'comorbidades':   paciente.comorbidades }
    
    pacientes.append(paciente_dic)
    _salvar_todos(pacientes)
    return paciente_dic['codigo']






def inserir_paciente(codigo_usuario, nome, idade, codigo_sexo, peso, altura, codigo_diabete, comorbidades):

    paciente = Paciente(None, codigo_usuario, nome, idade, codigo_sexo, peso, altura, codigo_diabete, comorbidades)

    return _inserir(paciente)






def buscar_paciente(codigo):
    pacientes = _ler_todos()
    for r in pacientes:
        if r['codigo'] == codigo:
            return Paciente(r['codigo'], 
                            r['codigo_usuario'], 
                            r['nome'],
                            r['idade'], 
                            r['codigo_sexo'], 
                            r['peso'], 
                            r['altura'],
                            r['codigo_diabete'],
                            r['comorbidades'])

    print("Paciente não encontrado")
    return -1


def buscar_paciente_por_codigo_usuario(codigo_usuario):
    pacientes = _ler_todos()
    for r in pacientes:
        if r['codigo_usuario'] == codigo_usuario:
            return Paciente(r['codigo'], 
                            r['codigo_usuario'], 
                            r['nome'], 
                            r['idade'], 
                            r['codigo_sexo'], 
                            r['peso'], 
                            r['altura'],
                            r['codigo_diabete'],
                            r['comorbidades'])
        
    print("Paciente não encontrado")
    return -1




def atualizar_paciente(codigo, codigo_usuario, nome, idade, codigo_sexo, peso, altura, codigo_diabete, comorbidades):

    paciente = Paciente(codigo, codigo_usuario, nome, idade, codigo_sexo, peso, altura, codigo_diabete, comorbidades)

    return _atualizar(paciente)




def _atualizar(paciente):
    encontrou = False


    pacientes = _ler_todos()


    for r in pacientes:
        if r['codigo'] == paciente.codigo:
            r['nome'] = paciente.nome
            r['idade'] = paciente.idade
            r['codigo_sexo'] = paciente.codigo_sexo
            r['peso'] = paciente.peso
            r['altura'] = paciente.altura
            r['codigo_diabete'] = paciente.codigo_diabete
            r['comorbidades'] = paciente.comorbidades
            encontrou = True
            break

    _salvar_todos(pacientes)


    return encontrou


def apagar_paciente(codigo):


    pacientes = _ler_todos()

    nova_lista_pacientes = []


    for paciente in pacientes:
        if paciente['codigo'] != codigo:
            nova_lista_pacientes.append(paciente)


    _salvar_todos(nova_lista_pacientes)

def buscar_pacientes():
    pacientes = _ler_todos()
    lista_de_pacientes = []

    for r in pacientes:
        paciente = Paciente(r['codigo'], 
                            r['codigo_usuario'], 
                            r['nome'], 
                            r['idade'], 
                            r['codigo_sexo'], 
                            r['peso'], 
                            r['altura'], 
                            r['codigo_diabete'],
                            r['comorbidades'])
        lista_de_pacientes.append(paciente)
        
    return lista_de_pacientes
