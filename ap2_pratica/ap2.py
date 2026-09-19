# Sistema de Reservas de Sala - Agenda Semanal
# Matriz 5x8:
# Dias: Seg, Ter, Qua, Qui, Sex
# Horários: 08, 09, 10, 11, 12, 13, 14, 15

dias = ["Seg", "Ter", "Qua", "Qui", "Sex"]
horarios = ["08", "09", "10", "11", "12", "13", "14", "15"]


def criar_agenda():
    agenda = []

    for i in range(5):
        linha = []
        for j in range(8):
            linha.append("LIVRE")
        agenda.append(linha)

    return agenda


def mostrar_menu():
    print("\n============== SISTEMA DE RESERVAS DE SALA ==============\n")
    print("1 - Mostrar agenda completa")
    print("2 - Consultar disponibilidade")
    print("3 - Fazer reserva")
    print("4 - Cancelar reserva")
    print("5 - Relatórios")
    print("6 - Mostrar histórico")
    print("0 - Sair")
    print("===========================================================\n")


def mostrar_agenda(agenda):
    print("\n===== AGENDA SEMANAL =====")

    print("Dia/Hora", end="\t")
    for horario in horarios:
        print(horario, end="\t")
    print()

    for i in range(5):
        print(dias[i], end="\t\t")
        for j in range(8):
            if agenda[i][j] == "LIVRE":
                print("LIVRE", end="\t")
            else:
                print("OCUP.", end="\t")
        print()


def ler_dia_horario():
    print("\nDias disponíveis:")
    print("1 -> Segunda")
    print("2 -> Terça")
    print("3 -> Quarta")
    print("4 -> Quinta")
    print("5 -> Sexta")

    dia = int(input("Escolha o dia: "))

    print("\nHorários disponíveis:")
    for i in range(8):
        print(str(i + 1) + " -> " + horarios[i] + " horas")

    horario = int(input("Escolha o horário: "))

    if dia < 1 or dia > 5 or horario < 1 or horario > 8:
        print("Dia ou horário inválido.")
        return -1, -1
    return dia - 1, horario - 1


def consultar(agenda):
    print("\n===== CONSULTAR DISPONIBILIDADE =====")
    dia, horario = ler_dia_horario()

    if dia == -1:
        return
    reserva = agenda[dia][horario]

    if reserva == "LIVRE":
        print("Esse horário está LIVRE.")
    else:
        print("Esse horário está RESERVADO.")
        print("Reserva:", reserva)


def reservar(agenda, historico):
    print("\n===== FAZER RESERVA =====")

    dia, horario = ler_dia_horario()
    if dia == -1:
        return

    if agenda[dia][horario] != "LIVRE":
        print("Esse horário já está reservado.")
        print("Reserva atual:", agenda[dia][horario])
        return
    nome = input("Nome do responsável: ").strip()

    if nome == "":
        print("O nome não pode ser vazio.")
        return
    motivo = input("Motivo da reserva: ").strip()

    if motivo == "":
        motivo = "Sem motivo informado"
    agenda[dia][horario] = nome + " - " + motivo

    historico.append(
        "Reserva criada: " + dias[dia] + ", " + horarios[horario] + "h, " + nome + " - " + motivo
    )
    print("Reserva criada com sucesso.")


def cancelar(agenda, historico):
    print("\n===== CANCELAR RESERVA =====")
    dia, horario = ler_dia_horario()
    if dia == -1:
        return

    if agenda[dia][horario] == "LIVRE":
        print("Esse horário já está livre. Não há reserva para cancelar.")
        return
    print("Reserva encontrada:", agenda[dia][horario])
    confirmacao = input("Deseja cancelar a reserva? (S/N): ").upper()

    if confirmacao == "S":
        reserva_cancelada = agenda[dia][horario]
        agenda[dia][horario] = "LIVRE"
        historico.append(
            "Reserva cancelada: " + dias[dia] + ", " + horarios[horario] + "h, " + reserva_cancelada
        )
        print("Reserva cancelada com sucesso.")
    else:
        print("Cancelamento não realizado.")


def relatorios(agenda):
    while True:
        print("\n===== RELATÓRIOS =====")
        print("1 - Total de horários livres e reservados")
        print("2 - Dia com mais reservas")
        print("3 - Horário mais reservado")
        print("4 - Buscar reservas por nome")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            total_livres = 0
            total_reservados = 0

            for i in range(5):
                for j in range(8):
                    if agenda[i][j] == "LIVRE":
                        total_livres += 1
                    else:
                        total_reservados += 1
            print("Total de horários livres:", total_livres)
            print("Total de horários reservados:", total_reservados)

        elif opcao == "2":
            maior_quantidade = -1
            dia_mais_reservado = ""

            for i in range(5):
                quantidade = 0

                for j in range(8):
                    if agenda[i][j] != "LIVRE":
                        quantidade += 1
                if quantidade > maior_quantidade:
                    maior_quantidade = quantidade
                    dia_mais_reservado = dias[i]
            print("Dia com mais reservas:", dia_mais_reservado)
            print("Quantidade de reservas:", maior_quantidade)

        elif opcao == "3":
            maior_quantidade = -1
            horario_mais_reservado = ""

            for j in range(8):
                quantidade = 0

                for i in range(5):
                    if agenda[i][j] != "LIVRE":
                        quantidade += 1
                if quantidade > maior_quantidade:
                    maior_quantidade = quantidade
                    horario_mais_reservado = horarios[j]

            print("Horário mais reservado:", horario_mais_reservado + "h")
            print("Quantidade de reservas:", maior_quantidade)
        elif opcao == "4":
            buscar_por_nome(agenda)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


def buscar_por_nome(agenda):
    nome_busca = input("Digite o nome para buscar: ").strip().lower()

    if nome_busca == "":
        print("O nome não pode ser vazio.")
        return
    encontrou = False

    for i in range(5):
        for j in range(8):
            reserva = agenda[i][j]

            if reserva != "LIVRE" and nome_busca in reserva.lower():
                print(dias[i], horarios[j] + "h:", reserva)
                encontrou = True
    if encontrou == False:
        print("Nenhuma reserva encontrada para esse nome.")


def mostrar_historico(historico):
    print("\n===== HISTÓRICO DE OPERAÇÕES =====")

    if len(historico) == 0:
        print("Nenhuma operação registrada.")
        return
    n = int(input("Quantas últimas operações deseja ver? "))

    if n <= 0:
        print("Quantidade inválida.")
        return
    inicio = len(historico) - n

    if inicio < 0:
        inicio = 0

    for i in range(inicio, len(historico)):
        print(historico[i])


def main():
    agenda = criar_agenda()
    historico = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            mostrar_agenda(agenda)
        elif opcao == "2":
            consultar(agenda)
        elif opcao == "3":
            reservar(agenda, historico)
        elif opcao == "4":
            cancelar(agenda, historico)
        elif opcao == "5":
            relatorios(agenda)
        elif opcao == "6":
            mostrar_historico(historico)
        elif opcao == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")
main()