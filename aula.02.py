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
        print(f"Autor: {self.autor}")
        print(f"Categoria: {self.categoria}\n")
        print(f"Preço: R${self.preco:.2f}\n")

lista_livros = []
print("--- SISTEMA DE CADASTRO DE LIVROS ---")
print("1. Adicionar livro")
print("2. Listar livros")
print("3. Sair")
print("= Solicitando dados =")
opcao = input("Escolha uma opção: ")
if opcao == "1":
    print("\n= Adicionando livro =")
    opcao_adicionar = "S"
    while opcao_adicionar.upper() == "S":
        livro = Livro(
            nome = input("Digite o nome do livro: "),
            autor = input("Digite o autor do livro: "),
            categoria = input("Digite a categoria do livro: "),
            preco = float(input("Digite o preço do livro: "))
        )
        print("")
        lista_livros.append(livro)
        opcao_adicionar = input("Deseja adicionar outro livro? (S/N): ")

elif opcao == "2":
    print("\n= Listando livros =")
    for livro in lista_livros:
        Livro.mostrar_dados(livro)
elif opcao == "3":
    print("\n= Sair/s =")
else:
    print("\n= Opção inválida =")
    
    print("")
    lista_livros.append(lista_livros)

print("\n= Exibindo dados =")
for livro in lista_livros:
    Livro.mostrar_dados(livro)
print("\n= Salvando dados =")
with open("catalogo_livros.csv", "a", encoding="utf-8") as arquivo_livros:
    for livro in lista_livros:
        arquivo_livros.write(f"Nome: {livro.nome}, Autor: {livro.autor}, Categoria: {livro.categoria}\n")
    print("\n= Dados salvos com sucesso! =\n")
print("= FIM DO PROGRAMA = ")