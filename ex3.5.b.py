import random
from time import perf_counter
from matplotlib import pyplot as plt


# Heap Class

class HeapPriority:
    def __init__(self):
        self.heap = []
    
    def push(self, value, priority):
        self.heap.append((priority, value))
        self._heapify_up(len(self.heap) - 1)
    
    def pop(self):
        if len(self.heap) == 0:
            raise Exception("Queue is empty.")
        self._swap(0, len(self.heap) - 1)
        priority, value = self.heap.pop()
        self._heapify_down(0)
        return (priority, value)
    
    def peek(self):
        if len(self.heap) == 0:
            raise Exception("Queue is empty.")
        return self.heap[0]
    
    def size(self):
        return len(self.heap)
    
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[parent] > self.heap[index]:
            self._swap(parent, index)
            self._heapify_up(parent)
    
    def _heapify_down(self, index):
        left = index * 2 + 1
        right = index * 2 + 2
        smallest = index
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# Linked List

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None

class LinkedListPriority:
    def __init__(self):
        self.head = None

    def enqueue(self, value, priority):
        new_node = Node(value, priority)
        if self.head is None or priority > self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None and priority <= current_node.next.priority:
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            return value

    def is_empty(self):
        return self.head is None

    def __str__(self):
        result = []
        current_node = self.head
        while current_node is not None:
            result.append((current_node.value, current_node.priority))
            current_node = current_node.next
        return str(result)



if __name__ == "__main__":
    heap = HeapPriority()
    linked_list = LinkedListPriority()
    
    for i in range(1000):
        value = random.randint(1, 10000)
        priority = random.randint(0, 10)
        heap.push(value, priority)
        linked_list.enqueue(value, priority)

    heap_push_times = []
    heap_pop_times = []
    linkedlist_enqueue_times = []
    linkedlist_dequeue_times = []

    for i in range(100):
        value = random.randint(1, 10000)
        priority = random.randint(0, 10)
        start_heap_push = perf_counter()
        heap.push(value, priority)
        stop_heap_push = perf_counter()
        heap_push_times.append(stop_heap_push - start_heap_push)

        start_heap_pop = perf_counter()
        heap.pop()
        stop_heap_pop = perf_counter()
        heap_pop_times.append(stop_heap_pop - start_heap_pop)

        
        start_linkedlist_enqueue = perf_counter()
        linked_list.enqueue(value, priority)
        stop_linkedlist_enqueue = perf_counter()
        linkedlist_enqueue_times.append(stop_linkedlist_enqueue - start_linkedlist_enqueue)
        
        start_linkedlist_dequeue = perf_counter()
        linked_list.dequeue()
        stop_linkedlist_dequeue = perf_counter()
        linkedlist_dequeue_times.append(stop_linkedlist_dequeue - start_linkedlist_dequeue)

    heap_pop_total = sum(heap_pop_times)
    heap_push_total = sum(heap_push_times)
    linkedlist_enqueue_total = sum(linkedlist_enqueue_times)
    linkedlist_dequeue_total = sum(linkedlist_dequeue_times)
    print(f"Heap push: Total time = {heap_push_total:.6f}s")
    print(f"Linked List enqueue: Total time = {linkedlist_enqueue_total:.6f}s")

    print(f"Heap pop: Total time = {heap_pop_total:.6f}s")
    print(f"Linked List dequeue: Total time = {linkedlist_dequeue_total:.6f}s")


    fig, axs = plt.subplots(2,2)
    axs1 = axs[0, 0]
    axs2 = axs[0, 1]
    axs3 = axs[1, 0]
    axs4 = axs[1, 1]

    axs1.plot(heap_pop_times)
    axs1.set_xlabel('Frequency')
    axs1.set_ylabel('Time (s)')
    axs1.set_title('Heap Pop')

    axs2.plot(heap_push_times)
    axs2.set_xlabel('Frequency')
    axs2.set_ylabel('Time (s)')
    axs2.set_title('Heap Push')

    axs3.plot(linkedlist_dequeue_times)
    axs3.set_xlabel('Frequency')
    axs3.set_ylabel('Time (s)')
    axs3.set_title('Linked List Dequeue')

    axs4.plot(linkedlist_enqueue_times)
    axs4.set_xlabel('Frequency')
    axs4.set_ylabel('Time (s)')
    axs4.set_title('Linked List Enqueue')

    plt.suptitle("Inefficient vs Efficient Priority Queue Insertion/Extraction")
    plt.tight_layout()
    plt.show()