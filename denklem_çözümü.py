#Numpy Kütüphanesi ni kullanarak Matematiksel denklem çözme işlemine örnek


import numpy as np

#matematiksel denklem örneği
"""
5 * x0 + x1 =12
x0 + 3 * x1 =10
"""
#yukarıdaki matematiksel ifadeyi numpy kütp. anlayabileceği bir dile çevirmem gerekli

a=np.array([[5,1],[1,3]])
b=np.array([12,10])
x=np.linalg.solve(a,b)

print("İki bilinmeyenli basit bir denklemin çözümü:",x)