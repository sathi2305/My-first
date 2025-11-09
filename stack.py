stack = []  # empty stack

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)   # [10, 20, 30]

# Pop element (LIFO)
top = stack.pop()
print("Popped:", top)    # 30

print("After pop:", stack)  # [10, 20]

# Peek top element
print("Top element:", stack[-1])  # 20
