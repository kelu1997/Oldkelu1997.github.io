import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = sns.load_dataset("titanic")
df = pd.DataFrame(df)

fig1 = sns.barplot(x=df['class'],y=df['fare'],hue=df['sex'],estimator=sum)
plt.show()

fig2 = sns.barplot(x=df['fare'],y=df['class'],hue=df['sex'],estimator=sum,orient="h")
plt.show()
