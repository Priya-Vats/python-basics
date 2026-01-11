#hash value or hasable value are immutable and can not be changed lifetime . It means the value assigned to a variable can not the changed.

"""collection = set()
collection.add(1)
collection.add(2)
collection.add("Priya Vats")
collection.add((1,2,3))

collection.add([1,2,3])

collection.remove(1)
collection.clear()
collection.pop()
print(collection)"""

set1 = {1,2,3}
set2 = {2,3,4}

#print(set1.union(set2)) #{1,2,3,4}
print(set1.intersection(set2))