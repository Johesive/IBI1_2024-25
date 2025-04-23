#input the data as a list
#import matplot and NumPy
#save the names of languages to the variable "languages"
#save the percentage of users to the variable "counts"
#draw the bar chart plt.bar(ind, counts, width, yerr=Std)
data = {'JavaScript':62.3,'HTML':52.9,'Python':51,'SQL':51,'TypeScript':38.5}

#draw the bar chart
import matplotlib.pyplot as plt 
import numpy as np
N = 5  #the number of languages
languages = list(data.keys())
counts = list(data.values())
Std = (0, 0, 0, 0, 0)  #the range of error of each language equals to 0 
ind = np.arange(N)  #Generate position array [0, 1, 2, 3, 4]
width = 0.35  #Width of each bar
p1 = plt.bar(ind, counts, width, yerr=Std)
plt.ylabel('percentage')  #Set y-axis label
plt.title('the percentage of developers who use the following languages')
plt.xticks(ind, ('JavaScript', 'HTML', 'Python', 'SQL','TypeScript')) 
plt.yticks(np.arange(0, 110, 10))
plt.show()

#print the percentage of JavaScript users
print(data['JavaScript'])  