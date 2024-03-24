import os
import timeit
from typing import Callable

def rabin_karp(text, pattern):
    d = 256  # Кількість символів у вхідному алфавіті
    q = 101  # Просте число
    M = len(pattern)
    N = len(text)
    i = j = 0
    p = 0  # хеш для шаблону
    t = 0  # хеш для тексту
    h = 1
    result = []

    # Значення h буде "pow(d, M-1)%q"
    for i in range(M-1):
        h = (h * d) % q

    # Розрахунок хешу для шаблону та перших M символів тексту
    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Слайд по тексту
    for i in range(N - M + 1):
        # Порівняння хешу шаблону та поточного відрізку тексту
        if p == t:
            # Перевірка символів один за одним
            for j in range(M):
                if text[i+j] != pattern[j]:
                    break

            j += 1
            # Якщо всі символи шаблону співпали з поточним відрізком тексту
            if j == M:
                result.append(i)

        # Розрахунок хешу для наступного відрізка тексту
        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            if t < 0:
                t = t + q
    return result

def knuth_morris_pratt(text, pattern):
    M = len(pattern)
    N = len(text)
    # Створюємо lps[] масив, який буде зберігати найбільшу префікс-суфікс довжину
    lps = [0]*M
    j = 0  # індекс для pattern[]

    # Попередній розрахунок lps[] масиву
    compute_lps_array(pattern, M, lps)

    i = 0  # індекс для text[]
    result = []  # Масив для зберігання індексів входження
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == M:
            result.append(i-j)
            j = lps[j-1]

        # Неспівпадіння після j співпадінь
        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return result

def compute_lps_array(pattern, M, lps):
    length = 0  # Довжина попереднього найбільшого префікс-суфіксу
    lps[0] = 0  # lps[0] завжди 0
    i = 1

    while i < M:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

# Boyer-Moore search
def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return i

        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return -1


# Прочитаємо текстові файли з локального сховища
def read_file(filename):
    project_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(project_dir, filename)
    with open(full_path, "r", encoding="utf-8", errors="ignore") as file:
        return file.read()

def time_search_algorithm(algorithm, text, pattern):
    start_time = timeit.default_timer()
    algorithm(text, pattern)
    return timeit.default_timer() - start_time

# Задайте текст та підрядки для пошуку
text1 = read_file('article_1.txt')
text2 = text1 = read_file('article_2.txt')

pattern1 = "Жадібний алгоритм у цьому випадку полягає в тому, щоб на кожному кроці побудови рішення використовувати монети максимального номіналу,"
pattern2 = "неіснуючий"  # Не існує в тексті

# Список алгоритмів
algorithms = [rabin_karp, knuth_morris_pratt, boyer_moore]

# Тестування кожного алгоритму
for algorithm in algorithms:
    name = algorithm.__name__
    print(f"{name} пошук '{pattern1}' у text1: {time_search_algorithm(algorithm, text1, pattern1)} секунд")
    print(f"{name} пошук '{pattern2}' у text1: {time_search_algorithm(algorithm, text1, pattern2)} секунд")
    print(f"{name} пошук '{pattern1}' у text2: {time_search_algorithm(algorithm, text2, pattern1)} секунд")
    print(f"{name} пошук '{pattern2}' у text2: {time_search_algorithm(algorithm, text2, pattern2)} секунд")
    
