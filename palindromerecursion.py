def palindrome(x) :
     global rev=0
    while (x>0) :
        rem = x%10
        rev = (rev*10) + rem
       
    palindrome(x//10)
    return  rev

num=int(input('enter a integer'))
check=palindrome(num)
if (check==num) :
        print(num,'is palindrome')
else :
        print(num,'is not palindrome')
