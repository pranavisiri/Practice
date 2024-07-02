#Regular Expression

import re
pattern=r'^Hello'
string='Hello world!'
match=re.search(pattern,string)
print(match)
if match:
    print("Match found:", match.group())
else:
    print("No match")
