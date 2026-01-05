x=int(input("Enter number of units consumed: "))
total=0
def caluclate(x):
    if(x<=100):
        total=x*2
    elif(x>100 and x<=200):
        total=100*2+(x-100)*3
    else:
        total=100*2+100*3+(x-200)*5
    return total

print(f"total bill: {caluclate(x)}")