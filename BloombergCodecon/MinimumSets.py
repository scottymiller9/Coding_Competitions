n = int(input())
l = []
for i in range(0, n):
    temp = input()
    l.append(temp)
    o = []
    c = []
for i in l:
    if i.startswith('^'):
        i = i.replace('^', '')
        for k in c:
            if i in k:
                o.append(k)
                c.remove(k)
            else:
                a = []
                a.append(i)
                o.append(a)
    elif i.startswith('/'):
        i = i.replace('/', '')
        for k in o:
            if i in k:
                c.append(k)
                o.remove(k)
    else:
        for j in o:
            j.append(i)

print(o)
print(c)
