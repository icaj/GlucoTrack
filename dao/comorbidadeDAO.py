from entidades.comorbidade import Comorbidade
import jsonpickle
import os


class ComorbidadeDAO:


    arquivo = 'dados/comorbidades.json'




    def __init__(self):
        if not os.path.exists(self.arquivo):
            tipos = [ { "codigo": 1, "descricao": "Hipertensão" },
                      { "codigo": 2, "descricao": "Cardíaco(a)" } ]
            with open(self.arquivo, 'w') as f:
                f.write(jsonpickle.encode([]))

            self._grava_todos(tipos)




    def _ler_todos(self):
        with open(self.arquivo, 'r') as f:
            return jsonpickle.decode(f.read())




    def _grava_todos(self, registros):
        with open(self.arquivo, 'w') as f:
            f.write(jsonpickle.encode(registros))




    def buscar(self, codigo):
        comorbidades = self._ler_todos()
        for comorbidade in comorbidades:
            if comorbidade['codigo'] == codigo:
                return Comorbidade(comorbidade['codigo'], comorbidade['descricao'])
        return None


    def listar_todos(self):
        tipos_diabete_bd = self._ler_todos()
        tipos_diabete = []
        for reg in tipos_diabete_bd:
            comorbidade = Comorbidade(reg['codigo'], reg['descricao'])
            tipos_diabete.append(comorbidade)
        return tipos_diabete




    def fechar(self):
        pass
    