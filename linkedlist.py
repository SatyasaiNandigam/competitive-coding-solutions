class Node:
    def __init__(self, data= None,next= None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr  = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr  = itr.next
        return count   

    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            count +=1
            itr = itr.next
        
    def insert_at_index(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        if index ==0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node

            itr = itr.next
            count +=1
        
    def insert_after_value(self,data_after,data_to_insert):

        itr = self.head
        count = 0
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert,itr.next)
                itr.next = node
                break

            count +=1
            itr = itr.next
        
        if count == self.get_length():
            raise Exception("Value not found error")
        
        

    def remove_by_value(self,data):
        
        if data == self.head.data:
            self.head = self.head.next
            return

        itr = self.head
        count = 0

        while itr and itr.next != None:
            if itr.next.data == data:
                itr.next = itr.next.next
                break

            count +=1
            itr = itr.next
        
        if count == self.get_length()-1:
            raise Exception("Value not found error")
            
    
    def Print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        listr = ""
        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next
        
        print(listr)


if __name__ == '__main__': 
    li = LinkedList()
    li.insert_values(["apple", "orange","pineapple", "kindhapple"])
    li.insert_after_value("orange","custards")
    li.remove_by_value("sldjf")
    li.Print()
    print("length:",li.get_length())
