""" generate a list of 10s from 10 to 100 inclusive print it out and reverse
 the list to start from 100 and print it out"""

# created an empty list and generate the elements using for loop
stack = []
for i in range(10, 101, 10):
    stack.append(i)
print(f"First list: {stack}")

# crearted a list that will take any poped element of the stack
reversed_list = list()
for _ in range(len(stack)):
    reversed_list.append(stack.pop())
print(f"Revered list: {reversed_list}")
