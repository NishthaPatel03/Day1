#Write a program which accepts marks of five subject 
# and based on average of those marks it will display appropriate grade.

s1=int(input('enter marks of maths:'))
s2=int(input('enter marks of science:'))
s3=int(input('enter marks of ss:'))
s4=int(input('enter marks of english:'))
s5=int(input('enter marks of gujarati:'))
avg=(s1+s2+s3+s4+s5)/5
grade=' '

if (avg>=90):
    grade='A'
elif (avg>=80):
    grade='B'
elif (avg>=70):
    grade='C'
elif (avg>=60):
    grade='D'
elif (avg>=50):
    grade='E'
else:
    grade='F'

print('Your grade is:',grade)

#Write a program which accepts average marks of student and if 
# average is greater than 40 then it will display a message “Congratulation!!! 
#You pass this exam successfully” else it will display “Sorry!!! Better luck next time”.

'''marks=input('Enter average marks:')
if float(marks)>40:
    print("Congratulation!!! You pass this exam successfully")
else:
    print("Sorry!!! Better luck next time")'''