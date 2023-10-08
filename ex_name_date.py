letter = '''Dear <|NAME|>,
Greetings from Indian Army, 
Congartulation, we glad to tell you have been selected in IMA, 
I hope you got a joining letter which we already sent you,
Have a good day,
Date: <|DATE|>   
'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)