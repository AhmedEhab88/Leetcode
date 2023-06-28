class MyHashSet:
    hashSet = []

    def __init__(self):    
        self.hashSet = []

    def add(self, key: int) -> None:
        if key not in self.hashSet:
            self.hashSet.append(key)

    def remove(self, key: int) -> None:
        if key in self.hashSet:
            self.hashSet.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.hashSet:
            return True
        else:
            return False

obj = MyHashSet()
obj.add(3)
param_2 = obj.contains(3)
print(param_2)
obj.remove(3)
param_3 = obj.contains(3)
print(param_3)