#count number of each vowel in a given string
count_a=0
count_e=0
count_i=0
count_o=0
count_u=0
count=0

string1=input("Enter string:")
for i in string1:
    if (i=='a' or i=='A'):
        count_a+=1
    elif (i=='e' or i=='E'):
        count_e+=1
    elif (i=='i' or i=='I'):
        count_i+=1
    elif (i=='o' or i=='O'):
        count_o+=1
    elif (i=='u' or i=='U'):
        count_u+=1
    else:
        count+=1


print("a:",count_a,"e:",count_e,"i:",count_i,"o:",count_o,"u:",count_u)