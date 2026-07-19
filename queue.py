# --- STACK IMPLEMENTATION FROM SCRATCH ---
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# --- QUEUE IMPLEMENTATION FROM SCRATCH ---
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)  # O(n) for simple implementation, can be optimized with pointers

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# --- APPLICATION 1: BALANCED BRACKETS USING STACK ---
def is_balanced(s: str) -> bool:
    stack = Stack()
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping.values():
            stack.push(char)
        elif char in mapping:
            if stack.is_empty() or stack.pop() != mapping[char]:
                return False
    return stack.is_empty()


# --- APPLICATION 2: MAX SLIDING WINDOW SUM USING QUEUE APPROACH ---
# Note: For tracking subarray structural rolling sums efficiently, we use a basic queue tracking system.
def max_sliding_window_sum(nums: list, k: int) -> int:
    if not nums or k <= 0 or k > len(nums):
        return 0
        
    q = Queue()
    current_sum = 0
    
    # Seed the initial window
    for i in range(k):
        q.enqueue(nums[i])
        current_sum += nums[i]
        
    max_sum = current_sum
    
    # Roll the window forward across the rest of the array
    for i in range(k, len(nums)):
        removed = q.dequeue()
        q.enqueue(nums[i])
        current_sum = current_sum - removed + nums[i]
        if current_sum > max_sum:
            max_sum = current_sum
            
    return max_sum


# --- VERIFICATION TESTS ---
print("Balanced Brackets Tests:")
assert is_balanced("{[()]}") is True
assert is_balanced("{[(])}") is False
assert is_balanced("(()") is False
print("Passed!")

print("Sliding Window Tests:")
assert max_sliding_window_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16  # Window [5, 3, 6] sum is 14, [3, 6, 7] sum is 16
assert max_sliding_window_sum([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3) == 16 # Window [2, 1, 7]=10, [1, 7, 8]=16
print("Passed!")