class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._percolate_up(len(self.heap) - 1)

    def _percolate_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = (index - 1) // 2

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
       
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._percolate_down(0)
        return max_val

    def _percolate_down(self, index):
        length = len(self.heap)
        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < length and self.heap[left] > self.heap[largest]:
                largest = left

            if right < length and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def delete(self, val):
        if val not in self.heap:
            return False
       
        index = self.heap.index(val)
        if index == len(self.heap) - 1:
            self.heap.pop()
            return True
       
        self.heap[index] = self.heap.pop()
        parent = (index - 1) // 2
        if index > 0 and self.heap[parent] < self.heap[index]:
            self._percolate_up(index)
        else:
            self._percolate_down(index)
        return True

if __name__ == "__main__":
    max_heap = MaxHeap()
    print("--- Max Heap Program ---")
    print("Commands:")
    print("  <number>        - Insert a number")
    print("  peek            - View max element")
    print("  delete <number> - Delete a specific number")
    print("  sort            - Extract all in descending order")
    print("  q / quit        - Exit\n")

    while True:
        user_input = input("Enter command: ").strip()
       
        if user_input.lower() in ('q', 'quit'):
            print("Exiting program. Goodbye!")
            break
           
        elif user_input.lower() == 'peek':
            max_val = max_heap.peek()
            if max_val is not None:
                print(f"-> Max element (Peek): {max_val}\n")
            else:
                print("Heap is empty!\n")
               
        elif user_input.lower() == 'sort':
            if not max_heap.heap:
                print("Heap is currently empty!\n")
                continue
               
            print("\nExtracting elements in descending order:")
            descending_list = []
            while max_heap.heap:
                descending_list.append(max_heap.extract_max())
           
            print(f"-> Result: {descending_list}")
            print("\n(Heap is now empty.)\n")
           
        elif user_input.lower().startswith('delete '):
            try:
                num_to_delete = int(user_input.split()[1])
                success = max_heap.delete(num_to_delete)
                if success:
                    print(f"-> Successfully deleted {num_to_delete}. Current Heap: {max_heap.heap}\n")
                else:
                    print(f"-> Value {num_to_delete} not found in heap.\n")
            except (IndexError, ValueError):
                print("Invalid delete format! Use 'delete <number>'.\n")
               
        else:
            try:
                num = int(user_input)
                max_heap.insert(num)
                print(f"-> Current Max Heap: {max_heap.heap}\n")
            except ValueError:
                print("Invalid input! Enter a number, 'peek', 'delete <num>', 'sort', or 'q'.\n")
