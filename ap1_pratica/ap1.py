codigos = []
nomes = []
precos = []
estoques = []
categorias = []
vendidos = []

historico_vendas = []
caixa = 0.0

carrinho_codigos = []
carrinho_qtd = []


def linha():
    print("-" * 60)

def titulo(texto):
    linha()
    print(texto.center(60))
    linha()

def buscar_indice_codigo(codigo):
    for i in range(len(codigos)):
        if codigos[i] == codigo:
            return i
    return -1

def mostrarProduto(i):
    print(f"""
Código:    {codigos[i]}
Nome:      {nomes[i]}
Preço:     R${precos[i]:.2f}
Estoque:   {estoques[i]}
Categoria: {categorias[i]}
Vendidos:  {vendidos[i]}
""")
    linha()

def cadastrarProduto():
    titulo("CADASTRAR PRODUTO")
    codigo = int(input("Código: "))

    if codigo <= 0:
        print("Código deve ser positivo.")
        return

    if buscar_indice_codigo(codigo) != -1:
        print("Código já cadastrado.")
        return

    nome = input("Nome: ")

    if nome == "":
        print("Nome não pode ser vazio.")
        return

    preco = float(input("Preço: R$"))

    if preco <= 0:
        print("Preço deve ser maior que zero.")
        return

    estoque = int(input("Estoque: "))

    if estoque < 0:
        print("Estoque não pode ser negativo.")
        return

    categoria = input("Categoria: ")

    if categoria == "":
        print("Categoria não pode ser vazia.")
        return

    codigos.append(codigo)
    nomes.append(nome)
    precos.append(preco)
    estoques.append(estoque)
    categorias.append(categoria)
    vendidos.append(0)
    print("Produto cadastrado com sucesso.")


def listarProdutos():
    titulo("LISTAR PRODUTOS")
    print("""
1 - Listar todos
2 - Listar por categoria
3 - Listar apenas com estoque > 0
4 - Listar por faixa de preço
5 - Ordenar por preço crescente
6 - Ordenar por preço decrescente
""")

    op = int(input("Escolha: "))
    linha()

    if len(codigos) == 0:
        print("Nenhum produto cadastrado.")
        return

    if op == 1:
        for i in range(len(codigos)):
            mostrarProduto(i)

    elif op == 2:
        categoria_busca = input("Categoria: ")
        encontrou = False

        for i in range(len(codigos)):
            if categorias[i].lower() == categoria_busca.lower():
                mostrarProduto(i)
                encontrou = True

        if not encontrou:
            print("Nenhum produto encontrado nessa categoria.")

    elif op == 3:
        encontrou = False

        for i in range(len(codigos)):
            if estoques[i] > 0:
                mostrarProduto(i)
                encontrou = True

        if not encontrou:
            print("Nenhum produto com estoque disponível.")

    elif op == 4:
        minimo = float(input("Preço mínimo: R$"))
        maximo = float(input("Preço máximo: R$"))

        encontrou = False

        for i in range(len(codigos)):
            if precos[i] >= minimo and precos[i] <= maximo:
                mostrarProduto(i)
                encontrou = True

        if not encontrou:
            print("Nenhum produto encontrado nessa faixa de preço.")

    elif op == 5 or op == 6:
        indices = []

        for i in range(len(codigos)):
            indices.append(i)

        for i in range(len(indices)):
            for j in range(i + 1, len(indices)):
                if op == 5:
                    if precos[indices[i]] > precos[indices[j]]:
                        temp = indices[i]
                        indices[i] = indices[j]
                        indices[j] = temp
                else:
                    if precos[indices[i]] < precos[indices[j]]:
                        temp = indices[i]
                        indices[i] = indices[j]
                        indices[j] = temp
        for i in indices:
            mostrarProduto(i)
    else:
        print("Opção inválida.")


def buscarProduto():
    titulo("BUSCAR PRODUTO")

    print("1 - Buscar por código")
    print("2 - Buscar por nome")

    op = int(input("Escolha: "))
    linha()

    if op == 1:
        codigo = int(input("Código: "))
        indice = buscar_indice_codigo(codigo)

        if indice == -1:
            print("Produto não encontrado.")
        else:
            mostrarProduto(indice)

    elif op == 2:
        nome_busca = input("Nome: ")
        encontrou = False

        for i in range(len(nomes)):
            if nome_busca.lower() in nomes[i].lower():
                mostrarProduto(i)
                encontrou = True

        if not encontrou:
            print("Produto não encontrado.")
    else:
        print("Opção inválida.")


def mostrarCarrinho():
    titulo("CARRINHO")

    if len(carrinho_codigos) == 0:
        print("Carrinho vazio.")
        return
    total = 0

    print(f"{'Produto':25} {'Qtd':5} {'Preço':10} {'Subtotal':10}")
    linha()

    for i in range(len(carrinho_codigos)):
        codigo = carrinho_codigos[i]
        qtd = carrinho_qtd[i]
        indice = buscar_indice_codigo(codigo)

        subtotal = precos[indice] * qtd
        total += subtotal
        print(f"{nomes[indice]:25} {qtd:<5} R${precos[indice]:<8.2f} R${subtotal:.2f}")

    linha()
    print(f"Total parcial: R${total:.2f}")


def adicionarProduto():
    titulo("ADICIONAR AO CARRINHO")

    if len(codigos) == 0:
        print("Nenhum produto cadastrado.")
        return

    codigo = int(input("Código do produto: "))
    indice = buscar_indice_codigo(codigo)

    if indice == -1:
        print("Produto não existe.")
        return

    qtd = int(input("Quantidade: "))

    if qtd <= 0:
        print("Quantidade inválida.")
        return

    indice_carrinho = -1

    for i in range(len(carrinho_codigos)):
        if carrinho_codigos[i] == codigo:
            indice_carrinho = i

    qtd_atual = 0

    if indice_carrinho != -1:
        qtd_atual = carrinho_qtd[indice_carrinho]

    if qtd + qtd_atual > estoques[indice]:
        print("Quantidade maior que o estoque disponível.")
        return

    if indice_carrinho == -1:
        carrinho_codigos.append(codigo)
        carrinho_qtd.append(qtd)
    else:
        carrinho_qtd[indice_carrinho] += qtd

    print("Produto adicionado ao carrinho.")
    mostrarCarrinho()


def removerProduto():
    titulo("REMOVER DO CARRINHO")

    if len(carrinho_codigos) == 0:
        print("Carrinho vazio.")
        return
    mostrarCarrinho()

    codigo = int(input("Código do produto para remover: "))

    for i in range(len(carrinho_codigos)):
        if carrinho_codigos[i] == codigo:
            carrinho_codigos.pop(i)
            carrinho_qtd.pop(i)
            print("Produto removido do carrinho.")
            return
    print("Produto não está no carrinho.")


def encerrarCompra():
    global caixa

    titulo("FINALIZAR COMPRA")

    if len(carrinho_codigos) == 0:
        print("Carrinho vazio.")
        return

    subtotal = 0
    quantidade_itens = 0
    resumo_itens = ""

    for i in range(len(carrinho_codigos)):
        codigo = carrinho_codigos[i]
        qtd = carrinho_qtd[i]
        indice = buscar_indice_codigo(codigo)

        subtotal += precos[indice] * qtd
        quantidade_itens += qtd
        resumo_itens += f"{nomes[indice]} x{qtd}; "

    taxa_fixa = 5.00
    desconto = 0

    mostrarCarrinho()

    cupom = input("Digite o cupom ou deixe vazio: ")

    if cupom == "DESC10":
        if subtotal >= 50:
            desconto = subtotal * 0.10
            print("Cupom DESC10 aplicado.")
        else:
            print("Cupom DESC10 só vale para subtotal maior ou igual a R$50.")
    elif cupom == "FRETEGRATIS":
        taxa_fixa = 0
        print("Cupom FRETEGRATIS aplicado.")
    elif cupom != "":
        print("Cupom inválido. Nenhum desconto aplicado.")

    imposto = subtotal * 0.04
    total_final = subtotal - desconto + taxa_fixa + imposto

    titulo("RESUMO DA COMPRA")

    print(f"Subtotal: R${subtotal:.2f}")
    print(f"Desconto: R${desconto:.2f}")
    print(f"Taxa fixa: R${taxa_fixa:.2f}")
    print(f"Imposto: R${imposto:.2f}")
    linha()
    print(f"TOTAL FINAL: R${total_final:.2f}")
    linha()

    print("1 - Dinheiro")
    print("2 - Cartão")

    pagamento = int(input("Forma de pagamento: "))

    if pagamento == 1:
        valor_pago = float(input("Valor pago: R$"))

        if valor_pago < total_final:
            print("Valor insuficiente.")
            return

        troco = valor_pago - total_final
        forma = "Dinheiro"
        print(f"Troco: R${troco:.2f}")

    elif pagamento == 2:
        forma = "Cartão"

    else:
        print("Forma de pagamento inválida.")
        return

    confirmar = input("Confirmar compra? (s/n): ")

    if confirmar.lower() != "s":
        print("Compra cancelada.")
        return

    for i in range(len(carrinho_codigos)):
        codigo = carrinho_codigos[i]
        qtd = carrinho_qtd[i]
        indice = buscar_indice_codigo(codigo)

        estoques[indice] -= qtd
        vendidos[indice] += qtd

    caixa += total_final
    venda = [total_final, quantidade_itens, forma, resumo_itens]
    historico_vendas.append(venda)

    carrinho_codigos.clear()
    carrinho_qtd.clear()
    print("Compra finalizada com sucesso.")


def reporEstoque():
    titulo("REPOR ESTOQUE")

    if len(codigos) == 0:
        print("Nenhum produto cadastrado.")
        return

    codigo = int(input("Código do produto: "))
    indice = buscar_indice_codigo(codigo)

    if indice == -1:
        print("Produto não encontrado.")
        return

    qtd = int(input("Quantidade para repor: "))

    if qtd <= 0:
        print("Quantidade inválida.")
        return

    estoques[indice] += qtd
    print("Estoque atualizado com sucesso.")
    print(f"Novo estoque de {nomes[indice]}: {estoques[indice]}")


def listarRelatorios():
    titulo("RELATÓRIOS")
    print(f"Faturamento total: R${caixa:.2f}")
    linha()

    if len(codigos) == 0:
        print("Nenhum produto cadastrado.")
        return

    mais_vendido = 0
    menor_estoque = 0

    for i in range(len(codigos)):
        if vendidos[i] > vendidos[mais_vendido]:
            mais_vendido = i

        if estoques[i] < estoques[menor_estoque]:
            menor_estoque = i

    print(f"Produto mais vendido: {nomes[mais_vendido]}")
    print(f"Quantidade vendida: {vendidos[mais_vendido]}")
    linha()

    print(f"Produto com menor estoque: {nomes[menor_estoque]}")
    print(f"Estoque atual: {estoques[menor_estoque]}")
    linha()

    categorias_unicas = []
    total_por_categoria = []

    for i in range(len(categorias)):
        achou = False

        for j in range(len(categorias_unicas)):
            if categorias_unicas[j] == categorias[i]:
                total_por_categoria[j] += vendidos[i]
                achou = True

        if not achou:
            categorias_unicas.append(categorias[i])
            total_por_categoria.append(vendidos[i])

    maior_categoria = 0

    for i in range(len(categorias_unicas)):
        if total_por_categoria[i] > total_por_categoria[maior_categoria]:
            maior_categoria = i

    print(f"Categoria mais vendida: {categorias_unicas[maior_categoria]}")
    print(f"Total vendido na categoria: {total_por_categoria[maior_categoria]}")
    linha()

    if len(historico_vendas) == 0:
        print("Ticket médio: R$0.00")
    else:
        soma = 0

        for venda in historico_vendas:
            soma += venda[0]

        ticket_medio = soma / len(historico_vendas)
        print(f"Ticket médio: R${ticket_medio:.2f}")

    linha()


def listarHistoricoVendas():
    titulo("HISTÓRICO DE VENDAS")

    if len(historico_vendas) == 0:
        print("Nenhuma venda registrada.")
        return

    n = int(input("Mostrar últimas quantas vendas? "))

    inicio = len(historico_vendas) - n

    if inicio < 0:
        inicio = 0

    for i in range(inicio, len(historico_vendas)):
        venda = historico_vendas[i]

        print(f"""
Venda #{i + 1}
Total: R${venda[0]:.2f}
Quantidade de itens: {venda[1]}
Forma de pagamento: {venda[2]}
Itens: {venda[3]}
""")
        linha()


def mostrarMenu():
    titulo("SISTEMA DE LOJA")
    print("1  - Cadastrar produto")
    print("2  - Listar produtos com filtros")
    print("3  - Buscar produto")
    print("4  - Carrinho: adicionar item")
    print("5  - Carrinho: remover item")
    print("6  - Finalizar compra")
    print("7  - Repor estoque")
    print("8  - Relatórios")
    print("9  - Histórico de vendas")
    print("10 - Sair")
    linha()

opcao = 0

while opcao != 10:
    mostrarMenu()
    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            cadastrarProduto()
        case 2:
            listarProdutos()
        case 3:
            buscarProduto()
        case 4:
            adicionarProduto()
        case 5:
            removerProduto()
        case 6:
            encerrarCompra()
        case 7:
            reporEstoque()
        case 8:
            listarRelatorios()
        case 9:
            listarHistoricoVendas()
        case 10:
            print("Saindo...")
        case _:
            print("Opção inválida.")