
def isprime(n):
    is_prime =False
    if number%number==0 and number%1==0:
        for n in range(2,round(number/2)+1):
            if number%n==0:
                is_prime=False
                break
            else:
                is_prime=True
    return is_prime
number=int(input('enter a number = '))
print(isprime(number))