# I want to do a maths test on addition but ten time repeating the test 
#telling Input is right or wrong each time
import math
import random


for i in range(10):
  a = random.randint(1,100)
  b = random.randint(1,100)
  print(a,b)
  Input = int(input("Enter the answer: "))
  total = a+b
  if Input == total:
    print("Right answer")
  else:
    print("Wrong its "+ str(total))