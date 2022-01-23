class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("the previous node not in the list")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.next = None

    def printList(self):
        temp = self.head
        while temp:
            print(str(temp.data), end=" ")
            temp = temp.next

    def deleteNode(self, pos):
        temp = self.head

        if pos == 0:
            self.head = temp.next
            temp = None
            return

        for _ in range(pos - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next
        temp.next = None
        temp.next = next

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def sortList(self, head):
        current = head
        index = Node(None)

        if head is None:
            return
        else:
            while current is not None:
                index = current.next
                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data
                    index = index.next
                current = current.next


if __name__ == "__main__":
    l = LinkedList()
    while 1:
        print("1/ insert items\n2/ print all items\n3/ quit")
        req = str(input("enter an order: "))
        
        if req == "1":
            for _ in range(int(input("size of the linked list: "))):
                l.insertAtBeginning(int(input()))
        if req == "2":
            l.printList()
            print()
        if req == "3":
            break

