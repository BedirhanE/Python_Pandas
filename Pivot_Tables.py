import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Titanic veri setini yükleme adımı
titanic = sns.load_dataset("titanic")

# Veri setinin ilk 5 satırını görüntülemek için gerekli kod
print(titanic.head())

# Yaşa göre hayatta kalma oranlarını hesaplama işlemi
age_survival = titanic.groupby("age")["survived"].mean()
print("Yaşa göre hayatta kalma:",age_survival)

# Bu verileri bir çizgi grafiği ile görselleştirin
plt.figure(figsize=(12, 6))
age_survival.plot()
plt.title("Yaşa Göre Hayatta Kalma Oranları")
plt.xlabel("Yaş")
plt.ylabel("Hayatta Kalma Oranı")
plt.grid(True)
plt.show()

# Yolcu sınıfına göre yaş ve cinsiyete bağlı hayatta kalma oranlarını hesaplayın
age_class_sex_survival = titanic.pivot_table("survived", index=["sex", "age"], columns="class")

# Bu verileri bir ısı haritası ile görselleştirin
plt.figure(figsize=(10, 6))
sns.heatmap(age_class_sex_survival, annot=True, cmap="coolwarm")
plt.title("Yolcu Sınıfına ve Yaşa Göre Hayatta Kalma Oranları")
plt.show()

# Cinsiyete göre yolcu sayısını hesaplama
gender_counts = titanic["sex"].value_counts()

# Bu verileri bir çubuk grafiği ile görselleştirme işlemi
plt.figure(figsize=(8, 5))
sns.barplot(x=gender_counts.index, y=gender_counts.values)
plt.title("Cinsiyete Göre Yolcu Sayısı")
plt.xlabel("Cinsiyet")
plt.ylabel("Yolcu Sayısı")
plt.show()
