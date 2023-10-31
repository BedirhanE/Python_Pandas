import seaborn as sns

print("-------------------------------------------")
#Veri görselleştirme yaparak veri çekmme işlemi
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Titanic veri setini yükleme işlemi yaptım
titanic_data = sns.load_dataset("titanic")

# Veri setini özetle (örneğin, yaş ortalamalarını hesaplama işlemi)
age_summary = titanic_data.groupby("class")["age"].mean().reset_index()

# Veriyi görselleştir (örnek olarak bar plot kütp. ile yaptım.)
sns.barplot(x="class", y="age", data=age_summary)
plt.title("Sınıfa Göre Ortalama Yaş")
plt.xlabel("Sınıf")
plt.ylabel("Ortalama Yaş")
plt.show()


