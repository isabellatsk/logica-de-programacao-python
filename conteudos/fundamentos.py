# VARIÁVEIS

nome = "Isa"
idade = 17
altura = 1.75
ativo = True

# Tipagem direta
idade: int = 25
altura: float = 1.75
nome: str = "Maria"
ativo: bool = True

""" ________________________________________________________________________________"""

# TIPOS PRIMITIVOS

texto = "Olá" # str
numero = 10 # int (número inteiro)
decimal = 10.5 # float (número decimal)
verdadeiro = True # bool (booleano)
nulo = None # None é um tipo especial que representa a ausência de valor

""" ________________________________________________________________________________"""

# PRINTAR VALORES

# Print (console.log)
print("Olá mundo")

# Interpolação
nome = "Isa"
print(f"Meu nome é {nome}")

""" ________________________________________________________________________________"""

# INPUT (prompt do JS)

nome = input("Digite seu nome: ") # sempre retorna string

# Converter
idade = int(input("Idade: "))

""" ________________________________________________________________________________"""

# CONDICIONAIS

if idade >= 18:
    print("Maior de idade")
elif idade == 17:
    print("Quase")
else:
    print("Menor")

# Match case (como switchCase) 
def dia_semana(dia):
    match dia:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda"
        case _:
            return "Outro dia"
print(dia_semana(1))  # Saída: Domingo

""" ________________________________________________________________________________"""

# OPERADORES

# Comparação
# == === !=  >  <  >=  <=

# Aritmético
# Soma                      +  
# Subtração                 -  
# Multiplicação             *    
# Resto da divisão          % 
# Divisão retorna inteira   // 
# Divisão retorna float     /
# Potência                  **

# Lógico
#and, or, not

# Identidade
# is, is not

# Obter o resto fracionário de uma divisão a partir de dois números inteiros
# (a % b ) / b

""" ________________________________________________________________________________"""

# LISTAS (Array do JS)
# É usada quando você precisa guardar vários itens e pode alterar depois (adicionar, remover, mudar).
lista = [1, 2, 3]

# Adicionar item
lista.append(4)

# Remover item
lista.pop()

# Acessar item
lista[0]


# SET (conjunto sem ordem e sem itens repetidos)
# É usado quando você precisa garantir que não existam valores repetidos.
numeros = [1, 2, 2, 3]
sem_repeticao = set(numeros)

# Adicionar item
sem_repeticao.add(4)

# Remover item
sem_repeticao.discard(2)

# Verificar item
3 in sem_repeticao


# TUPLA (colecao ordenada e imutavel)
# É usada quando os dados são fixos e não devem mudar. 
tupla = (10, 20, 30)
coordenada = (-29.65, -50.58)

# Acessar item
tupla[0]


# DICIONÁRIO (Objeto do JS)
# É usado quando você quer armazenar dados com chave e valor para acessar rápido. 

pessoa = {
    "nome": "Isa",
    "idade": 17
    pessoa: {
        "fjdd": "dsdssfsf"
    }
}

# Acessar
pessoa["nome"]

# Adicionar
pessoa["altura"] = 1.75

""" ________________________________________________________________________________"""

# MATRIZES

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

""" ________________________________________________________________________________"""

# LOOPS 

# For 
lista = [1, 2, 3] 
for item in lista:
    print(item)
# "in" Percorre os valores diretamente
# "range" Percorre usando índices
# "len" Pra descobrir quantidade

# range(inicio, fim, passo)
for i in range(0, 10, 2):
    print(i)
# print: 0, 1, 2

for i in range(5):
    print(i)
# range(5) → 0 até 4


# enumerate() -> retorna indice e valor ao mesmo tempo
frutas = ["maca", "banana", "uva"]
for indice, fruta in enumerate(frutas):
    print(indice, fruta)
# print:
# 0 maca
# 1 banana
# 2 uva


# While
contador = 0
while contador < 5:
    print(contador)
    contador += 1
    
""" ________________________________________________________________________________"""

# FUNÇÃO

def somar(a, b):
    return a + b

# Chamar
resultado = somar(2, 3)

""" ________________________________________________________________________________"""

# CLASSE (equivalente a class do JS)

class Pessoa:
    def __init__(self, nome): #__init__ = constructor
        self.nome = nome # self = equivalente ao this

    def falar(self):
        print(f"Meu nome é {self.nome}")

# Criar objeto
p = Pessoa("Isa")
p.falar()

""" ________________________________________________________________________________"""

# FUNCOES INTERNAS COMUNS (BUILT-INS)

# sorted() -> retorna uma nova lista ordenada (nao altera a original)
numeros = [7, 2, 10, 1]
numeros_ordenados = sorted(numeros)

# sort() -> ordena a propria lista (altera a lista original)
numeros.sort()

# len() -> quantidade de itens
quantidade_itens = len(numeros)

# sum() -> soma dos valores
soma_numeros = sum(numeros)

# max() e min() -> maior e menor valor
maior_numero = max(numeros)
menor_numero = min(numeros)

# type() -> mostra o tipo de uma variavel
tipo_nome = type(nome)

# abs() -> valor absoluto (sem sinal)
valor_absoluto = abs(-15)

# round() -> arredondamento
arredondado = round(3.14159, 2)

""" ________________________________________________________________________________"""
