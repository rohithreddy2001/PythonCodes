'''
pattern for linked_list is:
1st creating a class Node
2nd creating a class Linkedlist
3rd creating Nodes
4th printing the Linkedlist
'''


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("LinkedList is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, Index):
        if Index < 0 or Index >= self.get_length():
            Exception("Invalid Index")
        if Index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == Index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, Index, data):
        if Index < 0 or Index >= self.get_length():
            Exception("Invalid Index")

        if Index == 0:
            self.insert_at_begining(data)

        count = 0
        itr = self.head
        while itr:
            if count == Index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next

    def get(self, index):
        itr = self.head
        count = 0
        while itr:
            if count == index:
                return itr.data
            itr = itr.next
            count += 1
        return None


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    # ll.print()
    # ll.remove_by_value("orange")  # remove orange from linked list
    # ll.print()
    # ll.remove_by_value("figs")
    # ll.print()
    # ll.remove_by_value("banana")
    # ll.remove_by_value("mango")
    # ll.remove_by_value("apple")
    # ll.remove_by_value("grapes")
    # ll.print()
    ll.print()
    print(ll.get(4))


    # ll = LinkedList()
    # ll.insert_at_begining(10)
    # ll.insert_at_begining(20)
    # ll.insert_at_end(3)
    # ll.insert_at_end(4)
    # ll.insert_at_end(5)
    # ll.insert_values(['Rohith', 'Tarun', 'Ifteq', 'Prem', 'Adhi'])
    # ll.print()
    # print("Length: ",ll.get_length())
    # ll.remove_at(2)
    # ll.print()
    # print("Length: ", ll.get_length())
    # ll.insert_at(2, "Iftequer")
    # ll.print()








