n=int(input("enter four digit number")) #1634

a=n%10      #1634%10=4
b=n//10     #1634//10=163
c=b%10      #163%10=3
d=b//10     #163//10=16
e=d%10      #16%10=6
f=d//10     #16//10=1

s=f**4+e**4+c**4+a**4 #1**4+6**4+3**4+4**4=1634

if s==n:  
   print("it is armstrong number")
else:
   print("it is not a armstrong number")
