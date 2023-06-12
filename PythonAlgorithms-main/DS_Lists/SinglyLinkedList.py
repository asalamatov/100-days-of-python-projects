class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def printList(self):
        temp = self.head
        linked_list = ""
        while(temp):
            linked_list += (str(temp.val) + "=>")
            temp = temp.next
        linked_list = linked_list[:-2]
        print(linked_list)

    def insertNode(self, val, pos):
        target = ListNode(val)
        if pos==0:
            target.next = self.head
            self.head = target
            return
        def getPrev(pos):
            temp = self.head
            count = 1  
            while count < pos:
                temp = temp.next
                count +=1
            return temp

        prev = getPrev(pos)
        nextNode = prev.next
        prev.next = target
        target.next = nextNode

        
    
linked_list = LinkedList()
linked_list.head = ListNode(5)

second_node = ListNode(1)
third_node = ListNode(2)
fourth_node = ListNode(9)

linked_list.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node
linked_list.printList()
linked_list.insertNode(100, 2)
linked_list.printList()
