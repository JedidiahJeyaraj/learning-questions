class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def check_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.check_empty():
            print("STACK IS EMPTY")
            return
        return self.stack.pop()


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(8)
    stack.push(5)
    print(stack.stack)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.stack)
