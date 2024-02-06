class CircularQueue:
    def __init__(self, max_len=5):
        self.queue = {}
        self.front = 0
        self.back = 0
        self.max_len = max_len

    def remove_old_ele(self, element):
        if (self.back + 1) % self.max_len == self.front:
            old_ele = self.queue[self.front]
            print(f"removing the old ele: {old_ele}")
            self.front = (self.front + 1) % self.max_len

        self.queue[self.back] = element
        self.back = (self.back + 1) % self.max_len
        print(element)

    def display(self):
        if self.front == self.back:
            print("queue is empty.")
        else:
            current = self.front
            while current != self.back:
                print(self.queue[current], end=" ")
                current = (current + 1) % self.max_len
            print()
cq1 = CircularQueue(max_len=5)

cq1.remove_old_ele(1)
cq1.remove_old_ele(2)
cq1.remove_old_ele(3)
cq1.remove_old_ele(4)
cq1.remove_old_ele(5)

cq1.remove_old_ele(6)

cq1.display()