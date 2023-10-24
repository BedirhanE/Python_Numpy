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

#