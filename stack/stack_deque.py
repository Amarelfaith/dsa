import collections

stack = collections.deque()

def push():
    e = input('Element: ')
    stack.append(e)
    
def poop():
    if not stack:
        print('Stack is empty')
    else:
        stack.pop()

def view():
    print(stack)
    
while True:
    c = int(input('Select operation: 1.Push 2.Pop 3.View 4.Quit : '))
    if c == 1:
        push()
    elif c == 2:
        poop()
    elif c == 3:
        view()
    elif c == 4:
        break
    else:
        print('unknown operation')