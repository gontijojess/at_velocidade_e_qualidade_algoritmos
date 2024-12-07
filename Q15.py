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

    def _get_min(self, current):
        while current.left is not None:
            current = current.left
        return current
    
    def _get_max(self, current):
        while current.right is not None:
            current = current.right
        return current



tree = BinaryTree()

for value in [85,70,95,60,75,90,100]:
    tree.add(value)


min = tree._get_min(tree.root)
max = tree._get_max(tree.root)

print(f"A nota mínim é {min.value} e a nota máxima é {max.value}")

