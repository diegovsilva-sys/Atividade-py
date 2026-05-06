import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class Empresa:
    nome: str
    cnpj: str
    telefone: str

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'CPNJ: {self.cnpj}')
        print(f'Telefone: {self.telefone}\n')


QUANTIDADE_FUNCIONARIOS = 1
lista_empresas = []

print('= Solicitnado dados =')
for i in range(QUANTIDADE_FUNCIONARIOS):
    nova_empresa = Empresa(
        nome=input('Digite seu nome: '),
        cnpj=input('Digite o CPNJ: '),
        telefone=input('Digite seu telefone: ')
    )
    print('')
    lista_empresas.append(nova_empresa)

print('= Salvando dados =')
with open('contato_empresas.csv', 'a', encoding='utf-8') as arquivo:
    for empresa in lista_empresas:
        arquivo.write(f'{empresa.nome}, {empresa.cnpj}, {empresa.telefone}\n')
    print('Salvo com sucesso!')

print('= Fim do programa. =')