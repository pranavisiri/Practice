import re
pattern=r'^Hello'
pattern=r'^world'
string='Hello world!'
match=re.match(pattern,string)
if match:
    print("Match found:", match.group())
else:
    print("No match")
