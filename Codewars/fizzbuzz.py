def fizzbuzz(n):
    final_array = []
    
    # your code here
    if n < 1:
        return None

    for number in range(1,n+1):
        if (number % 3 == 0) and (number % 5 == 0):
            final_array.append("FizzBuzz")
        elif number % 3 == 0:
            final_array.append("Fizz")
        elif number % 5 == 0:
            final_array.append("Buzz")
        
        else:
            final_array.append(number)
            
    return final_array 


print(fizzbuzz(100))
