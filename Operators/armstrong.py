'''
A three digit number is entered by user. WAP to find whether number is armstrong number.

n=153 is armstrong

sum of cubof digit= original number

1**3+5**3+3***3=1+125+27=153

step1: start
step2: digit separation => %,// 10
step3: cube and add or summation.
step4: check summation is equal to number entered by user.
step5: if it found same then it is armstrong number.
step6: otherwise it is not an armstrong number
step7: stop
'''

print("enter three digit")
n=int(input()) #n=153, 231
#digit separation
a=n%10 #a=153%10=3, 231%10=1
b=n//10 #b=153//10=15  231//10=23
c=b%10 #c=15%10=5   23%10=3
d=b//10 #c=15//10=1 23%10=2

s=a**3+c**3+d**3 #cube and summation  , 1+27+8=36

#checking

if s==n:  #153==153 T, 36==231 F
   print("it is armstrong number")
else:
   print("it is not a armstrong number")
