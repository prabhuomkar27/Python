
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Ask the user for input
user_number = int(input("Enter a number to check if it's prime: "))

# Check and display the result
if is_prime(user_number):
    print(f"{user_number} is a prime number.")
else:
    print(f"{user_number} is not a prime number.")
  
