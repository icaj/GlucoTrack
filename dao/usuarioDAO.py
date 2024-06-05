from entidades.usuario import Usuario
import jsonpickle
import os


class UsuarioDAO:


    arquivo = 'dados/usuarios.json'




    def __init__(self):
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, 'w') as f:
                f.write(jsonpickle.encode([]))




    def _ler_todos(self):
        with open(self.arquivo, 'r') as f:
            buf = f.read()
            return jsonpickle.decode(buf)




    def _grava_todos(self, registros):
        with open(self.arquivo, 'w') as f:
            f.write(jsonpickle.encode(registros))






    def inserirPorDados(self, email, senha):

        usuario = Usuario(None, email, senha)
        return self.inserir(usuario)


    def inserir(self, usuario):
        usuarios = self._ler_todos()




        for r in usuarios:
            if r['email'] == usuario.email:
                return -1


        proximo_codigo = 0
        for r in usuarios:
            if r['codigo'] > proximo_codigo:
                proximo_codigo = r['codigo']


        usuario_dic = {'codigo': proximo_codigo + 1, 'email': usuario.email, 'senha': usuario.senha}


        usuarios.append(usuario_dic)


        self._grava_todos(usuarios)


        return usuario_dic['codigo']




    def buscar(self, codigo):
        usuarios = self._ler_todos()
        for usuario in usuarios:
            if usuario['codigo'] == codigo:
                return Usuario(usuario['codigo'], usuario['email'], usuario['senha'])
        return None




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


    def apagar(self, codigo):


        usuarios = self._ler_todos()


        usuarios = [usuario for usuario in usuarios if usuario['codigo'] != codigo]


        self._grava_todos(usuarios)




    def logar(self, email, senha):
        usuarios = self._ler_todos()
        for r in usuarios:
            if r['email'] == email:
                if r['senha'] == senha:
                    return r['codigo']
        return -1




    def fechar(self):
        pass
    