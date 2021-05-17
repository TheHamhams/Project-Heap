class MaxHeap():
    def __init__(self, name):
        self.count = 0
        self.heap_list = [None]
        self.name = name
    
    def add(self, value):
        self.heap_list.append(value)
        if self.heap_list[1] != value:
            self.heapify_up()
        print(f"{value} added to {self.name}, {self.heap_list}")
        self.count += 1
        return 

    def heapify_up(self):
        return print("Heapifying up")
        

    def heapify_down(self):
        return print("Heapifying down")


    def remove(self):
        if self.count == 0:
            print(f"{self.name} is empty")
            return 
        elif self.count == 1:
           removed = self.heap_list.pop()
           print(f"{removed} removed, {self.name} is now empty")
           self.count -= 1
           return removed
        else:
           first = self.heap_list[1]
           last = self.heap_list[-1]
           self.heap_list[1] = last
           self.heap_list[-1] = first
           removed = self.heap_list.pop()
           self.heapify_down()
           self.count -= 1
           print(f"Congradulations! {first} removed from {self.name}. {self.heap_list[1]} is your new highest priority.")
           return removed
    
    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count