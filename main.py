# List and Tuple
"""some_list = list()
for i in range(100):
    some_list.append(i)
    

tuple1 = (1,2,3,4,5,6)
print(tuple1)
for i in tuple1:
    print(i)
    
tuple2 = tuple()
print(type(tuple2))"""

# Set and Dictionary
"""d = {}  # an empty Dictionary
emails = {'amar': 'amar@xyz.com', 'muhd': 'muhd@xyz.com'}
print(emails)

try:
    d = {[1, 2]: (4, 5)}
    print('This works')
except TypeError:
    print('There is an error: You cannot use list as a key in dictionary because it is mutable')


print(emails['amar'])
for i in emails: # to print all the elements of the dictionary 
    print(emails[i])
"""
"""set1 = set()
set2 = {1, 2, 3, 4}
set3 = set([4, 5, 6, 7])
set4 = set('hello')  # duplicate vlues are ignored
set1.add(1)
for i in set2:
    print(i)
"""


"""
# this program offers many stack operations: push, pop, and reverse
stack = []

def push():

    if len(stack) >= n:
        print('stack is full: ', stack)
    else:
        element = int(input('Element: '))
        stack.append(element)
        print(stack)


def pop_e():

    if not stack:
        print('Stack is empty')
    else:
        print(f"Popped stack: {stack.pop()}")


def reverse_list():

    if not stack:
        print('cannot reverse an empty stack!')
    else:
        e = []
        for _ in range(len(stack)):
            e.append(stack.pop())
    print(f"Reversed list: {e}")


n = int(input('Limit of stack: '))

while True:

    choice = int(
        input('Select an operation: 1.Push 2.Pop 3.Reverse 4.Quit \n: '))
    if choice == 1:
        push()
    elif choice == 2:
        pop_e()
    elif choice == 3:
        reverse_list()
    elif choice == 4:
        break
    else:
        print('Unknown choice')
"""

# creating a stack using queue
"""# the number 3 sets the maximum limit of the elements in the stack
import queue
stack = queue.LifoQueue(3)
stack.put(10)
stack.put(20)
stack.put(30)
stack.put(40, timeout=1)
"""

# create a stack using list and reverse it
name = 'amar'
new_name = list()
for i in name:
    new_name.append(i)
    
print(new_name)
# reversing the string
reversed_name = []
for _ in range(len(new_name)):
    reversed_name.append(new_name.pop())
    
print(f"Reversed name: {reversed_name}")