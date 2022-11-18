from numpy import *
sturoll=array([10,20,20,20,20])
print(sturoll)
print(sturoll.dtype)

print()
sk=array(['bhai-','shokin','punam','devendra','rahul'])
print(sk)
print(sk.dtype)

#for loop in  numpy
for i in sk:
    print(i)

print()

for i in range(len(sk)):
    print(sk[i])
i=0
print('----------------------------------while loop--------------------------------')
#while loop in numpy
while i<len(sk):
    print(sk[i])
    i+=1
