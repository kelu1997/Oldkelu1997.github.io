# Video Review Assignment
[Video Review](Journalism%20in%20the%20Age%20of%20Data%20Review.pdf)

# 2 Chart Example
'''python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = sns.load_dataset("titanic")
df = pd.DataFrame(df)

fig1 = sns.barplot(x=df['class'],y=df['fare'],hue=df['sex'],estimator=sum)
plt.show()

fig2 = sns.barplot(x=df['fare'],y=df['class'],hue=df['sex'],estimator=sum,orient="h")
plt.show()

'''
[Code](main.py)
[Figure 1](fig1.png)
[Figure 2](fig2.png)

# Interesting Images

