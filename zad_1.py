def print_names(names):
    if len(names) == 5:
        for name in names:
            print(name)
    else:
        print('wrong number of names provided')


def double_numbers_w_for(numbers):
    if len(numbers) == 5:
        doubles = []
        for number in numbers:
            doubles.append(number * 2)
        return doubles
    else:
        print('wrong number of numbers provided')
        return -1


def double_numbers_w_list(numbers):
    if len(numbers) == 5:
        return [number * 2 for number in numbers]
    else:
        print('wrong number of numbers provided')
        return -1


def even_numbers(numbers):
    for i in range(10):
        if numbers[i] % 2 == 0:
            print(numbers[i])


def even_index(numbers):
    for i in range(0, 10, 2):
        print(numbers[i])


print_names(['a', 'b', 'c', 'd', 'e'])
print(double_numbers_w_for([1, 2, 4, 5, 3]))
print(double_numbers_w_list([1, 2, 4, 5, 3]))
print('even numbers only:')
even_numbers([1, 5, 3, 7, 5, 4, 7, 8, 9, 10])
print('even index only:')
even_index([1, 5, 3, 7, 5, 4, 7, 8, 9, 10])
