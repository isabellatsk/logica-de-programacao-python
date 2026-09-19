""" ________________________________________________________________________________"""

# EXERCICIOS DE FOR (LISTAS)

""" ________________________________________________________________________________"""

# 1
lista = []

for i in range(5):
    numero = int(input("Digite um número: "))
    lista.append(numero)

print("Lista:", lista)

# """ ________________________________________________________________________________"""

# 2
lista = []
soma = 0

for i in range(6):
    numero = int(input("Digite um número: "))
    lista.append(numero)
    soma += numero

print("Lista:", lista)
print("Soma:", soma)

# """ ________________________________________________________________________________"""

# 3
lista = []

for i in range(5):
    numero = int(input("Digite um numero: "))
    lista.append(numero)

print("Números pares:")
for num in lista:
    if num % 2 == 0:
        print(num)

# """ ________________________________________________________________________________"""

# 4
lista = []

for i in range(8):
    numero = int(input("Digite um número: "))
    lista.append(numero)

print("Maior:", max(lista))
print("Menor:", min(lista))

# """ ________________________________________________________________________________"""

# 5
lista = []
positivos = 0

for i in range(7):
    numero = int(input("Digite um número: "))
    lista.append(numero)
    
    if numero > 0:
        positivos += 1

print("Quantidade de positivos:", positivos)

# """ ________________________________________________________________________________"""

# 6
nomes = []

for i in range(5):
    nome = input("Digite um nome: ")
    nomes.append(nome)

for nome in nomes:
    print(nome)

# """ ________________________________________________________________________________"""

# 7
lista = []
dobro = []

for i in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)

for num in lista:
    dobro.append(num * 2)

print("Lista original:", lista)
print("Nova lista:", dobro)

# """ ________________________________________________________________________________"""

# 8
lista = []

for i in range(6):
    numero = int(input("Digite um número: "))
    lista.append(numero)

busca = int(input("Digite um número para buscar: "))

if busca in lista:
    print("Número encontrado na lista!")
else:
    print("Número não encontrado.")

# """ ________________________________________________________________________________"""

# 9
lista = []

for i in range(8):
    numero = int(input("Digite um número: "))
    lista.append(numero)

for i in range(len(lista) - 1, -1, -1):
    print(lista[i])

# """ ________________________________________________________________________________"""

# 10
lista = []
pares = []
impares = []

for i in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)
    
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lista original:", lista)
print("Pares:", pares)
print("Ímpares:", impares)

# """ ________________________________________________________________________________"""

# 11
lista = []
soma = 0

for i in range(5):
    numero = int(input("Digite um número: "))
    lista.append(numero)

for num in lista:
    soma += num

media = soma / len(lista)
print("Média:", media)

# """ ________________________________________________________________________________"""

# 12
lista = []
maiores = []

for i in range(6):
    numero = int(input("Digite um número: "))
    lista.append(numero)
    
    if numero > 10:
        maiores.append(numero)

print("Números maiores que 10:", maiores)

# """ ________________________________________________________________________________"""

# 13
palavras = []
contador = 0

for i in range(5):
    palavra = input("Digite uma palavra: ")
    palavras.append(palavra)
    
    if len(palavra) > 5:
        contador += 1

print("Palavras com mais de 5 letras:", contador)

# """ ________________________________________________________________________________"""

# 14
lista = []

for i in range(7):
    numero = int(input("Digite um número: "))
    lista.append(numero)

for i in range(len(lista)):
    print("Posiçao", i, ":", lista[i])

# """ ________________________________________________________________________________"""

# 15
lista = []
invertida = []

for i in range(5):
    numero = int(input("Digite um número: "))
    lista.append(numero)

for i in range(len(lista) - 1, -1, -1):
    invertida.append(lista[i])

print("Lista original:", lista)
print("Lista invertida:", invertida)