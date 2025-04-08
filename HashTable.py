class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, element in enumerate(self.arr[arr_index]):
            if element[0] == key:
                # print("del", index)
                del self.arr[arr_index][index]

t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 634
t["december 23"] = 67
t["november 12"] = 543
t["october 12"] = 456
t["january 12"] = 423
t["february 12"] = 234
t["may 12"] = 123
t["june 12"] = 15
t["july 12"] = 34
t["529344067295497451"] = 345


# del t['march 8']
print(t.arr)
print(len(t.arr))

