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
print(m)
