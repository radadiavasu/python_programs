# 'r' Read the file only
my_file = open('data.txt', 'r')
file_content = my_file.read()

my_file.close()

print(file_content)

# 'w' Write the file only and you can see into your .txt file yopur name has been changed
user_name = input('Enter Your Name: ')
my_file_writing = open('data.txt', 'w')
my_file_writing.write(user_name)

my_file_writing.close()