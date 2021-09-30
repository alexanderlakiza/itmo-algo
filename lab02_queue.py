class EmptyQueue(Exception):
    pass


class QueueOverflow(Exception):
    pass


class Queue:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity
        assert(capacity > 0)

    def isempty(self):
        if len(self.items) == 0:
            return True
        return False

    def push(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            raise QueueOverflow

    def pop(self):
        if self.isempty():
            raise EmptyQueue
        self.items = self.items[1:]

    def print(self):
        print(self.items)


if __name__ == "__main__":
    q = Queue(5)
    q.push(10)
    q.push(4)
    q.push(15)
    q.push(40)
    q.push(26)
    q.print()
    q.pop()
    q.print()