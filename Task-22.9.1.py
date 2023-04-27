def insertion_sort(array_list):
    for i in range(1, len(array_list)):
        num = array_list[i]
        id_num = i
        while id_num > 0 and array_list[id_num - 1] > num:
            array_list[id_num] = array_list[id_num - 1]
            id_num -= 1
        array_list[id_num] = num

while True:
    """ Ввод произвольного массива целых чисел через пробел (больше одного числа), с проверкой ввода."""
    try:
        array = input('Введите последовательность любых чисел через пробел: ')

        if len(array) <= 1:
            print('Ошибка! Необходимо ввести несколько чисел через пробел:')
            continue

    except ValueError:
        print('Ошибка! Необходимо ввести только целые числа:')
    else:
        break

array_list = list(map(int, array.split()))
print('Последовательность ваших чисел: ', str(array_list))
insertion_sort(array_list)
print('Отсортированная последовательность ваших чисел: ', array_list)

def binary_search(array_list, random_number, left, right):
    if left > right:
        print('Указанное число не входит в диапазон списка!')
        return False
    middle = (right + left) // 2
    if array_list[middle] == random_number:
        return middle
    elif random_number < array_list[middle]:
        return binary_search(array_list, random_number, left, middle - 1)
    else:
        return binary_search(array_list, random_number, middle + 1, right)

while True:
    """ Ввод произвольного числа, с проверкой ввода."""
    try:
        random_number = int(input('Введите любое число из диапазона списка: '))
        if random_number < min(array_list) or random_number > max(array_list):
            break
        if random_number <= 0:
            raise Exception
        break
    except ValueError:
        print('Ошибка! Необходимо ввести целое число:')
    except Exception:
        print("Ошибка! Необходимо ввести положительное число!")

print(f'Найденная позиция для числа {random_number} равна', binary_search(array_list, random_number, 0, len(array_list)-1))
