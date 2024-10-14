import string
import random

characters = list(string.ascii_letters + string.digits + " !@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    
    password = "" .join(password)
    print(password)

# option = input("Do you want to generate a password? (Yes/No): ")

# if option == "y":
#     generate_password()
# elif option == "n":
#     print("Program ended")
#     quit()
# else:
#     print("Invalid input, please input Yes or No")
#     quit()

"""
# reading about the random module 

1Getstate() -- is good module to create a array of radom numbers in the given range and given length 
2setstate()-- is dont understand about this much ,,but after getstate when you use setstate given the same values in less given length
3randrange()-- says its returns a random numbers within the range -- i tried its good
4randint() -- same as above
5choice() -- Returns a random item from a list, tuple, or string 
6choices() -- Returns multiple random elements from the list with replacement 
                syntax : random.choices(sequence,weights=None, cum_weights = None, k=1)
                weights is possibility for each item 
7sample() --Returns a particular length list of items chosen from the sequence
8random()-- Generate random floating numbers
9uniform () -- return a random floating number between two numbers both inclusive
10 shuffle()-- shuffles the list 


"""

state = random.getstate()
# print 10 random numbers
print(random.sample(range(20), k =10))
# restore state 
random.setstate(state)
# print same first five random numbers
# as above
print(random.sample(range(20), k=6))

print(type(random.randrange(7,678)))

strings = "Hello world hi"
print(random.choice(strings)) #r 

myList =['apple','banana','carrot','dhosakay']
print(random.choices(myList,weights=[1,2,3,10],k=5))
print(random.sample(myList,3))
print(round(random.random()*100,0))
myNumbers = [1,3,4,5,6,6,6]
shuffled = random.shuffle(myNumbers)
print(myNumbers)


