import re
# Validate email
pattern="[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
user_input = input()
if(re.search(pattern, user_input)):
    print(True)
else:
    print(False)