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

num_list = list(map(int, input().split()))
num_list.sort()
find_mean(num_list)
find_median(num_list)
find_mode(num_list)
