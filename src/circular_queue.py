class CircularQueue:
    def __init__(self, max_length=5):
        self.queue = {}
        self.front = 0
        self.back = 0
        self.max_length = max_length

    def remove_old_ele(self, element):
        if (self.back + 1) % self.max_length == self.front:
            # Queue is full, remove the oldest element
            oldest_element = self.queue[self.front]
            print(f"Queue is full. Removing the oldest element: {oldest_element}")
            self.front = (self.front + 1) % self.max_length

        self.queue[self.back] = element
        self.back = (self.back + 1) % self.max_length
        print(f"Enqueued: {element}")

    def display(self):
        if self.front == self.back:
            print("Queue is empty.")
        else:
            current = self.front
            while current != self.back:
                print(self.queue[current], end=" ")
                current = (current + 1) % self.max_length
            print()
cq1 = CircularQueue(max_length=5)

cq1.remove_old_ele(1)
cq1.remove_old_ele(2)
cq1.remove_old_ele(3)
cq1.remove_old_ele(4)
cq1.remove_old_ele(5)

# Queue is full, removing the oldest element (1)
cq1.remove_old_ele(6)

cq1.display()