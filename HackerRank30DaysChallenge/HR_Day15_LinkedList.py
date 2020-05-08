class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # Complete this method
        #print(head,data)
        node = Node(data)
        if head == None:
            head = node
        else:
            curr = head
            while(curr.next != None):
                curr = curr.next
            curr.next = node
        return head




mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head);
