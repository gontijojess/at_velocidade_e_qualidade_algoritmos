import sys
sys.stdout.reconfigure(encoding='utf-8')
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

    def __str__(self):
        result = []
        for arr in self.table:
            for pair in arr:
                result.append(f"{pair[0]}: {pair[1]}")
        return "{ " + ", ".join(result) + " }"
    
social_media_data = HashTable()

profile_anamaria12 = [{'idade': 24}, {'email': 'anamaria@gmail.com'}]
profile_marcospaulo = [{'idade': 32}, {'email': 'marcos_alves@gmail.com'}]
profile_lucasmoreira1 = [{'idade': 24}, {'email': 'moreiralucas@gmail.com'}]
social_media_data.inserir('anamaria12', profile_anamaria12)
social_media_data.inserir('marcospaulo', profile_marcospaulo)
social_media_data.inserir('lucasmoreira1', profile_lucasmoreira1)

searched_username = 'marcospaulo'
searched_profile = social_media_data.buscar('marcospaulo')
print(f'O perfil do usuário {searched_username} é {searched_profile}')

