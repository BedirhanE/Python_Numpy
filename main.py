#Matematiksel işlemlr için kullanılan numpy kütüphanesi

import numpy as np

#numpy kütüphanesi içerisinden np. ile numpay array oluşturma işlemi
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])

#oluşturmuş olduğum 2 farklı numpy arrayleri çarpma işlemi
print(a*b)

#istenilen aralıklara kadar başlangıç,bitiş ve artış miktarına göre tek boyutlu array oluşturma işlemi
print(np.arange(0,30,2))

print(np.linspace(0,1,10))

print(np.random.normal(3,12,5))

print(np.random.randint(0,10,(3,5)))

rast_gele=np.random.randint(0,10,size=10)
print("0  dan 10 a kadar rastgele array oluşturma:",rast_gele)
print("arrayın size boyutu:",len(rast_gele))


#2 boyutlu array i 3 boyutlu hale dönüştürmek reshape(yedniden şekillendirem işlemi)

print(np.arange(1,10))

print(np.arange(1,10).reshape((3,3)))

#array birleştirme işlemleri
x=np.array([1,2,3])
y=np.array([4,5,6])

print("iki array birleşimi:",np.concatenate([x,y]))

z=np.array(["p","r","s"])
print("üç farklı array birleşimi:",np.concatenate([x,y,z]))

#array ayırma işlemleri

x=np.array([1,2,3,4,78,89,45,56])

#numpy da split fonk. kullanarak tek bir arrayı 3 farklı arraya ayırma işlemi
print(np.split(x,[4,6]))


a,b,c= np.split(x,[4,6])
print("array a:",a)
print("array b:",b)
print("array c:",c)


print(np.random.randint(0,100,size=10))

#********************************************************