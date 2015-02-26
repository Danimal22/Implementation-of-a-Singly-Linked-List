class Node():
    def __init__(self, data):
        self.data = data
        self.nextel = None

class Stack(Node):
    def __init__(self, head = None):
        self.head = head


# (data, stack) -> (stack)
    def push(self, data):
        """
        If data is empty and the stack is empty, return None.
        If data is None and the stack isn't empty, return the
        data that stack points to.
        Else wrap data in node and reassign as head node.

        """
        currNode = Node(data)
        if self.head == None and currNode:
            self.head = currNode
            return self.head
        if self.head == None and currNode.data == None:
            return None
        else:
            currNode.nextel = self.head
            self.head = currNode
            return self.head
# (stack) -> (data)
    def pop(self):
        """
        If stack object isn't empty, return node from head of
        stack, reassign stack head pointer and return.
        Else, return None.

        """
        popNode = self.head
        if self.head == None:
            return None
        else:
            self.head = popNode.nextel
            popNode.nextel = None
            return popNode.data

# List[Int] -> List[Int]
def reverse(a):
    stack = Stack()
    revList = []
    for e in a:
        elt = Node(e)
        stack.push(elt)
    while stack.head != None:
        l = stack.pop().data
        revList.append(l)
    return revList

def test():
    a = range(15)
    print(a)
    print(reverse(a))

if __name__ == "__main__":
    test()
