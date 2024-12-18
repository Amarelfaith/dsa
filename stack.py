# Implementing stack using list
# using the append() method to push to the stack
"""stack = list()
for i in range(5):
    stack.append(i)
print(stack)

# using the pop() method to remove from the stack 
for _ in range(len(stack)):
    stack.pop()
    
print(stack)"""\

"""
# another way of implemeting a stack using list with user input

stack = []


def push():
    element = input('Enter the element: ')
    stack.append(element)
    print(stack)


def pop_element():
    if not stack:
        print('Stack is empty.')
    else:
        e = stack.pop()
        print(f"removed element: {e}")
        print(stack)


while True:
    
    choice = int(input('Select the operation 1.push 2.pop 3.cancel \n: '))
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print('Unknown choice')
"""

# implementation of stack using modules

"""# collections module 
import collections
stack = collections.deque()
for i in range(0, 31, 10):
    stack.append(i)
print(stack)
e = []
for _ in range(len(stack)):

    e.append(stack.pop())
print(f"Reversed stack: {e}")"""

# queue module 
"""import queue as q 
stack = q.LifoQueue()
# pushed items into the stack
for i in range(5):
    stack.put(i)

# if we want to print this stack we've to go through the process below because print() won't work with LifoQueue 
# we create a temporary stack using list where we'll store all the popped elements of the stack
# now we can pop all the items from the stack and save them to temp_stack
# this will come in reverse order so we've to reverse the temp_stack
temp_stack = []
while not stack.empty():
    item = stack.get()
    temp_stack.append(item)
    print("popped: ", item)
# This prints the temp_stack as it is after we get its input above 
print('reversed stack: ',temp_stack)

# reversing the stack to get it in its original form.
s_tack = []
for item in reversed(temp_stack):
    s_tack.append(item) 

# now printing the stack as it should be
print(f"My LifoQueue stack: {s_tack}")"""

q = []
print(not q)