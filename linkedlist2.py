class Node():
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def insert_at_end(self,data):

        node = Node(data,None)

        if self.head == None:
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node
    
    def inser_values(self,data_list):
        self.head = None
        
        for data in data_list:
            self.insert_at_end(data)

    def GetLength(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count 

    def remove_at(self,index):
        if index<0 or index>=self.GetLength():
            raise Exception("Invalid Index")
        
        if index ==0:
            self.head = self.head.next
            return 
            
        count = 1
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break 
            count +=1
            itr = itr.next

    def insert_at_index(self,index,data):
        if index < 0 or index >= self.GetLength():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = Node(data,self.head)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = Node(data,itr.next)
                return
            count +=1
            itr = itr.next
        
    def insert_after_value(self,data_after,data_to_insert):
        
        itr = self.head
        count = 0
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                return 
            count +=1 
            itr = itr.next
        
        if count== self.GetLength():
            raise Exception("Value not found")

    def remove_by_value(self, value):
        
        if value == self.head:
            self.head = self.head.next
        
        itr = self.head
        count = 0
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                return 
            count +=1
            itr = itr.next
        
        if count == self.GetLength()-1:
            raise Exception("Value not Found")

    
    def Print(self):
        if self.head == None:
            print("Linked list is empty")
            return 

        itr = self.head
        itrlist = ""
        while itr:
            itrlist += str(itr.data)+"-->"
            itr = itr.next
        print(itrlist)
    

if __name__ == "__main__":
    lik = LinkedList()
    lik.inser_values([1,2,3,4,5])
    lik.insert_after_value(1,11)
    lik.remove_by_value(19)
    lik.Print()
    print(lik.GetLength())
