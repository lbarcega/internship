def is_empty(list):
    return len(list) == 0

def peek_stack(stack):
    if(is_empty(stack) == False):
        item = stack[-1]
        print(f"Top of stack: {item}")
        return 
    else:
        print("Cannot peek an empty stack.")

def peek_queue(queue):
    if(is_empty(queue) == False):
        item = queue[0]
        print(f"Top of queue: {item}")
        return 
    else:
        print("Cannot peek an empty queue.")

def push(stack, item):
    stack.append(item)
    print(f"Pushed item: {item}")
    return stack

def pop(stack):
    if(is_empty(stack) == False):
        item = stack.pop()
        print(f"Popped item: {item}")
        return 
    else:
        print("Cannot pop an empty stack.")

def enqueue(queue, item):
    queue.append(item)
    print(f"Enqueued item: {item}")
    return queue

def dequeue(queue):
    if(is_empty(queue) == False):
        item = queue.pop(0)
        print(f"Dequeued item: {item}")
        return item
    
s1 = []
peek_stack(s1)
pop(s1)
push(s1, "grape")
push(s1, "gasoline")
push(s1, "grenade")
peek_stack(s1)
pop(s1)
peek_stack(s1)

print("\n")

q1 = []
peek_queue(q1)
dequeue(q1)
enqueue(q1, "wolf")
enqueue(q1, "walrus")
enqueue(q1, "wailord")
peek_queue(q1)
dequeue(q1)
peek_queue(q1)