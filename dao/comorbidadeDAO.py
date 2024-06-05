from entidades.comorbidade import Comorbidade
import jsonpickle
import os

# classe DAO para manipulação de usuarios no banco de dados (arquivos)
class ComorbidadeDAO:

    # caminho para o arquivo de dados no computador
    arquivo = 'dados/comorbidades.json'

    # construtor da classe
    # se não existir o arquivo, cria um arquivo vazio
    def __init__(self):
        if not os.path.exists(self.arquivo):
            tipos = [ { "codigo": 1, "descricao": "Hipertensão" },
                      { "codigo": 2, "descricao": "Cardíaco(a)" } ]
            with open(self.arquivo, 'w') as f:
                f.write(jsonpickle.encode([]))

            self._grava_todos(tipos)

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

    # devolve o objeto no banco a partir do codigo especificado
    # se não encontrar retona None
    def buscar(self, codigo):
        comorbidades = self._ler_todos()
        for comorbidade in comorbidades:
            if comorbidade['codigo'] == codigo:
                return Comorbidade(comorbidade['codigo'], comorbidade['descricao'])
        return None

    # retorna um array com todos os registros do banco
    def listar_todos(self):
        tipos_diabete_bd = self._ler_todos()
        tipos_diabete = []
        for reg in tipos_diabete_bd:
            comorbidade = Comorbidade(reg['codigo'], reg['descricao'])
            tipos_diabete.append(comorbidade)
        return tipos_diabete
        
    # fecha a tabela do banco.
    # em base de dados em arquivos, nao faz nada. Mantida para uso futuro em bases que nao forem baseadas em arquivos
    def fechar(self):
        pass
    