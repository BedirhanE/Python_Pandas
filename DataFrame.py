#DataFrame oluşturma
#Veri analizi ve veri manipülasyonları için pandas kütüphanesini kullanıyoruz.
import numpy as np
import pandas as pd

l=(1,2,39,69,78)
print("liste:",l)


#DataFrame oluşturma işlemi
data_frame=pd.DataFrame(l,columns=["değişken_isimleri"])
print(data_frame)



#3 boyutlu dataframe oluşturma işlemi
m=np.arange(1,10).reshape((3,3))#numpy daki gibi 3 boyutlu array oluşturma işlemi

data_frame_m=pd.DataFrame(m,columns=["var1","var2","var3"])
print(data_frame_m)
print(data_frame_m.head(2))#ilk 2 dataframe ekrana yazdıran kod

#DataFrame e eleman ekleme işlemleri.


