import numpy as np
import matplotlib.pyplot as plt

population = np.zeros((100, 100))  #randomly choose the first infected person
outbreak = np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]] = 1

beta = 0.3
gamma = 0.05

S = [100*100-1]  #create the list
I = [1]
R = [0]

for t in range(0,101):  #step 1 to step 100
    new_population = population.copy() #avoid overwriting
    
    # find infected points
    infectedIndex = np.where(new_population==1)

    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]

        # infect each neighbour with probability beta
        # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # don't infect yourself! (Is this strictly necessary?)
                if (xNeighbour,yNeighbour) != (x,y):
                    # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected!
                        if new_population[xNeighbour,yNeighbour]==0:
                            new_population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    

    #do recovery. This step should be no chronological order with infection, so two for loop is needed.
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]

        if new_population[x,y]==1:  #probability to be 2 equals to gamma
            new_population[x,y]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])[0]    
        

    population = new_population  #update
        
    new_S = np.sum(population == 0)
    new_I = np.sum(population == 1)
    new_R = np.sum(population == 2)
    S.append(new_S)        
    I.append(new_I)
    R.append(new_R)
        
    if t == 0 or t == 25 or t == 50 or t == 100: #plot when time step equals to 0, 25, 50, 100
        plt.figure(figsize=(6,4), dpi =150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time Step {t}')
        plt.show()


plt.figure(figsize=(10, 6))
plt.plot(S, label='Susceptible')
plt.plot(I, label='Infected')
plt.plot(R, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Count')
plt.title('Spatial SIR Model Dynamics')
plt.legend()
plt.show()