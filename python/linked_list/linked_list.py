class Node:
    # initially, null head and nullptr by default
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    # null head
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        # create a new node with data
        node = Node(data, self.head)
        # make the new node head of linked list
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Empty linked list")
            return
        
        # set the variable to head of linked list
        itr = self.head
        listr = ''
        # while itr is not None, meaning the node exists
        while itr:
            # append string
            listr += str(itr.data) + '->'
            # go to next node
            itr = itr.next
        print(listr)
    
    def insert_at_end(self, data):
        # if there is no head, insert the data at head of linked list
        if self.head is None:
            self.head = Node(data, None)
            return
        
        # set itr equal to head of linked list
        itr = self.head
        # while the node exists
        while itr.next:
            # traverse linked list until there is no next node
            itr = itr.next
        
        # insert data at a tail of linked list
        itr.next = Node(data, None)
    
    # take list of values and create a new linked list
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    # get length of linked list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        # head of linked list
        if index == 0:
            # make the head to the next node
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            # previoius element from the node we want to remove
            if count == index - 1:
                # Before doing this, itr.next is pointing to the node we want to remove.
                # By setting it to the next next pointer, which is the next node of the node we want to remove, it removes the node that we want to remove
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        # insert at the head
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            # at the previous position from the position we want to insert the node
            if count == index - 1:
                # initialize node with pointing to the next node from the position we want to insert
                # because the new node needs to be between previous position and the next position
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(20)
    linked_list.insert_at_end(30)
    linked_list.print()
    # linked_list.insert_values(["Peter", "Is", "Amazing"])
    linked_list.remove_at(1)
    linked_list.print()
    # linked_list.remove_at(5)
    linked_list.insert_at(1, 50)
    linked_list.print()
    print("length:", linked_list.get_length())
