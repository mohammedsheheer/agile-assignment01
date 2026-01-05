def SalCalc(basicPay):
 HRA= basicPay*.2
 DA= basicPay*.1
 Tax= basicPay*.05
 netSal=basicPay+HRA+DA-Tax
 print(f"Net salary: {netSal}")

basicPay=int(input("enter the basic pay amount: "))
SalCalc(basicPay)