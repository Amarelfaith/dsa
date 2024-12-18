"""queue = list()

def enqueue():
    e = input('Element: ')
    queue.append(e)
    
def dequeue():
    if not queue:
        print('Queue is empty')
    else:
        e = queue.pop(0)
        print(f"{e} popped")
    
def view():
    print(queue)
    
while True:
    c = int(input('Select operation: 1.Enqueue 2.Dequeue 3.View 4.Quit: '))
    if c == 1:
        enqueue()
    elif c == 2:
        dequeue()
    elif c == 3:
        view()
    elif c == 4:
        break
    else:
        print('Unknown operation')"""

q = []


def en_q():
    for i in range(0, 31, 10):
        q.insert(0, i)
        print(q)


def de_q():
    if not q:
        print('Queue is empty')
    else:
        q.pop()


def view():
    print(q)


while True:
    c = int(input('Select operation: 1.En_Q 2.De_Q 3.View 4.Quit : '))
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
