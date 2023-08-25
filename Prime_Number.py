
n = int(input("enter a number:"))
is_prime = True

for i in range(2,(n//2)+1):
    if n % i == 0:
        print(n," is not a prime number")
        is_prime = False
        break
if is_prime == True:
    print(n,"is a prime number")


