class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        # for no node
        if self.length == 0:
            return None
        temp =self.head
        pre = self.head
        # for more 2 or than 2
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next=None
        self.length -= 1
        # for 1 node only
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value


my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) items -Returns 2 Node
print(my_linked_list.pop())
# (1) items -Returns 1 Node
print(my_linked_list.pop())
# (0) items -Returns None
print(my_linked_list.pop())
my_linked_list.print_list()