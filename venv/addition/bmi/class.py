a=0
for i in range(4):
    for i in range (i+1):
        print(a,end='  ')

    print()
    a+=1

##################################
for i in range(5,0,-1):
    for k in range(i):
        print('*',end='  ')
    print()

#the python code below calculates the multiplication of 3 upto 10. Rewrite the code using for.

num=3
for i in range(1,11):
    multiplication=num*i
    print(num,'*', i ,'=', multiplication )

#What will be the output of following program? Rewrite the code using while loop to display same output.
i=0
while i<=5 :
    if i==3:
        break
    print(i)
    i=i+1

#What will be the output of following program? Rewrite the code using for loop to display same output.

for i in range(5):
    i +=1
    print(i)