

def checkPrime(n):
    if n > 1:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
            else:
                return True
    else:
        return True




def till_prime():
    prime_list = []
    x = int(input("enter number"))
    for i in range(2, x + 1):
        if checkPrime(i):
            prime_list.append(i)
        else:
            pass    
    print(prime_list)     
        
        
def firstn_primes():
    primes = []
    num = 2
    n = int(input("enter number"))
    
    while len(primes) < n:
        if checkPrime(num):
            primes.append(num)
        num += 1

    print(primes)
       
             
