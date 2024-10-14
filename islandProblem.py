'''
# n = input("enter each box contain how many pieces :")
# e = input("Number of sweets you can daily consume :")
# d= input("number of days you have to be on that island :")

n = 50
e = 48
d = 7
# result is what is the minimum number of times the you need to buy sweet to servive
# return -1 if not possible
# day starts with monday you cant buy sweets on the sunday.

count = 1
remSweets = n
for i in range(1,d):
  remSweets = remSweets  - e
  print("rem sweets:"+ str(remSweets) + " on the day " + str(i) + " count " + str(count))
  
  if remSweets<e:
    if i%7 == 0:
      count = -1 
      print(True)
    else:
      remSweets = remSweets + n 
      count = count + 1

print(count)
'''
n = 50  # Each box contains 50 pieces
e = 20  # You consume 48 sweets daily
d = 7   # Number of days to be on the island (including Sundays)

# If it's impossible to survive (need more than what you can store in 1 box):
if e > n:
    print(-1)  # Return -1 because it's impossible to survive
else:
    # Variables initialization
    count = 1  # Initial number of purchases
    remSweets = n  # Starting with 1 box of sweets

    for i in range(1, d + 1):
        remSweets -= e  # Decrease sweets by the amount consumed each day 
        print("rem sweets:"+ str(remSweets) + " on the day " + str(i) + " count " + str(count))
        
        if i % 7 == 6:  # Check if it's Saturday (before Sunday)
            # If you don't have enough sweets for both Sunday and Monday, it's impossible
            if remSweets < 2 * e:
                count = -1
                print("# If you don't have enough sweets for both Sunday and Monday, it's impossible")
                break
        
        if remSweets < e:  # If sweets remaining are less than required for the next day
            if i % 7 == 0:  # If it's Sunday, can't buy sweets
                count = -1  # It's impossible to survive
                print("If it's Sunday, can't buy sweets")
                break
            else:
                remSweets += n  # Buy a new box of sweets
                count += 1  # Increment purchase count
    
    print(count)
