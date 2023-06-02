#Задачи по теме Алгоритмическая сложность и анализ алгоритмов

#Задача 2

import random
import time

def linear_search(arr):
    min_num = float('inf')
    max_num = float('-inf')
    for num in arr:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return min_num, max_num

def binary_search(arr):
    min_num = float('inf')
    max_num = float('-inf')
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < min_num:
            min_num = arr[mid]
        if arr[mid] > max_num:
            max_num = arr[mid]
        if arr[mid] == min_num == max_num:
            break
        if arr[mid] < min_num:
            right = mid - 1
        else:
            left = mid + 1
    return min_num, max_num

# Генерация случайного массива
arr = [random.randint(0, 1000) for _ in range(1000)]

# Линейный поиск
start_time = time.time()
min_num_linear, max_num_linear = linear_search(arr)
linear_search_time = time.time() - start_time

# Бинарный поиск
start_time = time.time()
min_num_binary, max_num_binary = binary_search(sorted(arr))
binary_search_time = time.time() - start_time

# Вывод результатов
print(f"Минимальное число (линейный поиск): {min_num_linear}")
print(f"Максимальное число (линейный поиск): {max_num_linear}")
print(f"Время выполнения линейного поиска: {linear_search_time:.6f} сек\n")

print(f"Минимальное число (бинарный поиск): {min_num_binary}")
print(f"Максимальное число (бинарный поиск): {max_num_binary}")
print(f"Время выполнения бинарного поиска: {binary_search_time:.6f} сек")

#Задача 3

#Алгоритм перебора:

def brute_force_lcm(a, b):
    max_num = max(a, b)
    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        max_num += 1

#Алгоритм Евклида:
def euclidean_lcm(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    return abs(a * b) // gcd(a, b)

#Оба алгоритма дают правильный результат, однако алгоритм Евклида является более эффективным, так как его сложность зависит от логарифма от минимального из двух чисел, в то время как алгоритм перебора имеет линейную сложность. Поэтому алгоритм Евклида является лучшим решением для задачи нахождения НОК двух целых чисел.


#Задание 4
#Линейный поиск:

def linear_search_median(nums):
    n = len(nums)
    if n % 2 == 0:
        median = (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        median = nums[n // 2]
    return median

#Бинарный поиск:

def binary_search_median(nums):
    n = len(nums)
    if n % 2 == 0:
        median = (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        median = nums[n // 2]
    return median

#Оба алгоритма дают одинаковый результат и имеют одинаковую временную сложность O(1). Разница во времени выполнения между ними будет незначительной и будет зависеть от конкретной реализации и оптимизации. В данном случае можно сказать, что оба алгоритма равнозначны по эффективности и выбор между ними будет зависеть от контекста использования и предпочтений разработчика.


