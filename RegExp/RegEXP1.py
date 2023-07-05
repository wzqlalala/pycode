import re
match = re.search(r'[1-9]\d{5}','BIT 100081')
ls = re.findall(r'[1-9]\d{5}','BIT 100155 TGS 256916')
print(ls)
if match:
    print(match.group(0))
for i in ls:
    print(i)
lsplit1 = re.split(r'[1-9]\d{5}','BIT100155 TGS256916')
lsplit2 = re.split(r'[1-9]\d{5}','BIT100155 TGS256916',maxsplit=1)
print(lsplit1)
print(lsplit2)
st = re.sub(r'[1-9]\d{5}', ':zipcode','BIT100155 TGS256 916',count = 1)
print(st)

#match对象
m = re.search(r'[1-9]\d{5}','BIT 100155 TGS 256916')
print(m.string)
print(m.re)
print(m.pos)
print(m.endpos)
print(m.group(0))
print(m.start())
print(m.end())