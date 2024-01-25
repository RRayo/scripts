class MyHashMap:
    def __init__(self):
        self.__HASH_SIZE = 10**6 + 1
        self.__hashTable = {}
    
    def __hashFun(self, key):
        prime = 113
        hash_value = 5381  # Initial value
        hash_value = (hash_value * prime) ^ key
        return hash_value & 0xFFFFFFFF
        

    def add(self, key: int) -> None:
        hashKey = self.__hashFun(key)
        self.__hashTable[hashKey] = key
        
    def put(self, key: int, value: int) -> None:
        hashKey = self.__hashFun(key)
        self.__hashTable[hashKey] = value
        

    def remove(self, key: int) -> None:
        hashKey = self.__hashFun(key)
        if self.contains(key):
            del self.__hashTable[hashKey]
        

    def contains(self, key: int) -> bool:
        hashKey = self.__hashFun(key)
        if hashKey in self.__hashTable.keys():
            return True
        return False
    
    def get(self, key: int):
        if self.contains(key):
            hashKey = self.__hashFun(key)
            return self.__hashTable[hashKey]
        return -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# MyHashMap myHashMap = new MyHashMap();
# myHashMap.add(1);      # Map = [1]
# myHashMap.add(2);      # Map = [1, 2]
# myHashMap.contains(1); # return True
# myHashMap.contains(3); # return False, (not found)
# myHashMap.add(2);      # Map = [1, 2]
# myHashMap.contains(2); # return True
# myHashMap.remove(2);   # Map = [1]
# myHashMap.contains(2); # return False, (already removed)


def main():
    key = 1000000
    obj = MyHashMap()
    obj.add(key)
    #obj.remove(key)
    param_3 = obj.contains(0)
    print(param_3)

if __name__ == "__main__":
    main()
