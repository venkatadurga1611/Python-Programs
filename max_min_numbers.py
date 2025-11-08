import numpy as np
a = np.array([22,54,12,43,21,9])
num = 20
les = a[a < num]
gre = a[a > num]
print("Less : ",les)
print("gre : ",gre)
matrix = np.array([[10,24,21], [23,12,43],  [67,89,90]])
print("Max : ",np.max(matrix))
print("Min : ",np.min(matrix))
print("Index min : ",np.argmin(matrix))
print("Index max : ",np.argmax(matrix))
print("Index min along axis 0 : ",np.argmin(matrix,axis = 0))
print("Index max along axis 0 : ",np.argmax(matrix,axis = 0))
print("Index min along 1 : ",np.argmin(matrix,axis = 1))
print("Index max along 1 : ",np.argmax(matrix,axis = 1))
print("represen : ",repr(a))
print("unique : ",np.unique(matrix))
print("Bin count : ",np.bincount(a // 5))
