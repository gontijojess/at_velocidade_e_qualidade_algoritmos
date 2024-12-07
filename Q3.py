import sys
sys.stdout.reconfigure(encoding='utf-8')

def linear_search_iterative(arr, target):
    for i in arr:
        if i['nome'].lower() == target.lower():
            return f'O número de telefone da {i['nome']} é {i['telefone']}'
    return 'Nenhum contato foi encontrado com esse nome'

contatos = [
    {"nome": "Marina", "telefone": "(11) 99999-9999"},
    {"nome": "Daniel", "telefone": "(61) 98888-8888"},
    {"nome": "Ana Clara", "telefone": "(24) 97777-7777"},
    {"nome": "Marcelo", "telefone": "(11) 96666-6666"},
    {"nome": "Sofia", "telefone": "(21) 95555-5555"},
]

print(linear_search_iterative(contatos, 'Sofia'))
print(linear_search_iterative(contatos, 'Melissa'))
