#RE

import re
pattern=r'(\d+)-(\d+)-(\d+)'
string='My phone number is 123-456-7890.'
match=re.search(pattern,string)
if match:
    print("Full match:",match.group())
    print("Group 1:", match group(1))
    print("Group 2:", match group(2))
    print("Group 3:", match group(3))
else:
    print("No Match")
