first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
combined_strings = first_strings + second_strings

first_result = [len(x) for x in first_strings if len(x) >= 5]
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = {x: len(x) for x in combined_strings if len(x) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
print()

"""
Дан список целых чисел, примените функции map и filter
так, чтобы в конечном списке оставить нечётные квадраты чисел
"""


def odd(x):
    return x % 2 != 0


def square(y):
    return y ** 2


numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
result = map(square, filter(odd, numbers))
print(list(result))
