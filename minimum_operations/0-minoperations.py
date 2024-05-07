#/usr/bin/python3

def minOperations(n):
    if n <= 1:
       return 0
    
    divisor = 2

    num_of_operations = 0

    while n > 1:
        if n % divisor == 0:
            n = n / divisor
            print("\nn =n / divisor", n)

            num_of_operations = num_of_operations + divisor
            print("\nnum of ops", num_of_operations)

        else:
            divisor += 1
            print("divisor after increment: ", divisor)
    
    return num_of_operations

n=12

print(minOperations(n))

