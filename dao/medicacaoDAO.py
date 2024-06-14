from entidades.medicacao import Medicacao
import jsonpickle
import os

class MedicacaoDAO:

    arquivo = 'dados/medicacoes.json'

    def __init__(self):
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, 'w') as f:
                f.write(jsonpickle.encode([]))

    def _ler_todos(self):
        with open(self.arquivo, 'r') as f:
            return jsonpickle.decode(f.read())

    def _grava_todos(self, registros):
        f = open(self.arquivo, 'w')
        f.write(jsonpickle.encode(registros))

    def inserirPorDados(self, codigo_paciente, nome, hora_inical, periodo, lembrar):
        medicacao = Medicacao(None, codigo_paciente, nome, hora_inical, periodo, lembrar)
        return self.inserir(medicacao)

    def inserir(self, medicacao):

        if medicacao.codigo_paciente == None:
            return -1
        
        medicacoes = self._ler_todos()
        
        proximo_codigo = 0
        for r in medicacoes:
            if r['codigo'] > proximo_codigo:
                proximo_codigo = r['codigo']
            
        medicacao_dic = {'codigo': proximo_codigo + 1, 'codigo_paciente': medicacao.codigo_paciente, 'nome': medicacao.nome, 'hora_inicial': medicacao.hora_inicial, 'periodo': medicacao.periodo, 'lembrar': medicacao.lembrar}
        medicacoes.append(medicacao_dic)
        self._grava_todos(medicacoes)
        return medicacao_dic['codigo']

    def buscar_por_codigo(self, codigo):
        medicacoes = self._ler_todos()
        for medicacao in medicacoes:
            if medicacao['codigo'] == codigo:
                return Medicacao(medicacao['codigo'], medicacao['codigo_paciente'], medicacao['nome'], medicacao['hora_inicial'], medicacao['periodo'], medicacao['lembrar'])
        return None

    def buscar_por_codigo_paciente(self, codigo_paciente):
        medicacoes = self._ler_todos()
        medicacoes_do_paciente = []
        for medicacao in medicacoes:
            if medicacao['codigo_paciente'] == codigo_paciente:
                medicacao_do_paciente = Medicacao(medicacao['codigo'], medicacao['codigo_paciente'], medicacao['nome'], medicacao['hora_inicial'], medicacao['periodo'], medicacao['lembrar'])
                medicacoes_do_paciente.append(medicacao_do_paciente)
                
        return medicacoes_do_paciente

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

    def apagar(self, codigo):
        medicacoes = self._ler_todos()
        medicacoes = [medicacao for medicacao in medicacoes if medicacao['codigo'] != codigo]
        self._grava_todos(medicacoes)

