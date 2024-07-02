import re
pattern=r'\d+'
sentence="raju got 5 marks in phy, 7 marks in maths and 12 marks in chemistry"
marks_list=re.findall(pattern,sentence)
print(marks_list)
lst=[int(m) for m in marks_list]
print(sum(lst))








