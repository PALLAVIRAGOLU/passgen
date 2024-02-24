import random
import string
pass_len = int(input("Enter the password length: "))
char = string.ascii_letters
char += string.digits
char += string.punctuation
password = "".join([random.choice(char) for _ in range(pass_len)])
print(password)
