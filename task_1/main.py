def func_sequence(n):
    sequence = ""
    for i in range(1, n+1):
        sequence += str(i) * i
    return sequence

def main():
    n = int(input("Введите количество элементов (n): "))
    sequence = func_sequence(n)
    print(f"Первые {n} элементов последовательности: {sequence[0:n]}")

if __name__ == "__main__":
    main()