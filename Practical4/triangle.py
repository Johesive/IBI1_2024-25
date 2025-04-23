#it's the i th triangle
#consider adding from 1 to i
#j = 0
#for k in 1 to i:
#add k to j

for i in range(1,11): 
    j = 0    
    for k in range(1,i+1): 
        j += k
    print(j)  
