#Regular Expression
import re
pattern=r'\d+'
sentence="raju got 5 marks in phy, 7 marks in maths and 12 marks in chemistry"
marks_list=re.findall(pattern,sentence)
print(marks_list)
lst=[int(m) for m in marks_list]
print(sum(lst))

#RE
import re
pattern=r'^Hello'
string='Hello world!'
match=re.match(pattern,string)
if match:
    print("Match found:", match.group())
else:
    print("No match")


#RE
import re
pattern=r'(\d+)-(\d+)-(\d+)'
string='My phone number is 123-456-7890.'
match=re.search(pattern,string)
if match:
    print("Full match:",match.group())
    print("Group 1:", match.group(1))
    print("Group 2:", match.group(2))
    print("Group 3:", match.group(3))
else:
    print("No Match")

    
#RE
import re
pattern=r'^Hello'
string='Hello world!'
match=re.search(pattern,string)
print(match)
if match:
    print("Match found:", match.group())
else:
    print("No match")

import re
pattern=r'\b\d{4}-\d{2}-\d{2}\b'
string='inportant dates: 2024-06-22, 2023-01-15.'
matches=re.findall(pattern,string)
print("matches found:", matches)


import re
pattern=r'colou?r' #u is optional
strings=['color','colouring','colr']
matches=[re.match(pattern,string) for string in strings]
for match in matches:
    if match:
        print(f"matched: {match.group()}")
    else:
        print("No match")

import re
text="The cat catalog contains many cat"
pattern=r'\bcat\b'
replacement="dog"
result=re.sub(pattern,replacement,text)
print(result)


'''
Common Greedy quantifiers include:
*: matches 0 or more occurences of the preceding element
+: matches 1 or more occurences of the preceding element
?: matches 0 or 1 occurence of the preceding element
{n}: matches exactly n occurences of the preceding elemnet
{n,1}: matches n or more occurences of the preceding element
{n,m}: matches between n and m occurences of the preceding element


Non-Greedy quatifiers include:

*?: matches 0 or more occurences of the preceding element
+?:
??:
{n?}:
{n,
{n,m
'''


import re
string='<div>content</div>'
pattern=r'<.*?>' #non-greedy approach
#pattern=r'<.*>' #greedy approach
match=re.search(pattern, string)
print("match:",match.group())














        
