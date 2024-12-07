import sys
sys.stdout.reconfigure(encoding='utf-8')

def selectionSort(arr):
    size = len(arr)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            current_player_name, current_player_score = list(arr[j].items())[0]
            lowest_player_name, lowest_player_score = list(arr[min_index].items())[0]
            if current_player_score < lowest_player_score:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
 
arr = [{'Marcos': 300}, {'Marina': 450}, {'Marcelo': 120}, {'André': 680}, {'Carolina': 340}, {'Júlia': 553}, {'Lucas': 230}]
selectionSort(arr)
print(f'O registro de jogadores por pontuação após a ordenação pelo selection sort é: {arr}')
