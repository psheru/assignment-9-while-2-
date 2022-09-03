#7. Write a python script to print first N even natural numbers in reverse order.

n=int(input('enter the value up to you want to print even natural number reverse:-'))
i=(2*n)
while i>=2:
    print(i,end=',')
    i-=2
