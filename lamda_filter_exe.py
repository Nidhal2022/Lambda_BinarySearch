import re
def is_cat(i):
    
    return re.compile("*?cat")
r=re.compile(".*cat")
a = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo"]

d2 = list(filter(r.match, a))

print(d2)

