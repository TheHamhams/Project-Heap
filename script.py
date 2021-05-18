from heap import MaxHeap

test = MaxHeap("test")

test.add({"sweep": 1})
test.add({"vacuum": 2})
test.add({"dust": 5})
test.add({"iron": 3})
test.add({"eat": 4})
test.add({"sleep": 2})
test.add({"run": 7})
test.remove_by_key("iron")
test.remove_max()
test.remove_by_key("sleep")

