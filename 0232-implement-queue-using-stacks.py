class Queue:
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def balance(self):
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())

    def is_empty(self) -> bool:
        return not self.push_stack and not self.pop_stack

    def push(self, n: int) -> None:
        self.push_stack.append(n)

    def pop(self) -> int:
        if self.is_empty():
            return -1
        self.balance()
        return self.pop_stack.pop()

    def peek(self) -> int:
        if self.is_empty():
            return -1
        self.balance()
        return self.pop_stack[-1]


queue = Queue()
queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.is_empty())
