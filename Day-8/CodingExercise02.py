#Prime Number Checker
def prime_checker(number):
  is_prime = True
  for i in range(2,number-1):
    if number%i == 0:
      is_prime = False
  if is_prime:
    print(f"{number} is a Prime Number.")
  else:
    print(f"{number} is Not a Prime Number.")


n = int(input("Check this number: "))
prime_checker(number=n)