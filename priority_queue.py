"""implementing PriorityQueue using list"""

"""# least value -> highest priority
p_q = []
p_q.append(20)
p_q.append(10)
p_q.append(40)
p_q.append(30)
print(p_q)
# sorting the priority queue
p_q.sort()
print('sorted: ', p_q)

for _ in range(len(p_q)):
    print(p_q.pop(0), 'is served first')

print(f"{p_q} is empty")"""

"""# highest value -> highest priority 
q = []
for i in range(0, 41, 10):
    q.append(i)
    
print(q)

# sorting the queue 
q.sort(reverse=True)
print('Sorted based on priority: ', q)

for _ in range(len(q)):
    print(q.pop(0), ' is served first')
   """

# PriorityQueue() with tuple(priority, value)
q = []
q.append((1, 'amar'))
q.append((3, 'abk'))
q.append((4, 'muhd'))
q.append((2, 'mhd'))
q.append((5, 'bintu'))
print('as is: ', q)

# sort for least value -> high priority
q.sort()

print('sorted queue: ', q)
# uncomment for high value -> high priority
# q.sort(reverse=True)

for _ in range(len(q)):
    print(q.pop(0), ' is served first')


""" Implementing priority queue using PriorityQueue() class"""


"""# least value to highest priority
import queue
q = queue.PriorityQueue()
for i in range(0,61,10):
    q.put(i)
    
while not q.empty():
    print(q.get(),' is served first')"""

# highest values -> highest priority
