import sys
sys.stdout.reconfigure(encoding='utf-8')

class Queue:
    def __init__(self):
        self.itens = []


    def new_customer(self, item):
        self.itens.append(item)

    def customer_being_attended(self):
        if len(self.itens) == 0:
            print("A fila está vazia")
            return None
        return self.itens.pop(0) 

    def peek(self):
        if len(self.itens) == 0:
            print("A fila está vazia")
            return None
        return self.itens[0]

    def size(self):
        return len(self.itens)

    def display(self):
        if len(self.itens) == 0:
            print("A fila está vazia")
        else:
            for item in self.itens:
                print(item, end=", ")
            print()

customers_queue = Queue()
customers_queue.new_customer("Marco Alberto")
customers_queue.new_customer("Ana Clara")
customers_queue.new_customer("João de Souza")
customers_queue.new_customer("Maria Aparecida")
customers_queue.new_customer("Simone Silva")
customers_queue.new_customer("Lucas Pinheiro")

print('- Fila inicial:')
customers_queue.display()
customers_queue.customer_being_attended()
print('- Fila após Marco Alberto ser chamado para atendimento:')
customers_queue.display()
customers_queue.new_customer("Angela Maria")
customers_queue.customer_being_attended()
customers_queue.customer_being_attended()
print('- Fila após Ana Clara e João de Souza serem atendidos e Angela Maria chegar ao final da fila:')
customers_queue.display()
