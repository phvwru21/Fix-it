import numpy as np
x= np.array ([1,2,3])
a= np.array([[1,2,3],[4,5,6]])
print (x,a)
print(np.shape(a))

print(np.sum(x),np.mean(x))
print(np.sum(a, axis=0),np.mean(a, axis=0))
print(np.sum(a, axis=1),np.mean(a, axis=1))

#Exercise 1 Task 2
y=np.array(np.arange(0, 12, 2)) # array 0 to 10
print(y)
print(np.sum(y),np.mean(y),np.min(y), np.max(y), np.shape(y))#solving 

#Task 3

z=np.array([np.arange(1, 4),np.arange(4,7),np.arange(7,10)]) # matrix 1 to 9 3x3
print(z)
print(np.sum(z),np.mean(z), np.shape(z), np.transpose(z))#solving 
print(np.sum(z, axis=0),np.mean(z, axis=0))
print(np.sum(z, axis=1),np.mean(z, axis=1))

#Task 4
w=np.array(np.arange(1, 4))
v=np.array(np.arange(4, 7))
print(w*v, np.dot(w,v))

#task 5
b=np.array([np.arange(1, 3), np.arange(3, 5)])
c=np.array([np.arange(3, 5), np.arange(1, 3)])
print(b@c)

