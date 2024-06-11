from entidades.sexo import Sexo
import jsonpickle
import os


class SexoDAO:


    arquivo = 'dados/sexo.json'




    def __init__(self):
        if not os.path.exists(self.arquivo):
            tipos = [ { "codigo": "F", "descricao": "Feminino" },
                      { "codigo": "M", "descricao": "Masculino" }]

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
        sexos = self._ler_todos()
        for sexo in sexos:
            if sexo['codigo'] == codigo:
                return Sexo(sexo['codigo'], sexo['descricao'])
        return None


    def listar_todos(self):
        sexos_bd = self._ler_todos()
        sexos = []
        for reg in sexos_bd:
            sexo = Sexo(reg['codigo'], reg['descricao'])
            sexos.append(sexo)
        return sexos




    def fechar(self):
        pass
    