import queue
q = queue.Queue()


def en_q():
    for i in range(10, 51, 10):
        q.put(i)


def de_q():
    if q.empty():
        print('Queue is empty')
    else:
        q.get(0)


def view():
    print(vars(q))


while True:
    c = int(input('Select operation: 1.En_Q 2,De_Q 3.View 4.Quit: '))
    if c == 1:
        en_q()
    elif c == 2:
        de_q()
    elif c == 3:
        view()
    elif c == 4:
        break
    else:
        print('Unknown operation')
