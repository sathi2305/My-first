queue = []

# Enqueue (add)
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue:", queue)

# Dequeue (remove first)
first = queue.pop(0)
print("Dequeued:", first)
print("After dequeue:", queue)
