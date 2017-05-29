import re
#  the method of using find 只用于字符串的查找
a = 'asdfghajk'
b = 'as'
print(a.find(b,0))

#   re 模块

m = re.search(r'.*df.*',a)
print(m.group(0))

n = re.match(r'(as).*',a)

print(n.group(1))

c = a.split('f')
print(c)

d = re.split(r'h',a)
print(d)

t = re.findall(r'a',a)

print(t)