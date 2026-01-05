n=int(input("enter no of tuples: "))
a=[]
for i in range (0,n):
    name,age,score=input().split(',')
    a.append(((name, int(age), int(score))))

a.sort(key= lambda x: (x[0],x[1],x[2]))
print(a)

    
