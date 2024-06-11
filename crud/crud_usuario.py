from entidades.usuario import Usuario
import jsonpickle
import os


arquivo = 'dados/usuarios.json'

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


def _inserir(usuario):
    usuarios = _ler_todos()




    for r in usuarios:
        if r['email'] == usuario.email:
            print("Já existe usuário com este e-mail")
            return -1


    proximo_codigo = 0
    for r in usuarios:
        if r['codigo'] > proximo_codigo:
            proximo_codigo = r['codigo']


    usuario_dic = {'codigo': proximo_codigo + 1, 'email': usuario.email, 'senha': usuario.senha}


    usuarios.append(usuario_dic)


    _salvar_todos(usuarios)


    return usuario_dic['codigo']

def _atualizar(usuario):
    encontrou = False
    usuarios = _ler_todos()
    for r in usuarios:
        if r['codigo'] == usuario.codigo:
            encontrou = True
            r['email'] = usuario.email
            r['senha'] = usuario.senha
            break

    if(encontrou):
        _salvar_todos(usuarios)
    else:
        print("Usuario não encontrado")
    
    return encontrou






def inserir_usuario(email, senha):
    usuario = Usuario(None, email, senha)
    return _inserir(usuario)




def buscar_usuario(codigo):
    usuarios = _ler_todos()

    for r in usuarios:
        if r['codigo'] == codigo:
            return Usuario(r['codigo'], r['email'], r['senha'])

    print("Usuário não encontrado")
    return -1


def buscar_usuarios():
    usuarios = _ler_todos()

    lista_de_usuarios = []

    for r in usuarios:
        usuario = Usuario(r['codigo'], r['email'], r['senha'])
        lista_de_usuarios.append(usuario)

    return lista_de_usuarios

def atualizar_usuario(codigo, email, senha):




    usuario = Usuario(codigo, email, senha)
    return _atualizar(usuario)


def excluir_usuario(codigo):


    usuarios = _ler_todos()


    nova_lista_de_usuarios = []


    for u in usuarios:
        if u['codigo'] != codigo:


            nova_lista_de_usuarios.append(u)


    _salvar_todos(nova_lista_de_usuarios)




def login(email, senha):
    usuarios = _ler_todos()
 
    for r in usuarios:
        if r['email'] == email:
            if r['senha'] == senha:
                return r['codigo']
            
    return -1
    
