import numpy as np

array=np.arange(100)

print(array)


numpy_array=array.reshape(10,10)

print("Matris hali: ",numpy_array)

sırasız=[4,8,7,3,1,0,45,12,73]

sıralı=np.sort(sırasız)

print("Arrayın sıralamadan önceki hali:",sırasız)
print("Arrayın sıralama yapıldıktan sonraki hali:",sıralı)


#İki Boyutlu array sıralama

m=np.random.normal(20,5,(3,3))
print("3 boyutlu matrix in sırasız hali",m)

sıralı_m=np.sort(m)
print("3 boyutlu bir matrix in sıralı hali:",sıralı_m)


#slicing ile elemanlara erişmek
a=np.arange(20,30)

print(a)
print("0 indexinden 3. indexe kadar olan veriler: ",a[0:3])
print("başlangıç:Bitiş:artış miktarı na göre çekilen veriler:",a[0:8:2])  #0 dan 8 e kadar olan verileri 2 şer 2 şer olarak yazdıran kod.

#Koşullu eleman işlem
v=np.array([1,2,3,4,5])
print(v<3)

print(v[v<3])
print(v[v>3])
print(v[v!=3])
print(v[v==3])


#Matematiksel işlemler
print("v deki bütün elemanlardan 1 çıkarma :",np.subtract(v,1))

print("her bir elemana 5 ekleme işlemi:",np.add(v,5))

print("her bir elemanı 3 ile çarpma işlemi",np.multiply(v,3))

print("her bir elemanı 5 e bölme işlemi:",np.divide(v,5))

print("üslü değerini alma işlemi:",np.power(v,8))

print("modunu alma işlemi:",np.mod(v,2))

print("Mutlak değerini alma işlemi:",np.absolute(np.array([-3,5,-4-9])))

print("trigonometrik fonk kullanma işlemi sin360 değeri: :",np.sin(360))

print("v arrayı içerisindeki değerlerin log2 ye alınması işlemi:",np.log2(v))

#Kullanmış olduğum Kütüphanenin düzenli olarak notlarına nasıl erişebilirim???
#CHEATSHEET yapma işlemi ile
#örn: numpcheatsheet ile google da aratma yaparak numpy kütüphanesinin notlarına  detaylı olarak ulaşabilirim
