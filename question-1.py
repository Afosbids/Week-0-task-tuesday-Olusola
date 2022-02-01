def prime_number_checker(num):
    prime_factors = [1]
    if (num > 1):
        for j in range(2, (num + 1)): 
            if (num% j) == 0:  
                prime_factors.append(j)
                
    if len(prime_factors) > 2:
        return f"{num} is not a prime number. \n{prime_factors}"
    elif (num <= 1):
        return f"{num} is not a prime number, negative numbers, 1 and zero are not prime numbers"  
    else:  
        return f"{num} is a prime number."
           

print(prime_number_checker(9))