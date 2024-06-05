from dao.pacienteDAO import PacienteDAO
from dao.usuarioDAO import UsuarioDAO
from entidades.glicemia import Glicemia
import jsonpickle
import os

# classe DAO para manipulação de registros de glicemia no banco de dados
class GlicemiaDAO:

    # caminho para o arquivo de dados no computador
    arquivo = 'dados/glicemia.json'

    # construtor da classe
    # se não existir o arquivo, cria um arquivo vazio
    def __init__(self):
        if not os.path.exists(self.arquivo):
            f = open(self.arquivo, 'w')
            buf = jsonpickle.encode([])
            f.write(buf)

    # método de uso interno:
    # carrega todos os registros do arquivo
    def _ler_todos(self):
        f = open(self.arquivo, 'r')
        return jsonpickle.decode(f.read())

    # método de uso interno:
    # grava todos os registos para o arquivo
    def _grava_todos(self, registros):
        f = open(self.arquivo, 'w')
        f.write(jsonpickle.encode(registros))

    # insere um registro no arquivo.
    # devolve o código se gravou com sucesso.
    # devolve -1 se registro pesquisado nao contem o codigo do paciente
    def inserirPorDados(self, codigo_paciente, dia, mes, ano, valor):

        glicemia = Glicemia(None, codigo_paciente, dia, mes, ano, valor)
        return self.inserir(glicemia)
        
    # insere um registro no arquivo.
    # devolve o código se gravou com sucesso.
    # devolve -1 se registro pesquisado nao contem o codigo do paciente
    def inserir(self, glicemia):
        # valida se o campo codigo_paciente está preenchindo
        if glicemia.codigo_paciente == None:
            return -1
        
        glicemias = self._ler_todos()
        
        proximo_codigo = 0
        for r in glicemias:
            if r['codigo'] > proximo_codigo:
                proximo_codigo = r['codigo']
            
        glicemia_dic = {'codigo': proximo_codigo + 1, 'codigo_paciente': glicemia.codigo_paciente, 'dia': glicemia.dia, 'mes': glicemia.mes, 'ano': glicemia.ano, 'valor': glicemia.valor}
        glicemias.append(glicemia_dic)
        self._grava_todos(glicemias)
        return glicemia_dic['codigo']

    # faz uma busca do registro no arquivo pelo codigo especificado
    def buscar_por_codigo(self, codigo):
        glicemias = self._ler_todos()
        for glicemia in glicemias:
            if glicemia['codigo'] == codigo:
                return Glicemia(glicemia['codigo'], glicemia['codigo_paciente'], glicemia['dia'], glicemia['mes'], glicemia['ano'], glicemia['valor'])
        return None

    # faz uma busca no arquivo pelo registro com o codigo dopaciente especificado
    def buscar_por_codigo_paciente(self, codigo_paciente):
        glicemias = self._ler_todos()
        glicemias_do_paciente = []
        for glicemia in glicemias:
            if glicemia['codigo_paciente'] == codigo_paciente:
                glicemia_do_paciente = Glicemia(glicemia['codigo'], glicemia['codigo_paciente'], glicemia['dia'], glicemia['mes'], glicemia['ano'], glicemia['valor'])
                glicemias_do_paciente.append(glicemia_do_paciente)
                
        return glicemias_do_paciente

    # atualiza um objeto no banco
    # se não encontrar devolve -1
    def atualizar(self, glicemia):
        encontrou = 1
        glicemias = self._ler_todos()
        for r in glicemias:
            if r['codigo'] == glicemia.codigo:
                r['codigo_paciente'] = glicemia.codigo_paciente
                r['dia'] = glicemia.dia
                r['mes'] = glicemia.mes
                r['ano'] = glicemia.ano
                r['valor'] = glicemia.valor
                encontrou = 1
                break
        self._grava_todos(glicemias)
        return encontrou

    # remove um registro do banco a partir do codigo especificado
    def apagar(self, codigo):
        glicemias = self._ler_todos()
        glicemias = [glicemia for glicemia in glicemias if glicemia['codigo'] != codigo]
        self._grava_todos(glicemias)

    # retorna um array com todos os registros do banco
    def listar_todos(self):
        glicemias_bd = self._ler_todos()
        glicemias = []
        for reg in glicemias_bd:
            glicemia = Glicemia(reg['codigo'], reg['codigo_paciente'], reg['dia'], reg['mes'], reg['ano'], reg['valor'])
            glicemias.append(glicemia)
        return glicemias

    # fecha a tabela do banco.
    # em base de dados em arquivos, nao faz nada. Mantida para uso futuro em bases que nao forem baseadas em arquivos
    def fechar(self):
        pass
    