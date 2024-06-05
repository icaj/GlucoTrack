from dao.pacienteDAO import PacienteDAO
from dao.usuarioDAO import UsuarioDAO
from entidades.glicemia import Glicemia
import jsonpickle
import os


class GlicemiaDAO:


    arquivo = 'dados/glicemia.json'




    def __init__(self):
        if not os.path.exists(self.arquivo):
            f = open(self.arquivo, 'w')
            buf = jsonpickle.encode([])
            f.write(buf)




    def _ler_todos(self):
        f = open(self.arquivo, 'r')
        return jsonpickle.decode(f.read())




    def _grava_todos(self, registros):
        f = open(self.arquivo, 'w')
        f.write(jsonpickle.encode(registros))






    def inserirPorDados(self, codigo_paciente, dia, mes, ano, valor):

        glicemia = Glicemia(None, codigo_paciente, dia, mes, ano, valor)
        return self.inserir(glicemia)






    def inserir(self, glicemia):


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


    def buscar_por_codigo(self, codigo):
        glicemias = self._ler_todos()
        for glicemia in glicemias:
            if glicemia['codigo'] == codigo:
                return Glicemia(glicemia['codigo'], glicemia['codigo_paciente'], glicemia['dia'], glicemia['mes'], glicemia['ano'], glicemia['valor'])
        return None


    def buscar_por_codigo_paciente(self, codigo_paciente):
        glicemias = self._ler_todos()
        glicemias_do_paciente = []
        for glicemia in glicemias:
            if glicemia['codigo_paciente'] == codigo_paciente:
                glicemia_do_paciente = Glicemia(glicemia['codigo'], glicemia['codigo_paciente'], glicemia['dia'], glicemia['mes'], glicemia['ano'], glicemia['valor'])
                glicemias_do_paciente.append(glicemia_do_paciente)
                
        return glicemias_do_paciente




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


    def apagar(self, codigo):
        glicemias = self._ler_todos()
        glicemias = [glicemia for glicemia in glicemias if glicemia['codigo'] != codigo]
        self._grava_todos(glicemias)


    def listar_todos(self):
        glicemias_bd = self._ler_todos()
        glicemias = []
        for reg in glicemias_bd:
            glicemia = Glicemia(reg['codigo'], reg['codigo_paciente'], reg['dia'], reg['mes'], reg['ano'], reg['valor'])
            glicemias.append(glicemia)
        return glicemias




    def fechar(self):
        pass
    