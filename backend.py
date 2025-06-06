# check prime number
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")

print(f"{num} is not a prime number and its ok.")

print(f"{num} is not a prime number and what to do.")
