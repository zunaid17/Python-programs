'''
A number is entered by user. WAP to check wether number is even or odd number.

evev: the number which is completely divisible by 2.
      since it is completely division its remainder of the division is zero.
      opertor: %

step1:start
step2:message to user => print()
step3:store that input in variable => input()
step4:calculate remainder
step5:if remainder is equal to 0 then it is even
step6:if remainder is not equal to 0 then it is odd.
step7:stop
'''

print(" enter number:")
n=int(input())  #n=16, n=25
r=n%2  #r=16%2=0, r=25%2=1

if r==0:  #0==0 -> true so execute if block, #1==0 -> flase so execute else block
   print("even number")

else:
  print("odd number")
