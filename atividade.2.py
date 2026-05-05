import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Funcionario:
    nome: str
    idade: int

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}\n")

QUANTIDADE_FUNCIONARIOS = 2
lista_funcionarios = []

print("= Solicitando dados =")
for i in range(QUANTIDADE_FUNCIONARIOS):
    novo_funcionario = Funcionario(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: "))
    )
    print("")
    lista_funcionarios.append(novo_funcionario)

print("\n= Exibindo dados =")
for funcionario in lista_funcionarios:
    Funcionario.mostrar_dados(funcionario)

print("\n= Salvando dados =")
with open("dados_funcionarios.txt", "a", encoding="utf-8") as arquivo_funcionarios:
    for funcionario in lista_funcionarios:
        arquivo_funcionarios.write(f"Nome: {funcionario.nome}, Idade: {funcionario.idade}\n")
    print("\n= Dados salvos com sucesso! =\n")

print("= FIM DO PROGRAMA = ")