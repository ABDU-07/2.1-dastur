import random as r
list1=[]
for i in range(0,100):
    list1.append(r.randint(100,1000))
a = r.choice(list1)
for i in range(0,100):
    if list1[i] == a:
        exit()
    elif list1[i] % 2 == 0:
        print(list1[i],end=' ')