import random
import time


def generate_list():
    z = []
    for i in range(10):
        z.append(bin(random.randint(0, 10)))
    # print(z)
    return z


def simple_search(find_number, listi):
    mid_num = len(listi) // 2
    start = 0
    end = len(listi) - 1
    while listi[mid_num] != find_number and start <= end:
        if find_number > listi[mid_num]:
            start = mid_num + 1
        elif find_number < listi[mid_num]:
            end = mid_num - 1
        mid_num = (start + end) // 2
    if start > end:
        return None
    else:
        return mid_num


def recurse_search(find_number, listi):
    mid_num = len(listi) // 2
    if len(listi) == 0:
        return 'Нет такого числа'
    if listi[mid_num] == find_number:
        return mid_num
    else:
        if listi[mid_num] > find_number:
            return recurse_search(find_number, listi[:mid_num])
        return recurse_search(find_number, listi[mid_num + 1:])


def main():
    start = time.time()
    listq = [bin(1), bin(2), bin(3), bin(4), bin(5), bin(6), bin(7), bin(8), bin(9)]
    find_numberr = int(input('Введите искомое число - '))
    ist_of_numbers = list(generate_list())
    find_number = bin(find_numberr)
    print(recurse_search(find_number, listq))
    print(simple_search(find_number, listq))
    print(time.time()-start)


main()
