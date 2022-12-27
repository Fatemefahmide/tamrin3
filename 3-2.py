a = int(input("rows: "))
b = int(input("cols: "))

array=[]
array=[["*" for i in range(b)]for j in range(a)]

for j in range(a):
       print(array[j])


