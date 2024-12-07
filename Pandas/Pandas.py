import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#How to read a .csv
df1 = pd.read_csv("Foldername/Filename")
#How to select a column and a cell in that column
x = df1.iloc[0]["Column"]
#How to sort based on a column
df2 = df1.sort_values(
        by="column",
        ascending=False)
#Select rows that include x in a column
xlist = ['x1','x2']
df1.loc[df1['Column'].isin(xlist)]
#How to make a bar graph
datay = [1,2,3,4,5,6]
datax = [1,2,3,4,5,6]
y = np.array(datay)
x = np.array(datax)
plt.bar(x,y)
plt.show()