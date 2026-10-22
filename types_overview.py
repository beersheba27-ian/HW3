numbers = [100, 7, 22, -6]
exists = 10 in numbers
print(exists) #False
print(type(exists)) #bool
def exists(numbers, num):
    return num in numbers
print(exists([1, 2,3], 3))
  
