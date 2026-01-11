#Write a recursive function to calculate the sum of first n natural numbers. 
"""def sum(n):
    if (n == 0):
        return 0
    return sum(n-1) + n

print(sum(5))"""

#Write a reursive function to print all elements in a list.
#Hint : use list and index as parameters.

num = ["a","b","c","d","e","f","g"]
def print_list(list, idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

print_list(num)