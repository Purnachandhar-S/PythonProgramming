def add(a,b):
  answer=a+b
  print(str(a)+ " + "+ str(b) + " = " + str(answer))

def sub(a,b):
  answer=a-b
  print(str(a)+ " - "+ str(b) + " = " + str(answer))

def mul(a,b):
  answer=a*b
  print(str(a)+ " * "+ str(b) + " = " + str(answer))

def div(a,b):
  answer=a/b
  print(str(a)+ " / "+ str(b) + " = " + str(answer))




while True:
  operations = ["A. Addition","B. Subtraction", "C. Multiplication","D. Division","E. Exit"]
  for i in operations:
    print(i)
  choice = input("Input YOur choice: ")
  if choice=="a" or choice=="A":
    a= int(input("Input First number: "))
    b = int(input("Input second number: "))
    add(a,b)
  elif choice=="b" or choice=="B":
    a= int(input("Input First number: "))
    b = int(input("Input second number: "))
    sub(a,b)
  elif choice=="c" or choice=="C":
    a= int(input("Input First number: "))
    b = int(input("Input second number: "))
    mul(a,b)
  elif choice == "d" or choice=="D":
    a= int(input("enter first number: "))
    b= int(input("Input second number: "))
    div(a,b)
  elif choice=="E" or choice=="e":
    print("PROGRAM HAS ENDED")
    quit()

print("Hello world!")

#  how to get a biggest prime number
num = 1234567
# is_prime = True
# for a in range(100):
#   num+=2
#   for i in range(2,100):
#     if num%i==0:
#       is_prime= False
#   if is_prime==True:
#     print(num)
#   else:
#     print(False)

print(41/ c4)

    
