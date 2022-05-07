# Merging two sorted linked lists 

from typing import List


class Node:
    def __init__(self,data,next= None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
    
    def insert_at_end(self,data):
        
        if self.head == None:
            self.head = Node(data)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def Print(self):
        
        if self.head == None:
            print("Empty Linkedlist")
            return 
        
        itr = self.head
        itr_list = ""
        while itr:
            itr_list += str(itr.data) + '-->'
            itr = itr.next
        return itr_list


def MergeSort(headA,headB):
    dummy_Node = Node(0)
    tail = dummy_Node

    while True:
        if headA == None:
            tail.next = headB
            break
        if headB == None:
            tail.next = headA
            break

        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else: 
            tail.next = headB
            headB = headB.next

        tail = tail.next
    return dummy_Node.next


if __name__ == "__main__":
    listA = LinkedList()
    listB = LinkedList()

    listA.insert_at_end(10)
    listA.insert_at_end(15)
    listA.insert_at_end(20)

    listB.insert_at_end(5)
    listB.insert_at_end(12)
    listB.insert_at_end(19)

    print(listA.Print())
    print(listB.Print())

    listA.head = MergeSort(listA.head,listB.head)
    print(listA.Print())