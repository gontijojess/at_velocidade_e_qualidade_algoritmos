import sys
sys.stdout.reconfigure(encoding='utf-8')

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._add(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._add(current.right, value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        if value < current.value:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)


tree = BinaryTree()

for value in [100, 50, 150, 30, 70, 130, 170]:
    tree.add(value)

print("Preço 70 está disponível?", tree.search(70))
print("Preço 90 está disponível?", tree.search(90))