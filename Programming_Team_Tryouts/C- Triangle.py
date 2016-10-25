def triangle():
    s = input().split()
    r = input().split()

    works = False
    for i in s:
        if i in r:
            if s.index(i) == r.index(i):
                works = True
            continue
        else:
            print('NO')
            exit()

    if works:
        print('YES')
    else:
        print('NO')


while True:
    try:
        triangle()
    except:
        exit()
