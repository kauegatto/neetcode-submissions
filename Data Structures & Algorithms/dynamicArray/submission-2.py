class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None] * capacity
        self.lastSlot = len(self.array)-1
        self.capacity = capacity
        self.itemsUsed = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if self.get(i) is None:
            self.itemsUsed+=1
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.itemsUsed:
            self.resize()
        self.array[self.itemsUsed] = n
        self.itemsUsed += 1
    def popback(self) -> int:
        self.itemsUsed -= 1
        return self.array[self.itemsUsed]

    def resize(self) -> None:
        self.capacity = self.capacity*2
        newArray = [None] * self.capacity
        for i in range(len(self.array)):
            newArray[i] = self.array[i]
        self.array=newArray
        self.lastSlot = len(self.array)-1

    def getSize(self) -> int:
        return self.itemsUsed


    def getCapacity(self) -> int:
        return self.capacity