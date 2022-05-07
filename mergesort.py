
class Node():
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        
        itr = self.head 
        while itr.next:
            itr = itr.next
        itr.next = node

    def Print(self):

        if self.head == None:
            print("List is empty")
            return
        
        itr = self.head
        itr_list = ""
        while itr:
            itr_list += str(itr.data)+ "-->"
            itr = itr.next
        return itr_list

    def SortedMerge(self,a,b):
        result = None

        if a== None:
            return b
        if b == None:
            return a
        
        if a.data <= b.data:
            result = a
            result.next = self.SortedMerge(a.next,b)
        else:
            result = b
            result.next = self.SortedMerge(a,b.next)
        return result
    
    def MergeSort(self,head):

        if head == None or head.next == None:
            return head
        
        middle = self.get_middle(head)
        next_to_middle = middle.next
        

        middle.next = None

        left = self.MergeSort(head)
        right = self.MergeSort(next_to_middle)
        

        sorted_list = self.SortedMerge(left,right)
        return sorted_list

    def get_middle(self,head):

        if (head == None):
            return head
        
        slow = head
        fast = head

        while (fast.next != None and fast.next.next !=None):
            slow = slow.next
            fast = fast.next.next
        return slow

if __name__ == "__main__":
    li  = LinkedList()
    li.insert_at_end(10)
    li.insert_at_end(2)
    li.insert_at_end(6)
    li.insert_at_end(3)
    print(li.Print())
    li.head = li.MergeSort(li.head)
    print(li.Print())



        