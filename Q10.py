import sys
sys.stdout.reconfigure(encoding='utf-8')
class Stack:
    def __init__(self):
        self.history = []
        self.next = []
        self.current = None
    
    def visit(self, page):
        if self.current is not None:
            self.history.append(self.current)
        self.current = page
        self.next.clear()
        print(f"Página atual: {self.current}")

    def goBack(self):
        if not self.history:
            print("Não há página anterior")
            return
        self.next.append(self.current)
        self.current = self.history.pop()
        print(f"Você voltou para a página {self.current}")

    def goNext(self):
        if not self.next:
            print("Não há página anterior")
            return
        self.history.append(self.current)
        self.current = self.next.pop()
        print(f"Você seguiu para a próxima página {self.current}")

browser = Stack()

browser.visit('menu')
browser.visit('products_category')
browser.visit('products_list')
browser.visit('products_details')
browser.visit('products_price')

browser.goBack()
browser.goBack() 

browser.goNext()
browser.goNext()  
