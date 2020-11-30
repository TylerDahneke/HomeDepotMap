class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.size = capacity
        self.items = [None] * (self.size + 1)
        self.num_items = 0

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        # Should call perc_up
        if self.is_full():
            return False
        else:
            self.num_items += 1
            self.items[self.num_items] = item
            self.perc_up(self.num_items)
            return True

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.is_empty():
            return None
        return self.items[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        # Should call perc_down
        if self.is_empty():
            return None
        r_ans = self.items[1]
        self.items[1], self.items[self.num_items] = self.items[self.num_items], None
        self.perc_down(1)
        self.num_items -= 1
        return r_ans

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        return [i for i in self.items if i is not None]

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate 
        exactly the number of items in alist'''
        # Bottom-Up construction.  Do NOT call enqueue
        if len(alist) > self.size:
            self.num_items = self.size = len(alist)
            self.items = [None] + alist
        else:
            self.num_items = len(alist)
            remaining_size = self.size - len(alist)
            self.items = [None] + alist + [None] * remaining_size
        counter = self.num_items
        while counter > 1:
            self.perc_down(get_parent(counter))
            counter -= 1

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        return not self.num_items

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        return self.num_items == self.size

    def is_leaf(self, pos):
        truth_table = [False, False]
        if get_left(pos) > self.size or self.items[get_left(pos)] is None:
            truth_table[0] = True
        if get_right(pos) > self.size or self.items[get_right(pos)] is None:
            truth_table[1] = True
        return all(truth_table)

    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return self.size

    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.num_items

    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        truth_table = [False, False]
        if get_left(i) < self.size and self.items[get_left(i)] is not None and self.items[get_left(i)] > self.items[i]:
            truth_table[0] = True
        if get_right(i) < self.size and self.items[get_right(i)] is not None and self.items[get_right(i)] > self.items[
            i]:
            truth_table[1] = True
        if all(truth_table):
            if self.items[get_left(i)] > self.items[get_right(i)]:
                self.swap_left(i)
            else:
                self.swap_right(i)
        elif truth_table[0]:
            self.swap_left(i)
        elif truth_table[1]:
            self.swap_right(i)
        else:
            pass

    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        if i > 1 and self.items[i] > self.items[get_parent(i)]:
            self.items[i], self.items[get_parent(i)] = self.items[get_parent(i)], self.items[i]
            self.perc_up(get_parent(i))

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        self.build_heap(alist)
        pos = len(alist) - 1
        while not self.is_empty():
            alist[pos] = self.dequeue()
            pos -= 1

    def swap_left(self, i):
        self.items[i], self.items[get_left(i)] = self.items[get_left(i)], self.items[i]
        self.perc_down(get_left(i))

    def swap_right(self, i):
        self.items[i], self.items[get_right(i)] = self.items[get_right(i)], self.items[i]
        self.perc_down(get_right(i))


def get_left(pos):
    return pos * 2


def get_right(pos):
    return pos * 2 + 1


def get_parent(pos):
    return int(pos / 2)


def get_smallest(item_1, item_2):
    if item_1 is None:
        return
