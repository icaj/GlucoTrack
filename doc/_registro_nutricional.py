import jsonpickle
from datetime import datetime
import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def nome_registro_alimentos():
    print("=========================================================================================")
    print("======================== Registro de Alimentos - Versão 1.0 =============================")
    print('')

class RegistroNutricional:
    def __init__(self):
        self.registros = []
        self.carregar_de_json("alimentos.json")

    def adicionar_registro(self):
        limpa_tela()
        nome_registro_alimentos()
        alimento = input("Nome do alimento: ")
        carboidratos = float(input("Carboidratos (em gramas): "))
        proteinas = float(input("Proteínas (em gramas): "))
        gorduras = float(input("Gorduras (em gramas): "))
        
        calorias = (carboidratos * 4) + (proteinas * 4) + (gorduras * 9)
        print(f"Calorias: {calorias}")

        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        registro = {
            "Data e Hora": data_hora,
            "Alimento": alimento,
            "Carboidratos (g)": carboidratos,
            "Proteinas (g)": proteinas,
            "Calorias": calorias,
            "Gorduras (g)": gorduras
        }
        self.registros.append(registro)
        self.salvar_em_json("alimentos.json")
        input("Pressione Enter para continuar...")

    def listar_registros(self):
        limpa_tela()
        nome_registro_alimentos()
        if not self.registros:
            print("Nenhum registro encontrado.")
        else:
            for idx, registro in enumerate(self.registros, start=1):
                print(f"Registro {idx}:")
                for chave, valor in registro.items():
                    print(f"  {chave}: {valor}")
                print('')
        input("Pressione Enter para continuar...")

    def editar_registro(self):
        limpa_tela()
        nome_registro_alimentos()
        self.listar_registros()
        idx = int(input("Digite o número do registro que deseja editar: ")) - 1
        
        if 0 <= idx < len(self.registros):
            registro = self.registros[idx]
            for chave in ["Alimento", "Carboidratos (g)", "Proteinas (g)", "Gorduras (g)"]:
                novo_valor = input(f"{chave} atual ({registro[chave]}): ")
                if novo_valor:
                    registro[chave] = float(novo_valor) if chave != "Alimento" else novo_valor
            
            registro["Calorias"] = (registro["Carboidratos (g)"] * 4) + (registro["Proteinas (g)"] * 4) + (registro["Gorduras (g)"] * 9)
            self.salvar_em_json("alimentos.json")
            print("Registro atualizado com sucesso.")
        else:
            print("Registro não encontrado.")
        input("Pressione Enter para continuar...")

    def apagar_registro(self):
        limpa_tela()
        nome_registro_alimentos()
        self.listar_registros()
        idx = int(input("Digite o número do registro que deseja apagar: ")) - 1
        
        if 0 <= idx < len(self.registros):
            del self.registros[idx]
            self.salvar_em_json("alimentos.json")
            print("Registro apagado com sucesso.")
        else:
            print("Registro não encontrado.")
        input("Pressione Enter para continuar...")

    def salvar_em_json(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'w') as file:
                file.write(jsonpickle.encode(self.registros))
            print("\nAlimento(s) registrado(s) com sucesso.")
        except Exception as e:
            print(f"Erro ao registrar o alimento: {e}")

    def carregar_de_json(self, nome_arquivo):
        if os.path.exists(nome_arquivo):
            try:
                with open(nome_arquivo, 'r') as file:
                    self.registros = jsonpickle.decode(f.read())
            except Exception as e:
                print(f"Erro ao carregar registros: {e}")

def exibir_menu():
    while True:
        limpa_tela()
        nome_registro_alimentos()
        print("1 - Registrar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Apagar")
        print("0 - Sair\n")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            registro.adicionar_registro()
        elif opcao == '2':
            registro.listar_registros()
        elif opcao == '3':
            registro.editar_registro()
        elif opcao == '4':
            registro.apagar_registro()
        elif opcao == '0':
            break
        else:
            print("Opção inválida, por favor tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    limpa_tela()
    nome_registro_alimentos()
    registro = RegistroNutricional()
    exibir_menu()