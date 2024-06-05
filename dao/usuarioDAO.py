from entidades.usuario import Usuario
import jsonpickle
import os

# classe DAO para manipulação de usuarios no banco de dados (arquivos)
class UsuarioDAO:

    # caminho para o arquivo de dados no computador
    arquivo = 'dados/usuarios.json'

    # construtor da classe
    # se não existir o arquivo, cria um arquivo vazio
    def __init__(self):
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, 'w') as f:
                f.write(jsonpickle.encode([]))

    # método de uso interno:
    # carrega todos os registros do arquivo para a memória
    def _ler_todos(self):
        with open(self.arquivo, 'r') as f:
            buf = f.read()
            return jsonpickle.decode(buf)

    # método de uso interno:
    # grava todos os registos para o arquivo
    def _grava_todos(self, registros):
        with open(self.arquivo, 'w') as f:
            f.write(jsonpickle.encode(registros))

    # insere um registro no arquivo.
    # devolve o código se gravou com sucesso.
    # devolve -1 se registro pesquisado nao contem o codigo do paciente
    def inserirPorDados(self, email, senha):

        usuario = Usuario(None, email, senha)
        return self.inserir(usuario)
        
    # insere um usuario no banco de dados se não existir um usuário com o mesmo e-mail cadastrado
    def inserir(self, usuario):
        usuarios = self._ler_todos()
        # verifica se existe usuario com o mesmo email
        # se houver, retorna -1 para sinalizar erro
        for r in usuarios:
            if r['email'] == usuario.email:
                return -1
        
        # calcula o valor do código do novo usuário a partir do codigo do último usuário + 1
        proximo_codigo = 0
        for r in usuarios:
            if r['codigo'] > proximo_codigo:
                proximo_codigo = r['codigo']

        # cria um objeto na memorio com o registro do novo usuario a ser inserido no banco de dados    
        usuario_dic = {'codigo': proximo_codigo + 1, 'email': usuario.email, 'senha': usuario.senha}
        # adiciona o novo usuário aos usuários do banco
        usuarios.append(usuario_dic)
        # grava todos os registros no banco
        self._grava_todos(usuarios)
        # retorna o código do novo usuário cadastrado
        return usuario_dic['codigo']

    # devolve o objeto usuario no banco a partir do codigo especificado
    # se não encontrar retona None
    def buscar(self, codigo):
        usuarios = self._ler_todos()
        for usuario in usuarios:
            if usuario['codigo'] == codigo:
                return Usuario(usuario['codigo'], usuario['email'], usuario['senha'])
        return None

    # atualiza um objeto usuario no banco
    # se não encontrar devolve -1
    def atualizar(self, usuario):
        encontrou = -1
        usuarios = self._ler_todos()
        for r in usuarios:
            if r['codigo'] == usuario.codigo:
                r['email'] = usuario.email
                r['senha'] = usuario.senha
                encontrou = 1
                break
        self._grava_todos(usuarios)
        return encontrou

    # remove um usuario do banco a partir do codigo especificado
    def apagar(self, codigo):
        # carrega todos os usuarios do banco em uma lista
        usuarios = self._ler_todos()
        # percorre toda a lista removendo apenas o objeto que possui o código igual ao especificado
        usuarios = [usuario for usuario in usuarios if usuario['codigo'] != codigo]
        # grava a lista sem o registro excluido no banco
        self._grava_todos(usuarios)

    # metodo logar que apenas devolve o codigo do usuario a partir do email e senha informada
    # devolve -1 se nao encontrar
    def logar(self, email, senha):
        usuarios = self._ler_todos()
        for r in usuarios:
            if r['email'] == email:
                if r['senha'] == senha:
                    return r['codigo']
        return -1
    # fecha a tabela do banco.
    # em base de dados em arquivos, nao faz nada. Mantida para uso futuro em bases que nao forem baseadas em arquivos
    def fechar(self):
        pass
    