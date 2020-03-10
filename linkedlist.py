
class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?   O(n)"""
        # TODO: Loop through all nodes and count one for each
        iterator = self.head
        length = 0
        if self.head == None:
            return 0
        while iterator != None:
            length+=1
            iterator = iterator.next
        return length

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        if self.head == None:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        if self.head == None:
            self.head = Node(item)
            self.tail = self.head
        else:
            temp = self.head
            self.head = Node(item)
            self.head.next = temp

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        if self.head == None:
            print("No thoughts, List Empty")
            return
        else:
            iterator = self.head
            #stops on the node right before the desired node
            while iterator !=  None:
                if quality(iterator.data):
                    return iterator.data
                iterator = iterator.next
            print("No Items, Head Empty")
            return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        
        #checks for empty list
        if self.head == None:
            raise ValueError("empty list")
        else:
            #edge case where the item youre looking for is the first item
            if self.head.data == item:
                self.head = self.head.next  #sets head to the  next node
                #edge case if that was the last node
                if self.head == None:
                    self.tail = self.head
                return
            iterator = self.head    #pointer to iterate  through  list
            found = False
            #loops through list and stops on the node right before the desired node
            while iterator.next !=  None:
                #check if next node has the desired data
                if iterator.next.data == item:
                    found = True
                    break
                iterator = iterator.next    #go to next node
            if found:
                #edge case for if the item youre looking for is the last item
                if iterator.next == self.tail:
                    self.tail = iterator
                    iterator.next = None
                    return
                #makes the node right beofre next pointer equal to the node right after the desired node then deletes it    
                temp = iterator.next
                iterator.next = temp.next
                del temp
            else:
                raise ValueError("Item not found")


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()