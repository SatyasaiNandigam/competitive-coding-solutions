class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    
    def Add_child(self,data):
        if data == self.data:
            return 

        if data < self.data:
            if self.left:
                self.left.Add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        
        if data > self.data:
            if self.right:
                self.right.Add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def In_order_Traversal(self):
        elements = []
        
        if self.left:
            elements +=  self.left.In_order_Traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.In_order_Traversal()

        return elements 


    def Pre_order_Traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.Pre_order_Traversal()

        if self.right:
            elements += self.right.Pre_order_Traversal()

        return elements


    def Post_order_Traversal(self):
        elements = []

        if self.left:
            elements += self.left.Post_order_Traversal()
        
        if self.right:
            elements += self.right.Post_order_Traversal()
        
        elements.append(self.data)

        return elements


    def search(self,val):
        if val == self.data:
            return True
        
        if val <self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data

    def calculate_sum(self):
        Sum = 0

        if self.left:
            Sum += self.left.calculate_sum()
        
        Sum += self.data

        if self.right:
            Sum += self.right.calculate_sum()
        
        return Sum

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self
            


def Build_Tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.Add_child(elements[i])
    return root


numbers = [17,4,1,20,9,23,18,34]
number_tree = Build_Tree(numbers)
# print(number_tree.In_order_Traversal())
# print(number_tree.Pre_order_Traversal())
# print(number_tree.Post_order_Traversal())
# print(number_tree.search(9))
# print(number_tree.search(100))
# print(number_tree.find_min())
# print(number_tree.find_max())
# print(number_tree.calculate_sum())

number_tree.delete(20)
print("After deleting 20 ",number_tree.In_order_Traversal())

number_tree = Build_Tree([17,4,1,20,9,23,18,34])
number_tree.delete(9)
print("After deleting 9",number_tree.In_order_Traversal())

number_tree = Build_Tree([17,4,1,20,9,23,18,34])
number_tree.delete(17)
print("After deleting 17",number_tree.In_order_Traversal())
