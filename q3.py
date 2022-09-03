#3. Write a python script to print first N natural numbers in reverse order.
n=int(input('enter the value up to you want to print:-'))
i=n
while i>0:
    print(i,end=',')
    i-=1
