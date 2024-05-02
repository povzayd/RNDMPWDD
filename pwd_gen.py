import random
import string
pass_leng=10
char_val=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(pass_leng):
  password+=random.choice(char_val)
print("YOUR RANDOM PASSWORD IS :",password)
