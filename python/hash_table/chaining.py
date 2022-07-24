# Solving the collision by chaining
import enum


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            # get ASCII character and get the sum of it
            h += ord(char)
        return h % 100

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        
        for idx, element in enumerate(self.arr[h]):
            # if I have an element for the key
            if len(element) == 2 and element[0] == key:
                # change the value
                self.arr[h][idx] = (key,val)
                found = True
                break
        # if the key does not exist in hash table
        if not found:
            self.arr[h].append((key,val))
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]

if __name__ == '__main__':
    x = HashTable()
    x["march 6"] = 20
    x["march 8"] = 80
    x["march 9"] = 100
    x["march 17"] = 250

