#create three lists S, I and R to store the number of people in each state at each time step
#for loop: 1000 times
#probability of infection: beta*I[-1]/N
#probability of recovery: gamma
#randomize: all people who is in the suspectible group is randomly given the number 0 and 1, sum it altogether and get the infected number
#randomize: all people who is in the infected group is randomly given the number 0 and 1, sum it altogether and get the recovered number
#new suspectible number equals to old one minus infected number
#new infected number equals to old one plus infected number and plus recovered number
#new recovered number equals to old one plus recovered number
#add the numbers to the list: append
#draw the graph: plot


import numpy as np
import matplotlib.pyplot as plt

N = 10000
Suspectible = N-1
Infected = 1
Recovered = 0

beta = 0.3
gamma = 0.05

S = [Suspectible]  #create the lists
I = [Infected]
R = [Recovered]

for _ in range(1000):  #do the operation for 1000 times
    probability_of_infection = beta*I[-1]/N  #probability of infection

    NewInfections = np.random.choice(range(2),S[-1],p=[1-probability_of_infection,probability_of_infection]).sum()
#randomize the infected number
    NewRecoveries = np.random.choice(range(2),I[-1],p=[1-gamma,gamma]).sum()
#randomize the recovered number
    
    SuspectibleEvo = S[-1] - NewInfections #new suspectible number
    InfectedEvo = I[-1] + NewInfections - NewRecoveries #new infected number
    RecoveredEvo = R[-1] + NewRecoveries #new recovered number

    S.append(SuspectibleEvo)  #add the numbers to the list
    I.append(InfectedEvo)
    R.append(RecoveredEvo)


plt.plot(S, label="susceptible", color="blue")  #draw
plt.plot(I, label="infected", color="orange")
plt.plot(R, label="recovered", color="green")
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR Model")
plt.legend()
plt.show()