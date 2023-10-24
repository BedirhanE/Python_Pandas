#DataFrame oluşturma
#Veri analizi ve veri manipülasyonları için pandas kütüphanesini kullanıyoruz.

import pandas as pd

l=(1,2,39,69,78)
print("liste:",l)


#DataFrame oluşturma işlemi
data_frame=pd.DataFrame(l,columns=["değişken_isimleri"])
print(data_frame)