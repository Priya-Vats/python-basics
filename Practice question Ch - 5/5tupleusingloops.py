num = (1,4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36
i = 0 #initialization
while i < len(num):
    #print(num[i])
    if(num[i] == x):
        print("Found at index", i)
    else:
        print("finding...")
    i += 1