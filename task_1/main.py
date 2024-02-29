def func_sequence(n):
    for i in range(1, n+1):
        for _ in range(i):
            yield i

def main():
    n = int(input("Введите количество элементов: "))
    sequence = func_sequence(n)
    print(f"Первые {n} элементов последовательности: {''.join(str(next(sequence)) for _ in range(n))}")

if __name__ == "__main__":
    main()