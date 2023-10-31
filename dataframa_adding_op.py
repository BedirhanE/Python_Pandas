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
#Gözlem ve değişken Seçimi
import numpy as np
import  pandas as pd

m=np.random.randint(1,30, size=(10,3))
df=pd.DataFrame(m,columns=["var1","var2","var3"])
print(df)

#Loc tanımlandığı şekli ile seçim yapmak için kullanılır.(verilen indexs lere bağlı kalarak)
print(df.loc[0:3])

#iloc:alışık olduğumuz indeksleme mantığı ile seçim yapar
print(df.iloc[0:3])
print(df.iloc[0,0])
print(df.iloc[0:3]["var3"])
print(df["var3"])

print(df[df.var1>15])#data frame üzerinde koşul çalıştırma işlemi
print("***********************************")
print(df[(df.var1>10)&(df.var1<20)])#eğer Birden fazla koşul kullanıcaksak
print("***********************************")
print(df[(df.var1>10)&(df.var2<20)])
#DataFrame Birleştirme işlemleri


m=np.random.randint(1,30, size=(5,3))
df1=pd.DataFrame(m,columns=["var1","var2","var3"])
print("DataFrame 1:",df1)

df2=df1+50
print("dataframe 2:",df2)

#DataFrame leri birleştirme işlemi
print("DataFrame1 ve DataFrame2 nin birleştirilmiş hali:",pd.concat([df1,df2]))

#İndex sıralarının doğru şekilde yazılmış hali
print("DataFrame1 ve DataFrame2 nin birleştirilmiş hali:",pd.concat([df1,df2],ignore_index=True))
