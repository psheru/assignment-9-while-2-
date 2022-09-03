#4. Write a python script to print first N odd natural numbers.

n=int(input('enter the value up to you want to print odd natural number:-'))
i=1
while i<2*n:
    print(i,end=',')
    i+=2
