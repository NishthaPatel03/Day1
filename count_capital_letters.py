#count capital letters in a given string.

count=0

string1=input("Enter string: ")
for i in string1:
    if(i.isupper()):
        count+=1
print(count)