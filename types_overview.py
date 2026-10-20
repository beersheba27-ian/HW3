age = 50
comment = "child" if age < 13 else "adult"
print(comment)  

numbers = [1, 2, 10, 7, 8]
evenOdd = [ str(num) + '. ' + ("even" if num % 2 == 0 else "odd") for num in numbers]
  
print (evenOdd)