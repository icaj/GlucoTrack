

class Medicacao:

    def __init__(self, codigo, codigo_paciente, nome, dosagem, hora_inicial, periodicidade, lembrar):
        self.codigo = codigo
        self.codigo_paciente = codigo_paciente
        self.nome = nome
        self.dosagem = dosagem
        self.hora_inicial = hora_inicial
        self.periodicidade = periodicidade
        self.lembrar = lembrar
