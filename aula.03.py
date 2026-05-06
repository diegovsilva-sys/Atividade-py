import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}@gmail.com")
        print(f"Telefone: {self.telefone}\n")

lista_funcionarios = []

print("= Solicitando dados =")

while True:
    novo_funcionario = Funcionario(
        nome = input("\nDigite seu nome: "),
        email = input("Digite seu e-mail: "),
        telefone = input("Digite seu telefone: ")
    )
    continuar = input("Deseja cadastrar outro funcionário? (S/N): ")
    
    if novo_funcionario.nome == "N":
        break

    lista_funcionarios.append(novo_funcionario)

print("\n= Exibindo dados =")
for funcionario in lista_funcionarios:
    funcionario.mostrar_dados()