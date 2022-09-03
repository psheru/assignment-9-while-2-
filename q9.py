#9. Write a python script to print cubes of first N natural numbers.
n=int(input('enter the value:-'))

i=1
while i<=n:
    print(i*i*i,end=',')
    i+=1
