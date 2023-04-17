b=int(input('M1='))
c=int(input('M2='))
d=int(input('M3='))
a=int(input('S='))
if a<=100:
    print("Phai tra=",a*b,sep="")
elif 101<=a<=150:
    print("Phai tra=",(100*b)+(a-100)*c,sep="")
elif a>=151:
    print("Phai tra=",(100*b)+(50*c)+(a-150)*d,sep="")
 
