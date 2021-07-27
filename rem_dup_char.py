import re
import random

all_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

word = ''.join(random.choices(all_chars,k=10))
found = False
print("The string is {}".format(word))
for i,char in enumerate(word):
    if re.search(char,word[:i]+word[i+1:]):
        found = True
        break
if found:
    print("String has repeated characters")
else:
    print("String has unique characters")
