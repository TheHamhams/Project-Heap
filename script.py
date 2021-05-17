from heap import MaxHeap

test = MaxHeap("test")
test2 = MaxHeap("test2")
test.add({"sweep": 1})
test.add({"vacuum": 2})
test.add({"dust": 5})

test2.remove()
test2.add({"eat": 1})
test2.add({"sleep": 3})
test2.remove()
test2.remove()
