'''
A three digit number is entered through keyboard. write a program to
a. reverse that digit.
b. sum of digits.

a) input n=675 ------> logic ------> output 576

b) input n=675 ------> logic -------> output 6+7+5=18

 revers of digit of number is basic math format is 675= 6*100+7*10+5*1

5*100+ 7*10+ 6*1=576

sum=6+7+5
digit seperation => % and // with divisor 10

'''

n=675
a=n%10     #a=5
b=n//10    #b=67
c=b%10     #c=67%10=7
d=c//10    #d=6

rev=a*100+c*10+d*1  #rev=5*100+7*10+6*1=576
print("original number:",n)
print("revers number:",rev)

s=a+c+d #s=5+7+6=18
print("summation of digits:",s)


================================================================
Take input from user for above program

print("enter three digit number:")
x=input()   #ex if user give 642
n=int(x)    #covert string to integer
a=n%10     #a=6
b=n//10    #b=42
c=b%10     #c=42%10=4
d=c//10    #d=2

rev=a*100+c*10+d*1  #rev=2*100+4*10+6*1=246
print("original number:",n)
print("revers number:",rev)

s=a+c+d #s=6+4+2=12
print("summation of digits:",s)


#home work try with 4 digit or 5 digit for above program.
