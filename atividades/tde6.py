""" ________________________________________________________________________________"""

# EXERCICIOS DE FUNÇÕES 2

""" ________________________________________________________________________________"""

# 1
def ler_numeros():
    lista = []
    for i in range(8):
        n = int(input("Digite um número: "))
        lista.append(n)
    return lista


def analisar_numeros(lista):
    soma = sum(lista)
    pares = 0

    for n in lista:
        if n % 2 == 0:
            pares += 1

    print("Números:", lista)
    print("Soma:", soma)
    print("Pares:", pares)
    print("Maior:", max(lista))


# 2
def ler_notas():
    notas = []
    for i in range(4):
        nota = float(input("Digite a nota: "))
        notas.append(nota)
    return notas


def calcular_media(notas):
    return sum(notas) / len(notas)


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


# 3
def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    cont = 0

    for letra in frase:
        if letra in vogais:
            cont += 1

    return cont


def inverter_frase(frase):
    return frase[::-1]


def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)


# 4
def cadastrar_produtos():
    produtos = []

    for i in range(3):
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))

        produto = {
            "nome": nome,
            "preco": preco
        }

        produtos.append(produto)

    return produtos


def mostrar_produtos(produtos):
    for p in produtos:
        print(p["nome"], "-", p["preco"])


def total_produtos(produtos):
    total = 0
    for p in produtos:
        total += p["preco"]
    return total


def produto_mais_caro(produtos):
    return max(produtos, key=lambda p: p["preco"])


# 5
def cadastrar_aluno(lista):
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    aluno = {
        "nome": nome,
        "idade": idade
    }

    lista.append(aluno)


def listar_alunos(lista):
    for a in lista:
        print(a["nome"], "-", a["idade"])


def buscar_aluno(lista):
    nome = input("Digite o nome: ")

    for a in lista:
        if a["nome"] == nome:
            print("Encontrado:", a["nome"], "-", a["idade"])
            return

    print("Aluno não encontrado")


# EXECUÇÃO

# 1
lista = ler_numeros()
analisar_numeros(lista)

# 2
nome = input("Nome do aluno: ")
notas = ler_notas()
media = calcular_media(notas)
situacao = verificar_situacao(media)

print("Nome:", nome)
print("Média:", media)
print("Situação:", situacao)

# 3
frase = input("Digite uma frase: ")

print("Frase:", frase)
print("Vogais:", contar_vogais(frase))
print("Palavras:", contar_palavras(frase))
print("Invertida:", inverter_frase(frase))

# 4
produtos = cadastrar_produtos()

mostrar_produtos(produtos)

mais_caro = produto_mais_caro(produtos)

print("Mais caro:", mais_caro["nome"], "-", mais_caro["preco"])
print("Total:", total_produtos(produtos))

# 5
alunos = []

while True:
    print("\n1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    print("4 - Sair")

    op = input("Escolha: ")

    if op == "1":
        cadastrar_aluno(alunos)
    elif op == "2":
        listar_alunos(alunos)
    elif op == "3":
        buscar_aluno(alunos)
    elif op == "4":
        break
    else:
        print("Opção inválida")