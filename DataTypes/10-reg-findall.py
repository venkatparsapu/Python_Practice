import re
text="the quick brown fox"
pattern=r"brown"
search=re.search(pattern,text)
if search:
    print("pattern fond",search.group())
else:
    print("pattern not fond")    