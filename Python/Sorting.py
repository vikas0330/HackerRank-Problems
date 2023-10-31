'''
You are given a string .
S contains alphanumeric characters only.
 Your task is to sort the string S in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string S.

Constraints
0<len(s)<1000

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
s=sorted(input())
lower=''
upper=''
odd=''
even=''
for i in s:
    if i.islower():
        lower+=i
    elif i.isupper():
        upper+=i
    elif int(i)%2 !=0:
        odd+=i
    elif int(i)%2 ==0:
        even+=i
print(lower+upper+odd+even)
        
        
        
    

