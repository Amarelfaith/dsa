import queue

stack = queue.LifoQueue()


def push():
    e = input('Element: ')
    stack.put(e)


def poop():
    stack.get(timeout=1)


def view():
    print(vars(stack))


while True:
    c = int(input('Select operation: 1.Push 2.Pop 3.View 4.Quit: '))
    if c == 1:
        push()
    elif c == 2:
        poop()
    elif c == 3:
        view()
    elif c == 4:
        break
    else:
        print('Unknown operation')
