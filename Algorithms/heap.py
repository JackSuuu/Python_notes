class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i): return (i - 1) // 2
    def left(self, i): return 2 * i + 1
    def right(self, i): return 2 * i + 2

    def insert(self, val):
        self.heap.append(val)
        self.up_heapify(len(self.heap) - 1)

    def up_heapify(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            p = self.parent(i)
            # exchange element to make them go up
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        # Move last element to root and heapify down
        self.heap[0] = self.heap.pop()
        self.down_heapify(0)
        return root

    def down_heapify(self, i):
        size = len(self.heap)
        while self.left(i) < size:
            smallest = i
            l = self.left(i)
            r = self.right(i)

            if l < size and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < size and self.heap[r] < self.heap[smallest]:
                smallest = r
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def print_heap(self):
        print(self.heap)


class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i): return (i - 1) // 2
    def left(self, i): return 2 * i + 1
    def right(self, i): return 2 * i + 2

    # Max-Heap-Insert
    def insert(self, val):
        self.heap.append(val)
        self.up_heapify(len(self.heap) - 1)

    def up_heapify(self, i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            p = self.parent(i)
            # exchange element to make them go up
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p

    def print_heap(self):
        print(self.heap)


if __name__ == "__main__":
    print("MinHeap Example:")
    h = MinHeap()
    h.insert(5)
    h.insert(3)
    h.insert(8)
    h.insert(1)
    h.print_heap()  # Output should be something like [1, 3, 8, 5]

    print(h.extract_min())  # Should print 1
    h.print_heap()  # Heap after removing 1

    print("\nMaxHeap Example:")
    max_h = MaxHeap()
    max_h.insert(5)
    max_h.insert(3)
    max_h.insert(8)
    max_h.insert(1)
    max_h.print_heap()  # Output should be something like [8, 5, 3, 1]