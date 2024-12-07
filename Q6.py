import sys
sys.stdout.reconfigure(encoding='utf-8')
import random
import time

def bubble_sort(array):
  for i in range(len(array)):
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

def execution_time_bubble_sort(lista):

    start_time = time.time()
    bubble_sort(lista)
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"O tempo de execução para {len(lista)} elementos é de {execution_time:.6f} segundos")


random_arr_1000 = sorted([round(random.uniform(1, 100), 2) for _ in range(1000)])
random_arr_10000 = sorted([round(random.uniform(1, 100), 2) for _ in range(10000)])

execution_time_bubble_sort(random_arr_1000)
execution_time_bubble_sort(random_arr_10000)
