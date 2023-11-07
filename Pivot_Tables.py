import  pandas as pd
import seaborn as sns
titanic=sns.load_dataset("titanic")
titanic.head()
print(titanic.head())
#sıralama işlemi
#print(titanic.groupby("sex")["survived"].mean())
#pivot table oluşturma
#print(titanic.groupby(["sex","class"])[["survived"]].agreegate("mean").unstack())

#print(titanic.pivot_table("survived",index="sex",columns="class"))
#print(titanic.age.head())

print(titanic.pivot_table("survived",["sex","age"],"class"))