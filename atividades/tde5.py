""" ________________________________________________________________________________"""

# EXERCICIOS DE FUNÇÕES 1

""" ________________________________________________________________________________"""

# 1 
def analisar_idades():
    menores = adultos = idosos = 0

    for i in range(5):
        idade = int(input("Digite a idade: "))

        if idade < 0:
            print("Idade inválida")
            continue

        if idade < 18:
            menores += 1
        elif idade < 60:
            adultos += 1
        else:
            idosos += 1

    print("Menores:", menores)
    print("Adultos:", adultos)
    print("Idosos:", idosos)


# 2
def analisar_temperaturas():
    lista = []
    soma = 0
    abaixo15 = entre = acima30 = 0

    for i in range(5):
        temp = float(input("Digite a temperatura: "))
        lista.append(temp)
        soma += temp

        if temp < 15:
            abaixo15 += 1
        elif temp <= 30:
            entre += 1
        else:
            acima30 += 1

    print("Maior:", max(lista))
    print("Menor:", min(lista))
    print("Média:", soma / len(lista))
    print("Abaixo de 15:", abaixo15)
    print("Entre 15 e 30:", entre)
    print("Acima de 30:", acima30)


# 3
def analisar_vendas():
    soma = 0
    baixa = media = alta = 0

    for i in range(5):
        valor = float(input("Digite valor da venda: "))

        if valor < 0:
            print("Valor inválido")
            continue

        soma += valor

        if valor <= 100:
            baixa += 1
        elif valor <= 500:
            media += 1
        else:
            alta += 1

    print("Total:", soma)
    print("Média:", soma / 5)
    print("Baixas:", baixa)
    print("Médias:", media)
    print("Altas:", alta)


# 4 
def classificar_numeros():
    pares = impares = positivos = negativos = zeros = 0

    for i in range(5):
        n = int(input("Digite um número: "))

        if n == 0:
            zeros += 1
        else:
            if n % 2 == 0:
                pares += 1
            else:
                impares += 1

            if n > 0:
                positivos += 1
            else:
                negativos += 1

    print("Pares:", pares)
    print("Ímpares:", impares)
    print("Positivos:", positivos)
    print("Negativos:", negativos)
    print("Zeros:", zeros)


# 5 
def analisar_estoque():
    sem = baixo = normal = 0

    for i in range(5):
        qtd = int(input("Digite quantidade: "))

        if qtd == 0:
            sem += 1
        elif qtd <= 5:
            baixo += 1
        else:
            normal += 1

    print("Sem estoque:", sem)
    print("Baixo:", baixo)
    print("Normal:", normal)


# 6
def analisar_alturas():
    lista = []
    soma = 0
    baixa = media = alta = 0

    for i in range(5):
        h = float(input("Digite altura: "))

        if h <= 0:
            print("Altura inválida")
            continue

        lista.append(h)
        soma += h

        if h < 1.60:
            baixa += 1
        elif h <= 1.80:
            media += 1
        else:
            alta += 1

    print("Maior:", max(lista))
    print("Menor:", min(lista))
    print("Média:", soma / len(lista))
    print("Menor 1.60:", baixa)
    print("Entre 1.60 e 1.80:", media)
    print("Maior 1.80:", alta)


# 7 
def verificar_senhas():
    fraca = media = forte = 0

    for i in range(5):
        senha = int(input("Digite senha: "))

        if senha < 1000:
            print("Fraca")
            fraca += 1
        elif senha <= 9999:
            print("Média")
            media += 1
        else:
            print("Forte")
            forte += 1

    print("Fracas:", fraca)
    print("Médias:", media)
    print("Fortes:", forte)


# 8 
def analisar_precos():
    lista = []
    soma = 0
    barato = medio = caro = 0

    for i in range(5):
        preco = float(input("Digite preço: "))
        lista.append(preco)
        soma += preco

        if preco <= 50:
            barato += 1
        elif preco <= 200:
            medio += 1
        else:
            caro += 1

    print("Mais caro:", max(lista))
    print("Mais barato:", min(lista))
    print("Média:", soma / len(lista))
    print("Até 50:", barato)
    print("50 a 200:", medio)
    print("Acima de 200:", caro)


# 9
def avaliar_conceitos():
    A = B = C = D = 0

    for i in range(5):
        nota = float(input("Digite nota: "))

        if nota >= 9:
            A += 1
        elif nota >= 7:
            B += 1
        elif nota >= 5:
            C += 1
        else:
            D += 1

    print("A:", A)
    print("B:", B)
    print("C:", C)
    print("D:", D)


# 10
def analisar_partidas():
    lista = []
    soma = 0
    zero = baixo = alto = 0

    for i in range(5):
        gols = int(input("Gols: "))
        lista.append(gols)
        soma += gols

        if gols == 0:
            zero += 1
        elif gols <= 2:
            baixo += 1
        else:
            alto += 1

    print("Média:", soma / len(lista))
    print("Maior:", max(lista))
    print("Sem gols:", zero)
    print("1 a 2 gols:", baixo)
    print("3+ gols:", alto)