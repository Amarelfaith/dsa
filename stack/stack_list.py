
stack = list()


def push():
    e = input('Element: ')
    stack.append(e)


def poop():
    if not stack:
        print('Stack is empty')
    else:
        stack.pop()


def display():
    print(stack)


while True:
    choice = int(input('Select Operation: 1.Push 2.Pop 3.Show 4.Quit : '))
    if choice == 1:
        push()
    elif choice == 2:
        poop()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print('unknown operation')
