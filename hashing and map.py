class Hash:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def hashing(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hashing(key)
        for i, (k, v) in enumerate(self.hash_table[index]):
            if k == key:
                self.hash_table[index][i] = (key, value)
                return
        self.hash_table[index].append((key, value))

    def get(self, key):
        index = self.hashing(key)
        for k, v in self.hash_table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hashing(key)
        for i, (k, v) in enumerate(self.hash_table[index]):
            if k == key:
                del self.hash_table[index][i]
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.hash_table):
            if bucket:
                print(f"{i} - {bucket}")


# Example usage
h = Hash(4)
h.insert("id", 101)
h.insert("name", "varsha")
h.display()
h.insert("id",102)
print(h.get("id"))
h.delete("id")
h.display()
