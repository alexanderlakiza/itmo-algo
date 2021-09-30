class EmptyStack(Exception):
    pass


class StackOverflow(Exception):
    pass


class Stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def isempty(self):
        if len(self.stack) == 0:
            return True
        return False

    def push(self, item):
        if len(self.stack) < self.capacity:
            self.stack.append(item)
        else:
            raise StackOverflow

    def pop(self):
        if self.isempty():
            raise EmptyStack
        self.stack = self.stack[:-1]

    def print(self):
        print(self.stack)


if __name__ == "__main__":
    q = Stack(5)
    q.push(10)
    q.print()
    q.push(4)
    q.push(15)
    q.push(40)
    q.push(26)
    q.print()
    q.pop()
    q.print()
    q.pop()
    q.print()
