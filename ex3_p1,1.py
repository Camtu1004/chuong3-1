a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
a,b,c>0
p=(a+b+c)/2
import math
if a+b>c :
    if a+c>b:
        if b+c>a:
            print('Dien tich=', round (math.sqrt(p*(p-a)*(p-b)*(p-c)),3),sep="")
else:
    print("Khong hop le")
