'''
need of conditional statment
=============================
during code when there is need to take decision based on certain condition, then there is need of conditional statment.

what is conditional statment?
============================
The stament or instruction which helps to give decision based on certain condition in a progam are called as
conditional statment or conditional instructions or decision control instruction.

Types of conditional statment
==============================
1.if statment
2. if else statment
3. nested if else
4. logical operators
5. elif

if statment
============
syntax:
 
if condition:
 
    code in if block

working
========
if the condition is true then its execute if block or program control enter in if block
and execute code inside if block.

if condition is flase then it wont execute if block.
'''
'''
if..else
========

syntax:

if condition:
 
  code in if block
else:

  code in else block

working:
========
if the condition is true then its execute if block or program control enter in if block
and execute code inside if block.

if condition is flase then it execute else block.
'''

#Two number entered by user. WAP to find greatest of two numbers

priny("enter a number")
#x=input()
#a=int()
a=int(input())  #a=45
print("enter a numbrt:")
b=int(input())  #b=30

if a>b:   #45>30 = true, 10>30= flase then else block will work
  print("In if block")
  print("greater is:",a)

else:
  print("In else block")
  print("greater is:",b)

