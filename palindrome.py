#check whether given string is palindrome or not.

string1=input("Enter string: ")
string1=string1.casefold()
string2=reversed(string1)
if(list(string1)==list(string2)):
    print("palindrome")
else:
    print("not palindrome")