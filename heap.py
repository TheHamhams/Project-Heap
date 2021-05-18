class MaxHeap():
    def __init__(self, name):
        self.count = 0
        self.heap_list = [None]
        self.name = name
    
    def add(self, value):
        self.heap_list.append(value)
        print(f"{value} added to {self.name}")
        self.count += 1
        if self.heap_list[1] != value:
            self.heapify_up()
     

    def heapify_up(self):
        print("Heapifying up")
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            for key in child:
                child_key = key 
            parent = self.heap_list[self.parent_idx(idx)]
            for key in parent:
                parent_key = key
            if parent[parent_key] < child[child_key]:
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)
        print(f"{self.name} reorganized. {self.heap_list[1]} is currently the highest priority.")
        

    def heapify_down(self):
        print("Heapifying down")
        idx = 1
        while self.child_present(idx):
            larger_child_idx = self.get_larger_child_idx(idx)
            child = self.heap_list[larger_child_idx]
            for key in child:
                child_key = key
            parent = self.heap_list[idx]
            for key in parent:
                parent_key = key
            if parent[parent_key] < child[child_key]:
                self.heap_list[idx] = child
                self.heap_list[larger_child_idx] = parent
            idx = larger_child_idx
        

    def get_larger_child_idx(self, idx):
        pass


    def remove_max(self):
        if self.count == 0:
            print(f"{self.name} is empty")
            return 
        elif self.count == 1:
           removed = self.heap_list.pop()
           print(f"{removed} removed, Hoorah! {self.name} is now empty")
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