num=int(input('enter a  integer'))
check=num
rem=0
rev=0
while(num>0) :
    rem=num%10
    rev=rev*10+rem
    num=num//10

if (rev==check) :
    print(check,'is palindrome number')
else :
    print(check,'is not palindrome')
    

