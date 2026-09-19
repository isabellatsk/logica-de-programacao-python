""" ________________________________________________________________________________"""

# EXERCICIOS DE WHILE

""" ________________________________________________________________________________"""

# 1
senha = "dog2"
inputSenha = input("Digite sua senha: ")

while inputSenha != senha:
    print("Senha incorreta! Tente novamente.")
    inputSenha = input("Digite sua senha: ")

print("Acesso permitido!")

# """ ________________________________________________________________________________"""

# 2

continuar = "s"

while continuar == "s":
    numero = int(input("Digite um número para verificar se ele é negativo, positivo ou zero: "))

    if numero > 0:
        print("Número positivo!")
    elif numero  == 0:
        print("Zero!")
    else:
        print("Número negativo!")
        
    continuar = input("Deseja testar outro número (s/n)? ").lower()
    
print("Fim!")

# """ ________________________________________________________________________________"""

#3
maior = None

numero = int(input("Digite um número (0 para parar): "))

while numero != 0:
    if maior is None or numero > maior:
        maior = numero
    numero = int(input("Digite um número (0 para parar): "))

if maior is not None:
    print("Maior número:", maior)
else:
    print("Nenhum número informado.")

# """ ________________________________________________________________________________"""

#4
contador = 0
pares = 0
impares = 0

while contador < 10:
    numero = int(input("Digite um número inteiro: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    contador += 1

print("Pares:", pares)
print("Ímpares:", impares)

# """ ________________________________________________________________________________"""

#5
soma = 0
contador = 0

nota = float(input("Digite uma nota (-1 para parar): "))

while nota != -1:
    soma += nota
    contador += 1
    nota = float(input("Digite uma nota (-1 para parar): "))

if contador > 0:
    media = soma / contador
    print("Média:", media)
else:
    print("Nenhuma nota informada.")

# """ ________________________________________________________________________________"""

#6
opcao = 0

while opcao != 3:
    print("1 - Dizer Olá")
    print("2 - Mostrar mensagem")
    print("3 - Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        print("Olá")
    elif opcao == 2:
        print("Você escolheu a opção 2")
    elif opcao == 3:
        print("Saindo...")
    else:
        print("Opção inválida")

# """ ________________________________________________________________________________"""

#7
continuar = "s"

while continuar == "s":
    numero = int(input("Digite um número: "))
    
    i = 1
    while i <= 10:
        print(numero, "x", i, "=", numero * i)
        i += 1
    
    continuar = input("Deseja ver outra tabuada (s/n)? ").lower()

# """ ________________________________________________________________________________"""

#8
soma = 0
contador = 0

while soma <= 100:
    numero = int(input("Digite um número: "))
    soma += numero
    contador += 1

print("Soma total:", soma)
print("Quantidade de números digitados:", contador)

# """ ________________________________________________________________________________"""

#9
usuario_correto = "admin"
senha_correta = "1234"

tentativas = 0

while tentativas < 3:
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    
    if usuario == usuario_correto and senha == senha_correta:
        print("Login realizado com sucesso")
        break
    else:
        print("Dados incorretos")
        tentativas += 1

if tentativas == 3:
    print("Conta bloqueada")

# """ ________________________________________________________________________________"""

#10
numero_secreto = 7
tentativas = 0

palpite = int(input("Tente adivinhar o número: "))

while palpite != numero_secreto:
    tentativas += 1
    
    if palpite > numero_secreto:
        print("Muito alto")
    else:
        print("Muito baixo")
    
    palpite = int(input("Tente novamente: "))

tentativas += 1
print("Acertou!")
print("Tentativas:", tentativas)