#input the data list
#sort the data using sorted() function
#draw the two pie charts plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=False, startangle=90)

uk_countries=[57.11,3.13,1.91,5.45] 
zjneighbouring_provinces=[65.77,41.88,45.28,61.27,85.15]

print(sorted(uk_countries))
print(sorted(zjneighbouring_provinces))

import matplotlib.pyplot as plt
labels = 'England', 'Wales', 'Northern Ireland', 'Scotland'
sizes = [57.11,3.13,1.91,5.45]
explode = (0, 0, 0, 0)  #none will be emphasized in the chart
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
plt.axis ('equal')  #ensure that the bar is a circle
plt.show()

import matplotlib.pyplot as plt
labels = 'Zhejiang', 'Fujian', 'Jiangxi', 'Anhui','Jiangsu'
sizes = [65.77,41.88,45.28,61.27,85.15]
explode = (0, 0, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
plt.axis ('equal')
plt.show()