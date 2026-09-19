""" ________________________________________________________________________________"""

# EXERCICIOS DE CONDICIONAIS

""" ________________________________________________________________________________"""

# 1 
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (float(nota1) + float(nota2)) / 2

if media >= 7 and media < 10:
    print("\nAprovado!")
elif media == 10: 
    print("\nAprovado com Distinção!")
else:
    print("\nReprovado!")

""" ________________________________________________________________________________"""

# 2
num1 = 1
num2 = 56
num3 = 80

if num1 > num2 and num1 > num3:
    print(f"O número {num1} é o maior!")
elif num2 > num1 and num2 > num3:
    print(f"O número {num2} é o maior!")
else:
    print(f"O número {num3} é o maior!")

""" ________________________________________________________________________________"""

# 3
num1 = 100
num2 = 200
num3 = 30

if num1 > num2 and num1 > num3:
    print(f"O número {num1} é o maior!")
    if num2 < num3:
        print(f"O número {num2} é o menor!")
    else:
        print(f"O número {num3} é o menor!")
elif num2 > num1 and num2 > num3:
    print(f"O número {num2} é o maior!")
    if num1 < num3:
        print(f"O número {num1} é o menor!")
    else:
        print(f"O número {num3} é o menor!")
else:
    print(f"O número {num3} é o maior!")
    if num2 < num1:
        print(f"O número {num2} é o menor!")
    else:
        print(f"O número {num1} é o menor!")

""" ________________________________________________________________________________"""

# 4
numA = int(input("Digite o primeiro número: "))
numB = int(input("Digite o segundo número: "))

print(f"\nValor inicial: numA = {numA}, numB = {numB}.")

numA = numB
numB = numA

print(f"Valor inverso: numA = {numA}, numB = {numB}.")

""" ________________________________________________________________________________"""

# 5
salarioColaborador = float(input("Digite o salário do colaborador (R$): "))

if salarioColaborador <= 280:
    percentual = 20
    reajuste = (percentual / 100) * salarioColaborador
    novoSalario = salarioColaborador + reajuste
elif salarioColaborador > 280 and salarioColaborador < 700:
    percentual = 15
    reajuste = (percentual / 100) * salarioColaborador
    novoSalario = salarioColaborador + reajuste
elif salarioColaborador >= 700 and salarioColaborador < 1500:
    percentual = 10
    reajuste = (percentual / 100) * salarioColaborador
    novoSalario = salarioColaborador + reajuste
else:
    percentual = 5
    reajuste = (percentual / 100) * salarioColaborador
    novoSalario = salarioColaborador + reajuste
    
print(f"\nSalário antes do reajuste: {salarioColaborador}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: {reajuste:.1f}")
print(f"Novo salário com reajuste aplicado: {novoSalario}\n")
print(f"{reajuste:.1f} + {salarioColaborador} = {novoSalario}")

""" ________________________________________________________________________________"""

# 6
dia = int(input("Digite um número correspondente aos dias da semana: "))

def dia_semana(dia):
    match dia:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda"
        case 3:
            return "Terça"
        case 4:
            return "Quarta"
        case 5:
            return "Quinta"
        case 6:
            return "Sexta"
        case 7:
            return "Sábado"
        case _:
            return "\nValor inválido"
print(dia_semana(dia)) 

""" ________________________________________________________________________________"""

# 7
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par!")
else: 
    print(f"O número {numero} é impar!")

""" ________________________________________________________________________________"""

# 8
numero = int(input("Digite um número inteiro menor que 1000: "))

if 0 <= numero < 1000:

    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    partes = []

    if centenas:
        partes.append(f"{centenas} centena" if centenas == 1 else f"{centenas} centenas")

    if dezenas:
        partes.append(f"{dezenas} dezena" if dezenas == 1 else f"{dezenas} dezenas")

    if unidades:
        partes.append(f"{unidades} unidade" if unidades == 1 else f"{unidades} unidades")

    if len(partes) == 1:
        resultado = partes[0]
    else:
        resultado = ", ".join(partes[:-1]) + " e " + partes[-1]

    print(f"{numero} = {resultado}")

else:
    print("Número inválido.")

""" ________________________________________________________________________________"""

# 9
saque = int(input("Digite o valor do saque (de 10R$ à 600R$): "))

if saque < 10:
    print("Inválido! O valor mínimo para sacar é: 10R$")
elif saque > 600:
    print("Inválido! O valor máximo para sacar é: 600R$")
else:
    valor = saque
    notas = [100, 50, 10, 5, 1]

    print(f"Para sacar a quantia de {saque} reais, o programa fornece: ")
    for nota in notas:
        quantidade = valor // nota
        if quantidade > 0:
            print(f"{quantidade} nota(s) de R$ {nota}")
            valor = valor % nota

""" ________________________________________________________________________________"""

# 10
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f"\n({num1} ? {num2})")
print(f"\nDigite o número da operação: ")
print("Soma - 1 | Subtração - 2 | Divisão - 3 | Multiplicação - 4")
operacaoEscolhida = input()

def operacao(op, n1, n2):
    match op:
        case "1":
            return n1 + n2
        case "2":
            return n1 - n2
        case "3":
            if n2 == 0:
                return "Não é possível dividir por zero"
            return n1 / n2
        case "4":
            return n1 * n2
        case _:
            return "Operação inválida!"
resultado = operacao(operacaoEscolhida, num1, num2)

if isinstance(resultado, str):
    print(resultado)
else:
    print(f"\nResultado: {resultado}")

    if resultado.is_integer():
        if int(resultado) % 2 == 0:
            print("Resultado: par")
        else:
            print("Resultado: ímpar")
    else:
        print("Não é possível classificar como par ou ímpar (é decimal)")

    if resultado > 0:
        print("Resultado: positivo")
    elif resultado < 0:
        print("Resultado: negativo")
    else:
        print("Resultado: zero")

    if resultado.is_integer():
        print("Resultado: inteiro")
    else:
        print("Resultado: decimal")