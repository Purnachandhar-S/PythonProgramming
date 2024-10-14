#n=int(input("Enter a number 1- 100"))

#number divisible 1 and itself is a prime number
n=41

is_prime_number= False

for i in range(2,n-1):
  if n%i==0:
    is_prime_number= False
    print(i)
    break
  else:
    is_prime_number=True

if is_prime_number:
  print(is_prime_number)
else:
  print(is_prime_number)


