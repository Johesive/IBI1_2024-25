import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir(r"C:\Users\15041\IBI1_2024-25\Practical10")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

dalys_data.iloc[0:10,2] #the 10th year with DALYs data recorded in Afghanistan is 1999

year_column = dalys_data.iloc[:,2]


dalys_1990 = dalys_data.loc[dalys_data.Year == 1990, "DALYs"] #Boolean: dalys_data.Year == 1990
print(dalys_1990)


uk_dalys = dalys_data.loc[dalys_data.Entity=="United Kingdom", "DALYs"]
fr_dalys = dalys_data.loc[dalys_data.Entity=="France", "DALYs"]
uk_mean = uk_dalys.mean() #compute the mean of DALYs in 1990
fr_mean = fr_dalys.mean()

if uk_mean > fr_mean:
    print(f"the mean of United Kingdom", (uk_mean), "is greater than France", (fr_mean), "in 1990")
else:
    print(f"the mean of France", (fr_mean), "is greater than United Kingdom", (uk_mean), "in 1990") 

#the mean DALYs in the United Kingdom is greater than France (23319.016333333333 > 21474.627000000004)

uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
fr = dalys_data.loc[dalys_data.Entity=="France", ["DALYs", "Year"]]
plt.plot(uk.Year, uk.DALYs, 'bo')
plt.xticks(uk.Year,rotation=-90)
plt.show() #a plot of DALYs over time in the UK


#use Boolean dalys_data.Year == 1990 to select the data for 1990
#use plt.boxplot to draw a boxplot
dalys_1990 = dalys_data.loc[dalys_data.Year == 1990, "DALYs"]
plt.boxplot(dalys_1990.values)
plt.title("Boxplot of DALYs Across Countries in 1990")
plt.ylabel("DALYs")
plt.show()
