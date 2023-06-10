# 1. При старте приложения запускаются три процесса. Первый процесс заполняет список случайными числами.
# Два других процесса ожидают заполнения. Когда список заполнен оба процесса запускаются. Первый процесс находит
# сумму элементов списка, второй процесс среднеарифметическое значение в списке.
# Полученный список, сумма и среднеарифметическое выводятся на экран.

# import multiprocessing
# import random
#
#
# def summ(numbers):
#     print(sum(numbers))
#
#
# def avg(numbers):
#     print(sum(numbers) / len(numbers))
#
#
# if __name__ == '__main__':
#     numbers = [random.randint(0, 100) for i in range(10)]
#     print(numbers)
#     pr1 = multiprocessing.Process(target=summ, args=(numbers,))
#     pr2 = multiprocessing.Process(target=avg, args=(numbers,))
#     pr1.start()
#     pr1.join()
#     pr2.start()


# 2. Пользователь с клавиатуры вводит путь к файлу. После чего запускаются три процесса.
# Первый процесс заполняет файл случайными числами. Два других процесса ожидают заполнения.
# Когда файл заполнен оба процесса стартуют. Первый процесс находит все простые числа,
# второй процесс факториал каждого числа в файле. Результаты поиска каждый процесс должен записать в новый файл.
# На экран необходимо отобразить статистику выполненных операций.

# import multiprocessing
# import random
#
#
# def prime(numbers):
#     with open('new.txt', 'w', encoding='utf-8') as f:
#         for n in numbers:
#             if len([i for i in range(1, n + 1) if n % i == 0]) == 2:
#                 f.write(str(n) + '\n')
#             if n == 1:
#                 f.write(str(n) + '\n')
#
#
# def factorial(numbers):
#     with open('new1.txt', 'w', encoding='utf-8') as f:
#         for k in numbers:
#             factorial = 1
#             for i in range(1, k + 1):
#                 factorial *= i
#             f.write(str(factorial) + '\n')
#
#
# if __name__ == '__main__':
#     filename = input('Введите путь к файлу: ')
#     with open(filename, 'w', encoding='utf-8') as f:
#         numbers = [random.randint(1, 10) for i in range(10)]
#         f.write(str(numbers))
#
#     pr1 = multiprocessing.Process(target=prime, args=(numbers,))
#     pr2 = multiprocessing.Process(target=factorial, args=(numbers,))
#     pr1.start()
#     pr2.start()
