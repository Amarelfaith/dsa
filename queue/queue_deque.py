import collections
q = collections.deque()


def en_q():
    e = input('Element: ')
    q.append(e)


def de_q():
    if not q:
        print('Queue is empty')
    else:
        q.popleft()


def view():
    print(q)


while True:
    c = int(input('Select operation: 1.En_Q 2.De_Q 3.Veiw 4.Quit: '))
    if c == 1:
        en_q()
    elif c == 2:
        de_q()
    elif c == 3:
        view()
    elif c == 4:
        break
    else:
        print('Unknon operation')
