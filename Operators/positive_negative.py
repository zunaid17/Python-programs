'''
A number is entered by user, check wether number is positive number or negative number or not.


                 -----------------------------------------------
                    -3   -2    -1   0  1   2   3  4
                    negative < 0 > positive

positive: number must be greater than zero
negative: number must be less than zero
'''
print("enter a number:")
n=int(input()) #n=15, n=-7

if n>0:  #15>0 -> true, -7>0 -> flase
   print("the number is positive:")

else:
   print("the number is negative:")
