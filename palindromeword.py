string=input('enter a word')
l=len(string)
r=''
for i in range (l,0,-1) :
    r=r+string[i-1]

if (r==string) :
    print(string,'is palindrome word')
else :
    print(string,'is not a palindrome word')

    
