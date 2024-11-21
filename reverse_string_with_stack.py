# create string variables and reverse them using stack, for loop, and reverse() method
string = 'amar'

"""
+----------------------------------------+
| reversing a string using stack         |
+----------------------------------------+
"""

"""# reverse string using a stack

print(f"original strind: {string}")
stack = [] # a list to represent the stack

# pushing the elements of the string into the stack
for i in string:
    stack.append(i)
print(f"String in a stack: {stack}")

string_stack = [] # another list to store the reversed elements of the stack 

# reversing the stack and pushing it into string_stack
for _ in range(len(stack)):
    string_stack.append(stack.pop())
print(f"reversed stack: {string_stack}")

# making sure it comes out as string not stack
e = ''.join(string_stack)
print(f"reversed string: {e}")"""

"""
+----------------------------------------+
| reversing a string using for loop      |
+----------------------------------------+
"""
"""# reversing a string using for loop
reversed_string = ''
for char in string:
    reversed_string = char + reversed_string
print(reversed_string)
"""

"""
+---------------------------------------------+
| reversing a string using reverse() method   |
+---------------------------------------------+
"""
reversed_string = ''.join(reversed(string))
print(reversed_string)