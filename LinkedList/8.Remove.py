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

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_Node = Node(value)
        temp = self.get(index - 1)
        new_Node.next = temp.next
        temp.next = new_Node
        self.length += 1
        return True

    def popFirst(self):
        # for no node
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        if self.length == 0:
            self.tail = None
        return temp.value

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

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.popFirst()
        if index == self.length:
            return self.pop()

        prev = self.get(index-1)
        temp = self.get(index)
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp






my_linked_list = LinkedList(0)
my_linked_list.append(2)
my_linked_list.append(5)
my_linked_list.append(3)
my_linked_list.print_list()

my_linked_list.remove(2)
print("after removal ")
my_linked_list.print_list()
