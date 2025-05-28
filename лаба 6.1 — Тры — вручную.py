import timeit
import matplotlib.pyplot as plt

# Рекурсивная реализация с мемоизацией
def F_recursive(n, memo={}):
    if n < 2:
        return -23
    if n not in memo:
        if n % 2 == 0:  # Если n четное
            memo[n] = (F_recursive(n - 1, memo) - (n - 2))
        else:  # Если n нечетное
            factorial_2n = calculate_factorial(2 * n)
            memo[n] = ((n - 2) / factorial_2n) - F_recursive(n - 1, memo)
    return memo[n]

# Улучшенная итеративная реализация
def F_iterative_optimized(n):
    if n < 2:
        return -23
    
    prev = -23  # F(1)
    factorial_prev = 1  # Начальное значение факториала для 0 или 1
    
    for i in range(2, n + 1):
        if i % 2 == 0:  # Если i четное
            current = (prev - (i - 2))
        else:  # Если i нечетное
            # Обновляем факториал накопительно
            for j in range(factorial_prev + 1, 2 * i + 1):
                factorial_prev *= j
            factorial_2i = factorial_prev
            current = ((i - 2) / factorial_2i) - prev
        
        prev = current
    
    return prev

# Функция для ручного вычисления факториала
def calculate_factorial(x):
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

# Сравнение времени выполнения
def compare_methods(max_n):
    recursive_times = []
    iterative_times = []
    results = []

    for n in range(1, max_n + 1):
        # Измерение времени рекурсивного метода
        recursive_timer = timeit.Timer(lambda: F_recursive(n))
        recursive_time = recursive_timer.timeit(number=1)
        recursive_times.append(recursive_time)

        # Измерение времени итеративного метода
        iterative_timer = timeit.Timer(lambda: F_iterative_optimized(n))
        iterative_time = iterative_timer.timeit(number=1)
        iterative_times.append(iterative_time)

        # Сохранение результатов вычислений
        recursive_result = F_recursive(n)
        iterative_result = F_iterative_optimized(n)
        results.append((n, recursive_result, iterative_result))

    return recursive_times, iterative_times, results

# Главная функция
def main():
    max_n = 15  # Максимальное значение n для сравнения
    recursive_times, iterative_times, results = compare_methods(max_n)

    # Вывод таблицы результатов
    print("Таблица результатов:")
    print("n | Рекурсивное значение | Итеративное значение | Время рекурсии (с) | Время итерации (с)")
    print("-" * 90)
    for i, (n, recursive_result, iterative_result) in enumerate(results):
        print(f"{n:2d} | {recursive_result:<20.10f} | {iterative_result:<20.10f} | {recursive_times[i]:.6f} | {iterative_times[i]:.6f}")

    # Построение графика
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, max_n + 1), recursive_times, label='Рекурсивный метод')
    plt.plot(range(1, max_n + 1), iterative_times, label='Итеративный метод')
    plt.xlabel('n')
    plt.ylabel('Время выполнения (с)')
    plt.title('Сравнение рекурсивного и итеративного методов')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
