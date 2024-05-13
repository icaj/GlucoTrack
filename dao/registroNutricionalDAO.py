from entidades.medicacao import Medicacao
import json
import os

# classe DAO para manipulação de medicacoes no banco de dados (arquivos)
class RegistroNutricionalDAO:

    # caminho para o arquivo de dados no computador
    arquivo = 'dados/registro_nutricional.json'

    # construtor da classe
    # se não existir o arquivo, cria um arquivo vazio
    def __init__(self):
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, 'w') as f:
                json.dump([], f)

    # método de uso interno:
    # carrega todos os registros do arquivo para a memória
    def _ler_todos(self):
        with open(self.arquivo, 'r') as f:
            return json.load(f)

    # método de uso interno:
    # grava todos os registos para o arquivo
    def _grava_todos(self, registros):
        with open(self.arquivo, 'w') as f:
            json.dump(registros, f, indent=4)

    # insere um medicacao no arquivo se não existir um medicacao para o mesmo usuario
    # devolve o código do medicacao se gravou com sucesso.
    # devolve -1 se já existir um medicacao para o mesmo usuario
    def inserir(self, medicacao):
        # valida se o campo codigo_paciente está preenchindo
        if medicacao.codigo_paciente == None:
            return -2
        
        medicacoes = self._ler_todos()
        
        proximo_codigo = 0
        for r in medicacoes:
            if r['codigo'] > proximo_codigo:
                proximo_codigo = r['codigo']
            
        medicacao_dic = {'codigo': proximo_codigo + 1, 'codigo_paciente': medicacao.codigo_paciente, 'nome': medicacao.nome, 'hora_inicial': medicacao.hora_inicial, 'periodo': medicacao.periodo, 'lembrar': medicacao.lembrar}
        medicacoes.append(medicacao_dic)
        self._grava_todos(medicacoes)
        return medicacao_dic['codigo']

    # faz uma busca no arquivo pelo medicacao com o codigo especificado
    def buscar_por_codigo(self, codigo):
        medicacoes = self._ler_todos()
        for medicacao in medicacoes:
            if medicacao['codigo'] == codigo:
                return Medicacao(medicacao['codigo'], medicacao['codigo_paciente'], medicacao['nome'], medicacao['hora_inicial'], medicacao['periodo'], medicacao['lembrar'])
        return None

    # faz uma busca no arquivo pelo medicacao com o codigo especificado
    def buscar_por_codigo_paciente(self, codigo_paciente):
        medicacoes = self._ler_todos()
        medicacoes_do_paciente = []
        for medicacao in medicacoes:
            if medicacao['codigo_paciente'] == codigo_paciente:
                medicacao_do_paciente = Medicacao(medicacao['codigo'], medicacao['codigo_paciente'], medicacao['nome'], medicacao['hora_inicial'], medicacao['periodo'], medicacao['lembrar'])
                medicacoes_do_paciente.append(medicacao_do_paciente)
                
        return medicacoes_do_paciente

    # atualiza um objeto medicacao no banco
    # se não encontrar devolve -1
    def atualizar(self, medicacao):
        encontrou = 1
        medicacoes = self._ler_todos()
        for r in medicacoes:
            if r['codigo'] == medicacao.codigo:
                r['nome'] = medicacao.nome
                r['hora_inicial'] = medicacao.hora_inicial
                r['periodo'] = medicacao.periodo
                r['lembrar'] = medicacao.lembrar
                encontrou = 1
                break
        self._grava_todos(medicacoes)
        return encontrou

    # remove uma medicacao do banco a partir do codigo especificado
    def apagar(self, codigo):
        medicacoes = self._ler_todos()
        medicacoes = [medicacao for medicacao in medicacoes if medicacao['codigo'] != codigo]
        self._grava_todos(medicacoes)

    # fecha a tabela do banco.
    # em base de dados em arquivos, nao faz nada. Mantida para uso futuro em bases que nao forem baseadas em arquivos
    def fechar(self):
        pass
    