#!/usr/bin/env python
# coding: utf-8

# In[38]:


#import data and run a for loop to display all possible combination of features comparison 
import pandas as pd
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

df = pd.read_csv(filepath_or_buffer='~/Desktop/boston/housing.csv',sep='\s+',header=None)
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
#print(df.to_string())

os.makedirs('plots/7-matplotlib_dataset_exploration', exist_ok=True)

for col1_idx, column1 in enumerate(df.columns):
    for col2_idx, column2 in enumerate(df.columns):
        if col1_idx < col2_idx:
            fig, axes = plt.subplots(1, 1, figsize=(5, 5))
            axes.scatter(df[column1], df[column2], label=f'{column1} to {column2}', s=df[column3]*0.05,color='green', marker='x')
            axes.set_title(f'{column1} to {column2} to {column3}')
            axes.set_xlabel(column1)
            axes.set_ylabel(column2)
            axes.legend()
            plt.savefig(f'plots/7-matplotlib_dataset_exploration/housing_{column1}_{column2}_{column3}_scatter.png',dpi=300)
            plt.close(fig)
            

plt.close()


# In[ ]:





# In[ ]:





# In[53]:


#3D plot
os.makedirs('3Dplots/7-matplotlib_dataset', exist_ok=True)

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x=df['NOX']
y=df['DIS']
z=df['TAX']

ax.scatter(x,y,z, c='r',marker='x')
ax.set_xlabel('NOX')
ax.set_ylabel('DIS')
ax.set_zlabel('TAX')
plt.savefig(f'3Dplots/7-matplotlib_multiple_plot1.png', dpi=300)
#plt.show()
plt.close()

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x=df['LSTAT']
y=df['MEDV']
z=df['TAX']

ax.scatter(x,y,z, c='r',marker='x')
ax.set_xlabel('LSTAT')
ax.set_ylabel('MEDV')
ax.set_zlabel('TAX')
plt.savefig(f'3Dplots/7-matplotlib_multiple_plot2.png', dpi=300)
#plt.show()
plt.close()


# In[50]:


#NOX.DIS.TAX , LSTAT.MEDV.TAX Two most important graphs
import matplotlib.pyplot as plt
plt.style.use("ggplot")

os.makedirs('plots2/7-matplotlib_dataset', exist_ok=True)
fig, axes = plt.subplots(2, 1, figsize=(5, 5))
#axes.grid(axis='y', alpha=0.5)
axes[0].scatter(df['NOX'], df['DIS'],s=df['TAX']*0.05,color='green', marker='x')
axes[0].set_xlabel('NOX')
axes[0].set_ylabel('DIS')

axes[1].scatter(df['LSTAT'], df['MEDV'],s=df['TAX']*0.05,color='green', marker='o')
axes[1].set_xlabel('LSTAT')
axes[1].set_ylabel('MEDV')
#axes.scatter(df['alcohol'], df['class'])
axes[0].set_title(f'Crucial Factor1')
axes[1].set_title(f'Crucial Factor2')
plt.tight_layout()
#axes.legend()
plt.savefig(f'plots2/7-matplotlib_multiple_plot.png', dpi=300)



plt.close()

          


# In[ ]:




