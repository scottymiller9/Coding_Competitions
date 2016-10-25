number = int(input())
instance = 0

while instance < number:
    s = list(map(int, input().split()))
    publications = []
    names = {}
    erdosones = []
    erdostwos = []
    for i in range(0, s[0]):
        publications.append(input())
    for i in range(0, s[1]):
        names.update({input(): 'infinity'})

    for i in publications:
        for j in names:
            if j in i and 'Erdos' in i:
                names[j] = 1
                erdosones.append(j)

            else:
                if erdosones:

                    for m in erdosones:
                        if m in i and names[j] == 'infinity':
                            names[j] = 2
                            erdostwos.append(j)
                if erdostwos:
                    for m in erdostwos:
                        if m in i and names[j] == 'infinity':
                            names[j] = 3

print('Scenario', instance + 1)
for x in names:
    print(x)
    for y in names[x]:
        print(y)
instance += 1
