class MaxHeap():
    def __init__(self, name):
        self.count = 0
        self.heap_list = [None]
        self.name = name
    
    # adds value to desired heap and heapifys up
    def add(self, value):
        self.heap_list.append(value)
        print(f"{value} added to {self.name}")
        self.count += 1
        if self.heap_list[1] != value:
            self.heapify_up()
     
    # brings element up to appropriate position in the heap
    def heapify_up(self):
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            # loops create key variables for the parent and child
            for key in child:
                child_key = key 
            for key in parent:
                parent_key = key
            if parent[parent_key] < child[child_key]:
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)
        print(f"{self.name} reorganized. {self.heap_list[1]} is currently the highest priority.")
        
    # brings element down to appropriate position in the heap
    def heapify_down(self, idx=1):
        while self.child_present(idx):
            larger_child_idx = self.get_larger_child_idx(idx)
            child = self.heap_list[larger_child_idx]
            parent = self.heap_list[idx]
            # loops create key variables for the parent and child
            for key in child:
                child_key = key
            for key in parent:
                parent_key = key
            if parent[parent_key] < child[child_key]:
                self.heap_list[idx] = child
                self.heap_list[larger_child_idx] = parent
            idx = larger_child_idx

    def remove_by_key(self, remove_key):
        if self.count == 0:
            print(f"{self.name} is empty")
            return
        keys = []
        # loop adds keys to the keys list
        for element in self.heap_list:
            if element != None:
                for key in element:
                    keys.append(key)
        if remove_key not in keys:
            print(f"{remove_key} is not in {self.name}")
            return 
        idx = keys.index(remove_key) + 1
        if self.count == 1:
           removed = self.heap_list.pop()
           print(f"{removed} removed, Hoorah! {self.name} is now empty")
           self.count -= 1
           return removed
        else:
           # target replaces the first variable from the remove_max method to target the desired key
           target = self.heap_list[idx]
           last = self.heap_list[-1]
           self.heap_list[idx] = last
           self.heap_list[-1] = target
           removed = self.heap_list.pop()
           self.count -= 1
           self.heapify_down()
           self.heapify_up()
           self.print_heap()
           return removed
        

    def get_larger_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            for key in left_child:
                left_child_key = key
            right_child = self.heap_list[self.right_child_idx(idx)]
            for key in right_child:
                right_child_key = key
            if left_child[left_child_key] > right_child[right_child_key]:
                return self.left_child_idx(idx)
            else:
                return self.right_child_idx(idx)


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
           print(self.heap_list)
           first = self.heap_list[1]
           last = self.heap_list[-1]
           self.heap_list[1] = last
           self.heap_list[-1] = first
           removed = self.heap_list.pop()
           self.count -= 1
           self.heapify_down()
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

    def print_heap(self):
        # a copy of the heap is created to make use of the heapify method
        heap_copy = MaxHeap("copy")
        heap_copy.heap_list = self.heap_list.copy()
        heap_copy.count = self.count
        lst = []
        while heap_copy.count > 0:
            if heap_copy.count == 0:
                print(f"{self.name} is empty")
                return 
            elif heap_copy.count == 1:
                removed = heap_copy.heap_list.pop()
                heap_copy.count -= 1
                lst.append(removed)
            # modified remove_max method that replaces self.heap_list with the copy version
            else:
                first = heap_copy.heap_list[1]
                last = heap_copy.heap_list[-1]
                heap_copy.heap_list[1] = last
                heap_copy.heap_list[-1] = first
                removed = heap_copy.heap_list.pop()
                heap_copy.count -= 1
                heap_copy.heapify_down()
                lst.append(removed)
        print(lst)