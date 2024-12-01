


def find_mean(num_list):
    print("Mean: "+str(round(sum(num_list)/(len(num_list)),2)))

def find_median(num_list):
    k=len(num_list)
    if k % 2 == 0:
        a=int(num_list[int(k/2)])
        b=int(num_list[int(k/2)-1])
        median = (a+b)/2
        print("Median: {}".format(median))
    else:
        n= int((k-1)/2)
        print("Median: {}".format(num_list[n]))

def find_mode(num_list):
    #print("Mode: {}".format(statistics.mode(num_list)))
    y ={}
    for a in num_list:
        if not a in y:
            y[a] =1 
        else:
            y[a]+=1 
        result = [g for g,l in y.items() if l==max(y.values())]
    print("Mode: ",end="")
    for i in result:
        print(i, end=" ")
    print(y)
    print(num_list)

num_list = [14, 14, 14, 25, 25, 28, 32, 35, 36, 42, 50, 56, 61] # list(map(int, input().split()))
num_list.sort()
find_mean(num_list)
find_median(num_list)
find_mode(num_list)


# """
# Mean: 35.73
# Median: 35
# Mode: 14 {14: 2, 25: 1, 28: 1, 32: 1, 35: 1, 36: 1, 42: 1, 50: 1, 56: 1, 61: 1}
# [14, 14, 25, 28, 32, 35, 36, 42, 50, 56, 61]
# PS C:\Users\hp\Desktop\work\python_codes> python MeanMedianMode.py
# Mean: 34.83
# Median: 33.5
# Mode: 14 25 {14: 2, 25: 2, 28: 1, 32: 1, 35: 1, 36: 1, 42: 1, 50: 1, 56: 1, 61: 1}
# [14, 14, 25, 25, 28, 32, 35, 36, 42, 50, 56, 61]
# PS C:\Users\hp\Desktop\work\python_codes> python MeanMedianMode.py
# Mean: 33.23
# Median: 32
# Mode: 14 {14: 3, 25: 2, 28: 1, 32: 1, 35: 1, 36: 1, 42: 1, 50: 1, 56: 1, 61: 1}
# [14, 14, 14, 25, 25, 28, 32, 35, 36, 42, 50, 56, 61]

# """