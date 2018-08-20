import math

def is_prime(num):
    '''
    Better method of checking for primes.
    '''
    if num % 2 == 0 and num > 2:
            print("not prime")
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            print(' prime')
is_prime(13)