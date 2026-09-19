""" ________________________________________________________________________________"""

# EXERCICIOS DE MATRIZES

""" ________________________________________________________________________________"""

# 1. Soma de Todos os Elementos
# Objetivo: Praticar a iteração em estruturas bidimensionais. Crie uma matriz 3x3 de números inteiros. Escreva um programa que percorra toda a matriz usando laços for aninhados e exiba a soma de todos os seus elementos. 

import random
matriz = []
coluna = 3
linha = 3
soma = 0

for i in range(linha):
    nova_linha = []
    for j in range(coluna):
        numero = random.randint(1,10)
        print(numero)
        nova_linha.append(numero)
        soma = soma + numero
    matriz.append(nova_linha)
print(soma)
print(matriz)



# 2. Multiplicação por Escalar
# Objetivo: Manipulação e atualização de valores via índice. Dada uma matriz 2x2, peça para o usuário digitar um número (fator) através da função input(). Multiplique cada elemento da matriz por esse fator e exiba a matriz resultante.
# Dica: Lembre-se de converter a entrada do teclado para int ou float.

matriz = [
    [1, 2],
    [3, 4]
]

fator = int(input("Digite um número: "))
for i in range(2):
    for j in range(2):
        matriz[i][j] = matriz[i][j] * fator
print(matriz)



# 3. Gerador de Matriz Identidade
# Objetivo: Aplicar lógica condicional dentro de loops. Escreva um programa que peça um número inteiro n e gere uma Matriz Identidade de tamanho n×n (onde os elementos da diagonal principal são 1 e os demais são 0).
# Dica: Um elemento pertence à diagonal principal quando seu índice de linha é igual ao seu índice de coluna (i == j).

n = int(input("Digite o tamanho da matriz: "))
matriz = []

for i in range(n):
    linha = []

    for j in range(n):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)
print(matriz)



# 4. Criando Matrizes com Compreensão de Lista
# Objetivo: Utilizar sintaxe "Pythonica" para criação eficiente de dados. Utilize compreensões de lista aninhadas para criar uma matriz 4x4 onde cada elemento seja o produto dos seus índices (ex: o elemento na posição matriz deve ser 6).
# Dica: A sintaxe básica é [[expressão for j in range(colunas)] for i in range(linhas)].

matriz = [[i * j for j in range(4)] for i in range(4)]

print(matriz)



# 5. Transposição Simples
# Objetivo: Entender a inversão de eixos (linhas por colunas). Crie uma matriz 2x3 (2 linhas e 3 colunas). Escreva um código que gere uma nova matriz que seja a transposta da primeira (3 linhas e 2 colunas), invertendo as posições de cada item.

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
transposta = []

for j in range(3):
    nova_linha = []
    for i in range(2):
        nova_linha.append(matriz[i][j])
    transposta.append(nova_linha)
print(transposta)

