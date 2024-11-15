from collections import deque

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.popleft()
    
    def is_empty(self):
        return len(self.queue) == 0

def reverse_sequence_with_stack_and_queue(input_sequence):
    stack = Stack()
    queue = Queue()

    # Step 1: Enqueue elements to the queue
    for item in input_sequence:
        queue.enqueue(item)

    # Step 2: Push elements from the queue to the stack
    while not queue.is_empty():
        stack.push(queue.dequeue())

    # Step 3: Transfer the elements back to the queue (reversing the order)
    reversed_sequence = []
    while not stack.is_empty():
        reversed_sequence.append(stack.pop())

    # Return the reversed sequence as a string
    return ''.join(map(str, reversed_sequence))

# Main code
if __name__ == "__main__":
    # Example input: '5 4 3 2 1'
    user_input = input("Enter a sequence of numbers (space-separated): ").split()

    # Reverse the sequence using stack and queue
    reversed_output = reverse_sequence_with_stack_and_queue(user_input)

    # Print the reversed output
    print("Reversed sequence:", reversed_output)
