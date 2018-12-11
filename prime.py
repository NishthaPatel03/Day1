#Write a program to check whether entered number is prime or not.
n=int(input('Enter number to check if it is prime or not:'))
flag=0

for i in range(2,int(n/2)):
    if(n%i==0):
        flag=1  
        break
if (n==1):
    print("neither prime nor composite:")
else:
    if (flag==0):
        print(n,'is a prime number')
    else:
        print(n,'is not a prime number')