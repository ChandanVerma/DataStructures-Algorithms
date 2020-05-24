class Node(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        
        itr = self.head
        llist = ''
        while itr:
            llist += str(itr.data) + '-->'
            itr = itr.next

        print(llist)

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for i in data_list:
            self.insert_at_end(i)

    def get_length(self):
        counter = 0
        itr = self.head
        while itr:
            counter +=1
            itr = itr.next
        
        return counter

    def remove_at(self, index):
        if self.head == None:
            print('Linked list is empty')
            return
        
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.next
            return

        counter = 0
        itr = self.head
        while itr:
            if counter == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            counter +=1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.insert_at_begining(data)
            return

        counter = 0
        itr = self.head

        while itr:
            if counter == index - 1:
                itr.next = Node(data, itr.next)
                break
            
            itr = itr.next
            counter +=1

    def insert_after_value(self, value, data):
        if self.head.data == value:
            self.head.next = Node(data, self.head.next)
            return

        itr = self.head

        while itr:
            if itr.data == value:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, value):
        if self.head is None:
            print('Linked list is empty')
            return

        if self.head.data == value:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                break
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("banana","jackfruit")
    ll.print()
    ll.remove_by_value("mango") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()

    