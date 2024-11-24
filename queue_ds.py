# implementation of queue data structure using list

"""# this enqueue elements from left to righ [0, 10, 20, 30]
queue = list()
for i in range(0, 31, 10):
    queue.append(i)
print(queue)

for i in range(len(queue)):
    print(queue.pop(0))"""

"""# this enqueue elements from right to left [30, 20, 10, 0]
queue = []
for i in range(0, 31, 10):
    queue.insert(0, i)
print(queue)

for _ in range(len(queue)):
    queue.pop()
print(queue)"""

"""queue = list()


def enqueue():
    element = int(input('Enter queue element: '))
    queue.append(element)
    print(element, 'is added to the queue')


def dequeue():
    if not queue:
        print('Queue is empty')
    else:
        e = queue.pop(0)
        print('removed element: ', e)


def display_queue():
    print(queue)


while True:
    choice = int(
        input('choose: 1.Add to queue 2.Remove from queue 3.Print queue 4.Quit: '))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display_queue()
    elif choice == 4:
        break
    else:
        print('Unknown choice!')
"""

# queue implementation using classes 

"""# queue implementation using deque from collections module 
import collections
queue = collections.deque()
q_left = collections.deque()
for i in range(10):
    queue.append(i)
    q_left.appendleft(i)
print(queue)
print('From left: ',q_left)

for _ in range (len(queue)):
    queue.popleft()
print('This should be empty: ', queue)

for _ in range(len(q_left)):
    q_left.pop()
print('This should also be empty: ', q_left)"""


# implementing queueu using deque class of collections
"""# from right to left
import collections
q = collections.deque()


def enqueue():
    e = int(input('Enter element: '))
    q.append(e)
    print(f"{e} is added to the queue")


def dequeue():
    if not q:
        print('queue is empty')
    else:
        print(q.popleft(), 'is removed from queue')


def display():
    print(q)


while True:
    choice = int(input('Options: 1.Insert 2.Remove 3.Show 4.Quit \nChoose: '))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print('Unknown choice')"""

"""# implementing queue using deque from left to right 
import collections
q = collections.deque()

def enqueue():
    e = int(input('Enter element: '))
    q.appendleft(e)
    print(e, ' is added to queue')
    
def dequeue():
    if not q:
        print('Queue is empty')
    else:
        print(q.pop(), ' is removed from the queue')
        
def display():
    print(q)

while True:
    c = int(input('Options: 1.Insert 2.Remove 3.Show 4.Quit \nChoose: '))
    if c == 1:
        enqueue()
    elif c == 2:
        dequeue()
    elif c == 3:
        display()
    elif c == 4:
        break 
    else:
        print('Unknown choice')"""
        
        
        
"""# queue implementation using queue class 
import queue
q = queue.Queue()

def enqueue():
    e = int(input('Enter element: '))
    q.put(e)
    print(e, ' is added to the queue')

def dequeue():
    if q.empty():
        print('Queue is empty')
    else:
        print(q.get(), ' is removed from queue')
        
def display():
    print(vars(q))
    
while True:
    c = int(input('Options: 1.Insert 2.Remove 3.Show 4.Quit \nChoose: '))
    if c == 1:
        enqueue()
    elif c == 2:
        dequeue()
    elif c == 3:
        display()
    elif c == 4:
        break 
    else:
        print('Unkown choice')"""
        
"""# implemeting queue using list Right oto Left 
q = []

def enqueue():
    e = int(input('Enter element: '))
    q.append(e)
    print(e, 'is added to the queue')
    
def dequeue():
    if not q:
        print('Queue is empty!')
    else:
        print(q.pop(0),' is removed form queue')
        
def display():
    print(q)
    
while True:
    c = int(input('Options: 1.Insert 2.Remove 3.Show 4.Quit \nChoose: '))
    if c == 1:
        enqueue()
    elif c == 2:
        dequeue()
    elif c == 3:
        display()
    elif c == 4:
        break 
    else:
        print('Unknown choice')"""


# implementing queue using list from left oto right
q = []

def enqueue():
    e = int(input('Enter element: '))
    q.insert(0, e)
    print(e, ' is added to queue')
    
def dequeue():
    if not q:
        print('Queue is empty')
    else:
        print(q.pop(), ' is removed from queue')
    
def display():
    print(q)
    
while True:
    c = int(input('Options: 1.Insert 2.Remove 3.Show 4.Quit'))
    if c == 1:
        enqueue()
    elif c == 2:
        dequeue()
    elif c == 3:
        display()
    elif c == 4:
        break 
    else: print('unknown choice')      