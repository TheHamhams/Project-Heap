class MaxHeap():
    def __init__(self, name):
        self.count = 0
        self.heap_list = [None]
        self.name = name
    
    def add(self, value):
        self.heap_list.append(value)
        if self.heap_list[1] != value:
            self.heapify_up
        print(f"{value} added to {self.name}, {self.heap_list}")
        self.count += 1
        return 

    def heapify_up():
        print("Heapifying up")

test = MaxHeap("test")
test.add({"sweep": 1})
test.add({"vacuum": 2})