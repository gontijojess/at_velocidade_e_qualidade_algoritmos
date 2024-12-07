import sys
sys.stdout.reconfigure(encoding='utf-8')
import random

def binary_search(arr, isbn_target):
    begin = 0
    end = len(arr) - 1
    num_iterations = 0

    while begin <= end:
        num_iterations += 1
        middle = (begin + end) // 2
        if arr[middle] == isbn_target:
            return middle, num_iterations
        elif arr[middle] < isbn_target:
            begin = middle + 1
        else:
            end = middle - 1
    return -1

def linear_search(arr, isbn_target):
    num_iterations = 0
    for index, isbn in enumerate(arr):
        num_iterations += 1
        if isbn == isbn_target:
            return index, num_iterations
    return -1

random_arr = sorted([random.randint(10**(13-1), 10**13-1) for _ in range(100000)])
random_num = random.choice(random_arr)

num_binary, iterations_binary = binary_search(random_arr, random_num)
num_linear, iterations_linear = linear_search(random_arr, random_num)

print(f'Para encontrar com busca binária o número {random_num}, {num_binary}° elemento da lista, foi preciso {iterations_binary} iterações')
print(f'Para encontrar com busca lienar o número {random_num}, {num_linear}° elemento da lista, foi preciso {iterations_linear} iterações')