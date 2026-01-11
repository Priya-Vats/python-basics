student = {
    "name" : "Priya",
    "Score" : {
        "chem" : 95,
        "phy" : 98,
        "maths" : 96,
    } 
}

print(student.keys()) #return all keys
print(len(list(student.keys())))
print(student.values()) #return all values
print(student.items())  #return all key value pairs as tuples

#print(student["name2"]) #error
print(student.get("name")) #no error -> none, returns the value according to the key

student.update({"city" : "Dubai"}) #inserts the specified or new items to the dictonaries

new_dict = {"city" : "karnal", "state" : "haryana"}
student.update(new_dict)
print(student)