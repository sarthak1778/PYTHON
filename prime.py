#a number is prime or not

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


"""
Why only √n?
Suppose
n = 36
Factor pairs are
1 × 36
2 × 18
3 × 12
4 × 9
6 × 6
Notice:After √36 = 6, the factors repeat in reverse.
Checking beyond 6 is unnecessary.
Another example:
49 = 7 × 7
√49 = 7
Checking numbers greater than 7 finds nothing new.
So instead of
2,3,4,...,48
you only check
2,3,4,5,6,7
This makes the algorithm much faster."""

while True:
    n=int(input("Enter a number to check if it is prime: "))
    print(prime(n)) 


