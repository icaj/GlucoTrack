from entidades.tipo_diabete import TipoDiabete
import jsonpickle
import os


class TipoDiabeteDAO:


    arquivo = 'dados/tipos_diabete.json'




    def __init__(self):
        if not os.path.exists(self.arquivo):
            tipos = [ { "codigo": 1, "descricao": "Tipo 1" },
                      { "codigo": 2, "descricao": "Tipo 2" },
                      { "codigo": 3, "descricao": "Gestacional" },
                      { "codigo": 4, "descricao": "Outros"} ]

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
        tipos_diabete = self._ler_todos()
        for tipo_diabete in tipos_diabete:
            if tipo_diabete['codigo'] == codigo:
                return TipoDiabete(tipo_diabete['codigo'], tipo_diabete['descricao'])
        return None


    def listar_todos(self):
        tipos_diabete_bd = self._ler_todos()
        tipos_diabete = []
        for reg in tipos_diabete_bd:
            tipo_diabete = TipoDiabete(reg['codigo'], reg['descricao'])
            tipos_diabete.append(tipo_diabete)
        return tipos_diabete




    def fechar(self):
        pass
    