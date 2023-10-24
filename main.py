
#Pandas Kütüphanesi kullanımı ve örnekler.yapay zeka da da kullanılıyor bu kütüphane


import pandas as pd #pandas importlama işlemi

seri=pd.Series([10,88,3,4,5])#pandas da seri oluşturma

print(seri)
print(type(seri))
print(seri.axes)
print("veri tipi:",seri.dtype)
print("Boyutu:",seri.size)
print(seri.ndim)
print("Değerler:",seri.values)
print("seri nin ilk 3 argumanını getirme:  ", seri.head(3))
print("Sondan bakma işlemi:",seri.tail(2))


#####################################################################
#pandas da seri oluşturmak istersek index atama işlemlerini de kendimiz yapabiliriz.
seri1=pd.Series([10,11,12,13,14,15],index=["a","b","c","d","e","f"])
print(seri1)


#Sözlük üzerinden Liste oluşturma işlemleri

sozluk=pd.Series({"reg":10,"log":11,"cart":12})
print(sozluk)

#eleman işlemleri

seri=pd.Series([100,200,300,400],index=["x","y","z","t"])#seri oluşt. indexleme işlemi yaptım.
print(seri)
print(seri.dtype)

print(list(seri.item()))

#eleman sorgulama işlemi

print("100" in seri)