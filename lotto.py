import random
def exists(numbers, num):
    # numbers list of integers
    # num - being tested number for existence
    i = 0
    size = len(numbers)
    while i < size and numbers[i] != num:
        i += 1
    return i < size  

def distinct_random_numbers(min, max, size):
    """
    
    returns list with "size" distinct random numbers 
    each number >= "min" and <= "max"
    if creating "size" distinct random numbers is impossible, return empty array
    requirement: to use the above function "exists" and one while-loop
    """
    result = []
    if size > 0 and max - min + 1 >= size:
        i = 0
        while i < size:
            num = random.randint(min, max)
            if not exists(result, num):
                i += 1
                result.append(num)
    return result
print (distinct_random_numbers(1, 49, 7))