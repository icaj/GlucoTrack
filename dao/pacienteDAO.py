from entidades.paciente import Paciente
import jsonpickle
import os

# classe DAO para manipulação de pacientes no banco de dados (arquivos)
class PacienteDAO:

    # caminho para o arquivo de dados no computador
    arquivo = 'dados/pacientes.json'

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
            return jsonpickle.decode(f.read())

    # método de uso interno:
    # grava todos os registos para o arquivo
    def _grava_todos(self, registros):
        with open(self.arquivo, 'w') as f:
            f.write(jsonpickle.encode(registros))

    # insere um registro no arquivo.
    # devolve o código se gravou com sucesso.
    # devolve -1 se registro pesquisado nao contem o codigo do paciente
    def inserirPorDados(self, codigo_usuario, nome, diaNascimento, mesNascimento, anoNascimento, codigo_sexo, peso):

        paciente = Paciente(None, codigo_usuario, nome, diaNascimento, mesNascimento, anoNascimento, codigo_sexo, peso)
        return self.inserir(paciente)

    # insere um paciente no arquivo se não existir um paciente para o mesmo usuario
    # devolve o código do paciente se gravou com sucesso.
    # devolve -1 se já existir um paciente para o mesmo usuario
    def inserir(self, paciente):
        # valida se o campo codigo_usuario está preenchindo
        if paciente.codigo_usuario == None:
            return -2
        
        pacientes = self._ler_todos()
        # verifica se existe paciente com o mesmo codigo de usuario.
        for r in pacientes:
            if r['codigo_usuario'] == paciente.codigo_usuario:
                return -1
        
        proximo_codigo = 0
        for r in pacientes:
            if r['codigo'] > proximo_codigo:
                proximo_codigo = r['codigo']
            
        paciente_dic = {'codigo': proximo_codigo + 1, 
                        'codigo_usuario': paciente.codigo_usuario, 
                        'nome': paciente.nome, 
                        'diaNascimento': paciente.diaNascimento, 
                        'mesNascimento': paciente.mesNascimento, 
                        'anoNascimento': paciente.anoNascimento,
                        'codigo_sexo': paciente.codigo_sexo, 
                        'peso': paciente.peso, 
                        'altura': paciente.altura,
                        'codigo_diabete': paciente.codigo_diabete}
        pacientes.append(paciente_dic)
        self._grava_todos(pacientes)
        return paciente_dic['codigo']

    # faz uma busca no arquivo pelo paciente com o codigo especificado
    # se encontrar devole o objeto encontrado
    # se não encontrar devolve None
    def buscar_por_codigo(self, codigo):
        pacientes = self._ler_todos()
        for paciente in pacientes:
            if paciente['codigo'] == codigo:
                return Paciente(paciente['codigo'], 
                                paciente['codigo_usuario'], 
                                paciente['nome'], 
                                paciente['diaNascimento'], 
                                paciente['mesNascimento'], 
                                paciente['anoNascimento'], 
                                paciente['codigo_sexo'], 
                                paciente['peso'], 
                                paciente['altura'],
                                paciente['codigo_diabete'])
        return None

    # faz uma busca no arquivo pelo paciente com o codigo especificado
    def buscar_por_codigo_usuario(self, codigo_usuario):
        pacientes = self._ler_todos()
        for paciente in pacientes:
            if paciente['codigo_usuario'] == codigo_usuario:
                return Paciente(paciente['codigo'], 
                                paciente['codigo_usuario'], 
                                paciente['nome'], 
                                paciente['diaNascimento'], 
                                paciente['mesNascimento'], 
                                paciente['anoNascimento'], 
                                paciente['codigo_sexo'], 
                                paciente['peso'], 
                                paciente['altura'],
                                paciente['codigo_diabete'])
        return None
    
    # atualiza um objeto paciente no banco
    # se não encontrar devolve -1
    def atualizar(self, paciente):
        encontrou = -1
        # carrega todos os registro do banco numa lista
        pacientes = self._ler_todos()
        # percorre a lsita a procura do paciente com o codigo fornecido
        for r in pacientes:
            if r['codigo'] == paciente.codigo:
                r['nome'] = paciente.nome
                r['diaNascimento'] = paciente.diaNascimento
                r['mesNascimento'] = paciente.mesNascimento
                r['anoNascimento'] = paciente.anoNascimento
                r['codigo_sexo'] = paciente.codigo_sexo
                r['peso'] = paciente.peso
                r['altura'] = paciente.altura
                r['codigo_diabete'] = paciente.codigo_diabete
                encontrou = 1
                break
        self._grava_todos(pacientes)
        # retorno 1 se atualizou com sucesso ou -1 se não encontrou o registro
        return encontrou

    # remove um paciente do banco a partir do codigo especificado
    def apagar(self, codigo):
        # carrega todos os registros do banco de daos para uma lista
        pacientes = self._ler_todos()
        # percorre toda a lista removendo o paciente com o codigo especificado
        pacientes = [paciente for paciente in pacientes if paciente['codigo'] != codigo]
        # grava lista no banco de dados
        self._grava_todos(pacientes)

    # fecha a tabela do banco.
    # em base de dados em arquivos, nao faz nada. Mantida para uso futuro em bases que nao forem baseadas em arquivos
    def fechar(self):
        pass
    