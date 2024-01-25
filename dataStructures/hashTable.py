
class MyHashSet:
    def __init__(self):
        self.__HASH_SIZE = 10**6 + 1
        self.__hashTable = {}
    
    def __hashFun(self, key):
        prime = 113
        # return key*(key+prime) % self.__HASH_SIZE
        return hash(key)
        

    def add(self, key: int) -> None:
        hashKey = self.__hashFun(key)
        self.__hashTable[hashKey] = key
        

    def remove(self, key: int) -> None:
        hashKey = self.__hashFun(key)
        if self.contains(key):
            del self.__hashTable[hashKey]
        

    def contains(self, key: int) -> bool:
        hashKey = self.__hashFun(key)
        if hashKey in self.__hashTable.keys():
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      # set = [1]
# myHashSet.add(2);      # set = [1, 2]
# myHashSet.contains(1); # return True
# myHashSet.contains(3); # return False, (not found)
# myHashSet.add(2);      # set = [1, 2]
# myHashSet.contains(2); # return True
# myHashSet.remove(2);   # set = [1]
# myHashSet.contains(2); # return False, (already removed)


def main():
    key = 1000000
    obj = MyHashSet()
    obj.add(key)
    #obj.remove(key)
    param_3 = obj.contains(0)
    print(param_3)

if __name__ == "__main__":
    main()
