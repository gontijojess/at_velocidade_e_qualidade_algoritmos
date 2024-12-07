class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.size = 0 

    def hash(self, key):
        return hash(key) % self.capacity

    def inserir(self, key, value):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return False
        
        self.table[index].append([key, value])
        self.size += 1
        return True

    def buscar(self, key):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remover(self, key):
        index = self.hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                self.size -= 1
                return True
        return False

    def __str__(self):
        result = []
        for arr in self.table:
            for pair in arr:
                result.append(f"{pair[0]}: {pair[1]}")
        return "{ " + ", ".join(result) + " }"

no_duplicates_list = [1, 2, 3, 4, 5, 6, 7]
duplicates_list = [1, 2, 3, 4, 5, 3, 8]

hash_table = HashTable(len(duplicates_list))

def is_there_duplicates(arr, table):
    for x in arr:
        table.inserir(x, None)
    if len(arr) != table.size: 
        return True
    else:
        return False


print(is_there_duplicates(duplicates_list, hash_table))
