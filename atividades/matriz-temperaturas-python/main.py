
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
times = ["Morning", "Afternoon", "Evening", "Night"]


def read_temperatures():
    matrix = []

    print("=== Register Temperatures ===\n")

    for day in days:
        row = []

        for time in times:
            temperature = float(input(f"Enter temperature for {day} - {time}: "))
            row.append(temperature)

        matrix.append(row)

    return matrix


def show_table(matrix):
    print("\n=== TEMPERATURE TABLE ===")

    print(f"{'Day':<8}", end="")

    for time in times:
        print(f"{time:<12}", end="")

    print()

    for i in range(len(matrix)):
        print(f"{days[i]:<8}", end="")

        for temp in matrix[i]:
            print(f"{temp:<12}", end="")

        print()


def averages(matrix):
    print("\n=== AVERAGES BY DAY ===")

    for i in range(len(matrix)):
        avg_day = sum(matrix[i]) / len(matrix[i])
        print(f"{days[i]}: {avg_day:.2f}°C")

    print("\n=== AVERAGES BY TIME ===")

    for col in range(len(times)):
        total = 0

        for row in range(len(matrix)):
            total += matrix[row][col]

        avg_time = total / len(matrix)
        print(f"{times[col]}: {avg_time:.2f}°C")


def highest_lowest(matrix):
    highest = matrix[0][0]
    lowest = matrix[0][0]

    highest_day = 0
    highest_time = 0

    lowest_day = 0
    lowest_time = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            value = matrix[i][j]

            if value > highest:
                highest = value
                highest_day = i
                highest_time = j

            if value < lowest:
                lowest = value
                lowest_day = i
                lowest_time = j

    print("\n=== HIGHEST AND LOWEST TEMPERATURE ===")

    print(f"Highest: {highest}°C ({days[highest_day]} - {times[highest_time]})")
    print(f"Lowest: {lowest}°C ({days[lowest_day]} - {times[lowest_time]})")


def query(matrix):
    print("\n=== TEMPERATURE QUERY ===")

    while True:
        day = int(input("Enter day (1-Mon to 5-Fri): "))
        if 1 <= day <= 5:
            break
        print("Invalid day. Try again.")

    while True:
        time = int(input("Enter time (1-Morning | 2-Afternoon | 3-Evening | 4-Night): "))
        if 1 <= time <= 4:
            break
        print("Invalid time. Try again.")

    day -= 1
    time -= 1

    print(
        f"\nTemperature on {days[day]} - {times[time]}: {matrix[day][time]}°C"
    )


def main():
    matrix = read_temperatures()
    show_table(matrix)
    averages(matrix)
    highest_lowest(matrix)
    query(matrix)


main()

