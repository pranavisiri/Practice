import re
pattern=r'\b\d{4}-\d{2}-\d{2}\b'
string='inportant dates: 2024-06-22, 2023-01-15.'
matches=re.findall(pattern,string)
print("matches found:", matches)
