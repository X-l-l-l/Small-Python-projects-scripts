class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data

    @staticmethod
    def successor(node):
        current = node
        while(current.left is not None):
            current = current.left

        return current

    def delete(self, data):

        if self is None:
            return self

        if data < self.data:
            self.left = self.left.delete(data)
        elif(data > self.data):
            self.right = self.right.delete(data)
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            
            temp = self.successor(self.right)
            self.data = temp.data
            self.right = self.right.delete(temp.data)

        return self

    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()