class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print("pushed item: " + item)

    def pop(self):
        if self.empty():
            return "stack is empty"
        return self.stack.pop()

    def display(self):
        print(self.stack)


if __name__ == "__main__":
    stack = Stack()
    stack.push(str(1))
    stack.push(str(2))
    stack.push(str(3))
    stack.push(str(4))
    stack.push(str(5))
    print(stack.empty())
    print("popped item: " + stack.pop())
    print("stack now: ")
    stack.display()
