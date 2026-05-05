import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Contato_Empresa:
    nome: str
    cnpj: str
    telefone: str
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CNPJ: {self.cnpj}")
        print(f"Telefone: {self.telefone}\n")

lista_empresas = []
print("= Solicitando dados =")
for i in range(2):
    nova_empresa = Contato_Empresa(
        nome = input("Digite o nome da empresa: "),
        cnpj = input("Digite o CNPJ da empresa: "),
        telefone = input("Digite o telefone da empresa: ")
    )
    print("")
    lista_empresas.append(nova_empresa)

print("\n= Exibindo dados =")
for empresa in lista_empresas:
    Contato_Empresa.mostrar_dados(empresa)
print("\n= Salvando dados =")
with open("lista_empresas.csv", "a", encoding="utf-8") as arquivo_empresas:
    for empresa in lista_empresas:
        arquivo_empresas.write(f"Nome: {empresa.nome}, CNPJ: {empresa.cnpj}, Telefone: {empresa.telefone}\n")
    print("\n= Dados salvos com sucesso! =\n")