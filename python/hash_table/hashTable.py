class HashTable:
    def __init__(self):
        # initialize array of size 100
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            # get ASCII character and get the sum of it
            h += ord(char)
        return h % 100

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

if __name__ == '__main__':
    x = HashTable()
    x.get_hash('march 6')
    x['April 20'] = 2001
    x['August 15'] = 1945
    print(x['April 20'])
    print(x['August 15'])
    del x['April 20']
    print(x.arr)
