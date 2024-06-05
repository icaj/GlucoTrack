from entidades.usuario import Usuario
import jsonpickle
import os

# caminho para o arquivo de dados no computador
arquivo = 'dados/usuarios.json'

def _criar_bd():
    # se não existir o arquivo, cria um arquivo vazio
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            buf = jsonpickle.encode([])
            f.write(buf)

def _ler_todos():
    _criar_bd()

    # carrega todos os registros do arquivo para a memória
    with open(arquivo, 'r') as f:
        return jsonpickle.decode(f.read())

def _salvar_todos(registros):
    _criar_bd()
    with open(arquivo, 'w') as f:
        buf = jsonpickle.encode(registros)
        f.write(buf)

# insere um usuario no banco de dados se não existir um usuário com o mesmo e-mail cadastrado
def _inserir(usuario):
    usuarios = _ler_todos()
    # verifica se existe usuario com o mesmo email
    # se houver, retorna -1 para sinalizar erro
    for r in usuarios:
        if r['email'] == usuario.email:
            print("Já existe usuário com este e-mail")
            return -1
        
    # calcula o valor do código do novo usuário a partir do codigo do último usuário + 1
    proximo_codigo = 0
    for r in usuarios:
        if r['codigo'] > proximo_codigo:
            proximo_codigo = r['codigo']

    # cria um objeto na memoria com o registro do novo usuario a ser inserido no banco de dados    
    usuario_dic = {'codigo': proximo_codigo + 1, 'email': usuario.email, 'senha': usuario.senha}
    # adiciona o novo usuário aos usuários do banco
    usuarios.append(usuario_dic)
    # grava todos os registros no banco
    _salvar_todos(usuarios)
    # retorna o código do novo usuário cadastrado
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

# insere um usuario no arquivo json
# devolve o código do novo usuario se gravou com sucesso.
# devolve -1 se registro não encontrado
def inserir_usuario(email, senha):
    usuario = Usuario(None, email, senha)
    return _inserir(usuario)
        
# devolve o objeto usuario no banco a partir do codigo especificado
# se não encontrar retorna -1
def buscar_usuario(codigo):
    usuarios = _ler_todos()

    for r in usuarios:
        if r['codigo'] == codigo:
            return Usuario(r['codigo'], r['email'], r['senha'])

    print("Usuário não encontrado")
    return -1

# devolve todos os usuarios cadastrados
def buscar_usuarios():
    usuarios = _ler_todos()

    lista_de_usuarios = []

    for r in usuarios:
        usuario = Usuario(r['codigo'], r['email'], r['senha'])
        lista_de_usuarios.append(usuario)

    return lista_de_usuarios

def atualizar_usuario(codigo, email, senha):
    # atualiza um objeto usuario no banco
    # se não encontrar devolve -1
    usuario = Usuario(codigo, email, senha)
    return _atualizar(usuario)

# remove um usuario do banco a partir do codigo especificado
def excluir_usuario(codigo):
    # carrega todos os usuarios do banco em uma lista
    usuarios = _ler_todos()

    # cria uma lsta vazia que receberá todos os usuarios do banco, menos o usuário que se quer excluir
    nova_lista_de_usuarios = []

    # percorre toda a lista removendo apenas o objeto que possui o código igual ao especificado
    for u in usuarios:
        if u['codigo'] != codigo:
            # adiciona na nova lista apenas os usuários que não tiverem o código especificado
            nova_lista_de_usuarios.append(u)

    # grava a lista sem o registro excluido no banco
    _salvar_todos(nova_lista_de_usuarios)


# metodo logar que apenas devolve o codigo do usuario a partir do email e senha informada
# devolve -1 se nao encontrar
def login(email, senha):
    usuarios = _ler_todos()
 
    for r in usuarios:
        if r['email'] == email:
            if r['senha'] == senha:
                return r['codigo']
            
    return -1
    
