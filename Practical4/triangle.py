for i in range(1,11):  #first determine it's the i th triangle
    j = 0    #consider adding from 1 to i
    for k in range(1,i+1):  #add 1, then 2, all the way to i
        j += k
    print(j)  #output
