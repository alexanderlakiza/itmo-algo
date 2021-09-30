class EmptyStackException(Exception):
    pass


class Stack:
    class Node:
        def __init__(self, value, nextnode):
            self.value = value
            self.nextnode = nextnode

    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, value):
        self.top = Stack.Node(value, self.top)

    def pop(self):
        if self.isempty():
            raise EmptyStackException
        val = self.top.value
        self.top = self.top.nextnode
        return val


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    while not s.isempty():
        print(s.pop())
