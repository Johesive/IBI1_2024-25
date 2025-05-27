#same as SIR.py, but with vaccinated people
#need to print 11 different plots, each with different vaccinated number: for loop + plt.plot label=f'{i*10}% Vaccinated'
#create three lists to store the numbers of susceptible, infected, and recovered people at each time step
#use [-1] to get the current number of people in each state


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

for i in range (0,11): #10*i% is the rate of vaccination
    
    #There is a question. 
    #If vaccinated number is 100%, in the context there will be no infected people at first, which is contradictory to the assumption that one person is affected. 
    #As a result, I choose to set suscepitble number as 0 in this situation.
    
    N = 10000
    Vaccinated = 1000*i
    Susceptible = max(N-Vaccinated-1,0) #set susceptible number as 0 if vaccinated number is 100%
    Infected = 1
    Recovered = 0
    label = 10*i

    beta = 0.3
    gamma = 0.05

    S = [Susceptible]  #create the lists
    I = [Infected]
    R = [Recovered]

    for _ in range(1000):  #do the operation for 1000 times
        current_S = S[-1]  #get the current numbers
        current_I = I[-1]
        current_R = R[-1]
        
        probability_of_infection = beta*current_I/ N  #calculate probability of infection, while probability of recovery equals to gamma

        NewInfections = np.random.choice(range(2),current_S,p=[1-probability_of_infection,probability_of_infection]).sum()
        #randomize the infected number
        NewRecoveries = np.random.choice(range(2),current_I,p=[1-gamma,gamma]).sum()
        #randomize the recovered number
        
        SusceptibleEvo = current_S - NewInfections #new suspectible number
        InfectedEvo = current_I + NewInfections - NewRecoveries #new infected number
        RecoveredEvo = current_R + NewRecoveries #new recovered number

        S.append(SusceptibleEvo)  #add the numbers to the list
        I.append(InfectedEvo)
        R.append(RecoveredEvo)
    #draw
    plt.plot(I,label=f'{i*10}% Vaccinated', color=cm.viridis(i/10))  #use viridis colormap to differentiate the lines

   
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR Model with different vaccination rates")
plt.legend()
plt.show()
