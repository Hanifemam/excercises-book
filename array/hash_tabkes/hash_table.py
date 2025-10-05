class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.size
        return hash

    def get(self, key):
        for pair in self.hash_table[self._hash(key)]:
            if key == pair[0]:
                return pair[1]
        return None

    def add(self, key, value):
        self.hash_table[self._hash(key)].append([key, value])

    def keys(self):
        keys = []
        for items in self.hash_table:
            for pair in items:
                keys.append(pair[0])
        return keys

    def values(self):
        values = []
        for items in self.hash_table:
            for pair in items:
                values.append(pair[1])
        return values


hash_table = HashTable(4)
hash_table.add("hanif", 4)
print(hash_table.keys())
print(hash_table.values())
