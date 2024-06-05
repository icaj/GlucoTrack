from entidades.paciente import Paciente
import jsonpickle
import os


class PacienteDAO:


    arquivo = 'dados/pacientes.json'




    def __init__(self):
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, 'w') as f:
                f.write(jsonpickle.encode([]))




    def _ler_todos(self):
        with open(self.arquivo, 'r') as f:
            return jsonpickle.decode(f.read())




    def _grava_todos(self, registros):
        with open(self.arquivo, 'w') as f:
            f.write(jsonpickle.encode(registros))






    def inserirPorDados(self, codigo_usuario, nome, diaNascimento, mesNascimento, anoNascimento, codigo_sexo, peso):

        paciente = Paciente(None, codigo_usuario, nome, diaNascimento, mesNascimento, anoNascimento, codigo_sexo, peso)
        return self.inserir(paciente)






    def inserir(self, paciente):


        if paciente.codigo_usuario == None:
            return -2
        
        pacientes = self._ler_todos()


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




    def atualizar(self, paciente):
        encontrou = -1


        pacientes = self._ler_todos()


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


        return encontrou


    def apagar(self, codigo):


        pacientes = self._ler_todos()


        pacientes = [paciente for paciente in pacientes if paciente['codigo'] != codigo]


        self._grava_todos(pacientes)




    def fechar(self):
        pass
    