from heap import MaxHeap

test = MaxHeap("test")

test.add({"sweep": 1})
test.add({"vacuum": 2})
test.add({"dust": 5})
test.add({"iron": 3})
test.remove_max()
test.remove_max()

