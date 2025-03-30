
import numpy as np
import matplotlib.pyplot as plt

for i in range (0,10): #10*i% is the rate of vaccination
    
    #There is a question. 
    #If vaccinated number is 100%, in the context there will be no infected people at first, which is contradictory to the assumption that one person is affected. 
    #As a result, I choose to set the range as (0,10) instead of (0,11).
    
    N = 10000
    Vaccinated = 1000*i
    Suspectible = N-Vaccinated-1
    Infected = 1
    Recovered = 0
    label = 10*i

    beta = 0.3
    gamma = 0.05

    S = [Suspectible]  #create the lists
    I = [Infected]
    R = [Recovered]

    for _ in range(1000):  #do the operation for 1000 times
        new_S = S.copy()  #create a copy of the population to avoid overwriting during updates
        new_I = I.copy()
        new_R = R.copy()
        
        probability_of_infection = beta*I[-1]/N  #calculate probability of infection, while probability of recovery equals to gamma

        NewInfections = np.random.choice(range(2),new_S[-1],p=[1-probability_of_infection,probability_of_infection]).sum()
    #randomize: all people who is in the suspectible group is randomly given the number 0 and 1, sum it altogether and get the infected number
        NewRecoveries = np.random.choice(range(2),new_I[-1],p=[1-gamma,gamma]).sum()
    #randomize: all people who is in the infected group is randomly given the number 0 and 1, sum it altogether and get the recovered number
        
        SuspectibleEvo = new_S[-1] - NewInfections #new suspectible number equals to old one minus infected number
        InfectedEvo = new_I[-1] + NewInfections - NewRecoveries #new infected number equals to old one plus infected number and plus recovered number
        RecoveredEvo = new_R[-1] + NewRecoveries #new recovered number equals to old one plus recovered number

        new_S.append(SuspectibleEvo)  #add the numbers to the list
        new_I.append(InfectedEvo)
        new_R.append(RecoveredEvo)


        #update new data
        S = new_S
        I = new_I
        R = new_R

    #draw
    plt.plot(new_I,label=f'{i*10}% Vaccinated')

   
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR Model with different vaccination rates")
plt.legend()
plt.show()
