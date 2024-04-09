
import copy


class HashTable:
    def __init__(self, size=10, growth_factor=2):
        self.size = size
        self.growth_factor = growth_factor
        self.used_slots = 0
        self.arr = [0] * self.size

    def increase_space_and_rehash(self):  # still in progress
        self.size *= self.growth_factor
        temp_arr = copy.deepcopy(self.arr)
        self.arr = [0] * self.size
        for i in range(len(temp_arr)):
            if temp_arr[i] != 0:
                self.insert(temp_arr[i][0], temp_arr[i][1])

    def hashing(self, key):
        hashed_key = hash(key)
        index = hashed_key % self.size
        return index

    def insert(self, key, value):
        index = self.hashing(key)
        if self.arr[index] != 0:
            index = self.collision_handling(key, index)
        self.arr[index] = (key, value)
        self.used_slots += 1

        if self.used_slots > len(self.arr) / 1.5:
            self.increase_space_and_rehash()

    def get(self, key):
        index = self.hashing(key)
        initial_index = index

        n = 1
        while True:  # modified collision logic that checks if keys match
            if self.arr[index] != 0:
                if self.arr[index][0] == key:
                    return self.arr[index][1]

            index = (initial_index + n) % self.size
            n += 1
            if index == initial_index:  # key not found
                break

        raise KeyError("Key not found")

    def delete(self, key):
        index = self.hashing(key)
        initial_index = index
        n = 1
        while True:  # modified collision logic that checks if keys match
            if self.arr[index] != 0:
                if self.arr[index][0] == key:
                    self.arr[index] = 0

            index = (initial_index + n) % self.size
            n += 1
            if index == initial_index:  # key not found
                break

    def collision_handling(self, key, idx):  # linear probing technique
        n = 0
        while self.arr[idx] != 0:
            n += 1
            idx = (hash(key) + n) % self.size

        return idx


h = HashTable(8, 2)
h.insert('John', 25)
h.insert('Misho', 24)
h.insert('Alek', 21)
h.insert('Simo', 23)
h.insert('Gosho', 55)
h.insert('Gosho2', 55)

print(h.arr)

print(h.get('John'))
print(h.get('Misho'))
print(h.get('Alek'))
print(h.get('Simo'))
print(h.get('Gosho'))

print(h.arr)
h.delete('Gosho2')
print(h.arr)
