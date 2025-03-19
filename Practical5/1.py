#input the data
data = {'JavaScript':62.3,'HTML':52.9,'Python':51,'SQL':51,'TypeScript':38.5}

#draw the bar chart
import matplotlib.pyplot as plt   #import matplot and NumPy
import numpy as np
N = 5  #the number of languages
languages = ['JavaScript', 'HTML', 'Python', 'SQL','TypeScript']  #the names of languages
counts = [62.3, 52.9, 51, 51, 38.5]  #the percentage of users
Std = (0, 0, 0, 0, 0)  #the range of error of each language equals to 0 
ind = np.arange(N)  #Generate position array [0, 1, 2, 3, 4]
width = 0.35  #Width of each bar
p1 = plt.bar(ind, counts, width, yerr=Std)
plt.ylabel('percentage')  #Set y-axis label
plt.title('the percentage of developers who use the following languages')  #Set title
plt.xticks(ind, ('JavaScript', 'HTML', 'Python', 'SQL','TypeScript'))  #Label x-axis as language names
plt.yticks(np.arange(0, 110, 10))  #Set y-axis range
plt.show()

#print the percentage of JavaScript users
print(data['JavaScript'])  