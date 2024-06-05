from entidades.registro_nutricional import RegistroNutricional
import jsonpickle
import os


class RegistroNutricionalDAO:


    arquivo = 'dados/registros_nutricionais.json'




    def __init__(self):
        if not os.path.exists(self.arquivo):
            f = open(self.arquivo, 'w')
            buf = jsonpickle.encode([])
            f.write(buf)




    def _ler_todos(self):
        f = open(self.arquivo, 'r')
        return jsonpickle.decode(f.read())




    def _grava_todos(self, registros):
        f =  open(self.arquivo, 'w')
        f.write(jsonpickle.encode(registros))

    def inserirPorDados(self, codigo_paciente, dia, mes, ano, calorias, proteinas, gorduras, carboidratos):
        registro_nutricional = RegistroNutricional(codigo_paciente, dia, mes, ano, calorias, proteinas, gorduras, carboidratos)
        return self.inserir(registro_nutricional)






    def inserir(self, registro_nutricional):


        if registro_nutricional.codigo_paciente == None:
            return -2
        
        registros_nutricionais = self._ler_todos()
        
        proximo_codigo = 0
        for r in registros_nutricionais:
            if r['codigo'] > proximo_codigo:
                proximo_codigo = r['codigo']
            
        registro_nutricional_dtc = {'codigo': proximo_codigo + 1, 
                                    'codigo_paciente': registro_nutricional.codigo_paciente, 
                                    'dia': registro_nutricional.dia, 
                                    'mes': registro_nutricional.mes, 
                                    'ano': registro_nutricional.ano, 


                                    'calorias': 4 * (registro_nutricional.proteinas + registro_nutricional.carboidratos) + 9 * (registro_nutricional.gorduras),
                                    'proteinas': registro_nutricional.proteinas,
                                    'gorduras': registro_nutricional.gorduras,
                                    'carboidratos': registro_nutricional.carboidratos}
        registros_nutricionais.append(registro_nutricional_dtc)
        self._grava_todos(registros_nutricionais)
        return registro_nutricional_dtc['codigo']


    def buscar_por_codigo(self, codigo):
        registros_nutricionais = self._ler_todos()
        for registro in registros_nutricionais:
            if registro['codigo'] == codigo:
                return RegistroNutricional(registro['codigo'], registro['codigo_paciente'], registro['dia'], registro['mes'], registro['ano'], registro['calorias'], registro['proteinas'], registro['gorduras'], registro['carboidratos'])
        return None


    def buscar_por_codigo_paciente(self, codigo_paciente):
        registros = self._ler_todos()
        registros_do_paciente = []
        for r in registros:
            if r['codigo_paciente'] == codigo_paciente:
                registro_do_paciente = RegistroNutricional(r['codigo'], r['codigo_paciente'], r['dia'], r['mes'], r['ano'], r['calorias'], r['proteinas'], r['gorduras'], r['carboidratos'])
                registros_do_paciente.append(registro_do_paciente)
                
        return registros_do_paciente




    def atualizar(self, registro_nutricional):
        encontrou = 1
        registros_nutricionais = self._ler_todos()
        for r in registros_nutricionais:
            if r['codigo'] == registro_nutricional.codigo:
                r['dia'] = registro_nutricional.dia
                r['mes'] = registro_nutricional.mes
                r['ano'] = registro_nutricional.ano
                r['calorias'] = registro_nutricional.calorias
                r['proteinas'] = registro_nutricional.proteinas
                r['gorduras'] = registro_nutricional.gorduras
                r['carboidratos'] = registro_nutricional.carboidratos
                encontrou = 1
                break
        self._grava_todos(registros_nutricionais)
        return encontrou


    def apagar(self, codigo):
        registros_nutricionais = self._ler_todos()
        registros_nutricionais = [registro_nutricional for registro_nutricional in registros_nutricionais if registro_nutricional['codigo'] != codigo]
        self._grava_todos(registros_nutricionais)




    def fechar(self):
        pass
