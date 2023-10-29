import numpy as np
import pandas as pd

s1=np.random.randint(10,size=5)
s2=np.random.randint(10,size=5)
s3=np.random.randint(10,size=5)

sozluk = {"var1":s1,"var2":s2,"var3":s3}

print(sozluk)

df= pd.DataFrame(sozluk)

print(df)

print(df[0:1]) #dataframe de istenilen kısıma kadar olan veriyi ekrana yazdırma işlemi.
print(df.index)
print(df)
df.index=["a","b","c","d","e"]
print(df)
print(df["a":"c"])
print(df["c":"e"])

#silme işlemi

print(df.drop("a"))  #geçici silme işlemi

print(df)

df.drop("a",axis=0,inplace=True) #kalıcı olarak silme işlemi

print(df)

#fancy
l=["c","e"]
print(df.drop(l,axis=0))  #fancy metodu ile istenilen kısımları silme işlemi

print("var1" in df)

l=["var1","var4","var3"] #Sutun bazında sorgulama işlemi
for i in l:
    print(i in df)


