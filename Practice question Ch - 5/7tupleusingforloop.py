#search for a number x in this tupe using loop
tup = [1,4,9,16,25,36,49,64,81,100,49]

#The process of finding a number is known a linear(search in a single line) search.

x = 49

idx = 0
for el in tup:
    if(el == x):
        print("Found at idx", idx)
        break
    idx += 1
    #else:
    #    print("finding...")
    #idx += 1
