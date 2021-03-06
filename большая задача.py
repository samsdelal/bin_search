# Developer: Boris Kuznecov 19704.2 group
# Algorith developed by Joseph Stein in 196

import random
import time


def generate_list():
    z = []
    for i in range(1000):
        z.append(random.randint(0, 10))
    # print(z)
    return z


def simple_search(find_number, listi):
    startt = time.time()
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
        print('simple search - ', time.time() - startt)
        return None
    print('simple search - ', time.time() - startt)
    return mid_num


def recurse_search(find_number, listi, time_f):
    mid_num = len(listi) // 2
    if len(listi) == 0:
        print('rec search - ', time.time() - time_f)
        return 'Нет такого числа'
    if listi[mid_num] == find_number:
        print('rec search - ', time.time() - time_f)
        return mid_num
    else:
        if listi[mid_num] > find_number:
            return recurse_search(find_number, listi[:mid_num], time_f)
        return recurse_search(find_number, listi[mid_num + 1:], time_f)


def main():
    start = time.time()
    listq = [1, 2, 3, 9, 12]
    find_numberr = int(input('Введите искомое число - '))
    ist_of_numbers = list(generate_list())
    find_number = find_numberr
    rec_start = time.time()
    print(recurse_search(find_number, listq, rec_start))
    print(simple_search(find_number, listq))
    print(time.time() - start)


main()
