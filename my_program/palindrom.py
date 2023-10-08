# Check (s) value whether is palindrome or not 
def isPalindrome(s):
       return s == s[::-1]
   
s = "123"
ans = isPalindrome(s)
if ans:
       print("Yes")
else:
       print("No")   

# convert decimal number into binary number
x = int(input("Enter your number: "))
y = int(bin(x)[2:])
print("Your binary number is: ", y)

# Whether the binary equvalent of given number i 
x = int(input("Enter your number: "))
y = int(bin(x)[2:])
out = str(y)[::2]
print("Your binary number is: ", y)
if int(out)==y:
       print("this binary number is palindrome.")
else:
       print("this binary number is not palindrome.")       