class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def addNode(self,data):
        newnode=node(data)
        if self.head == None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
    def main(self):
        curr=self.head
        while curr:
            print(curr.data,end='->' if curr.next else '\n')
            curr=curr.next
    def reverse(self):
        prv=None
        curr=self.head
        while curr is not None:
            next_node=curr.next
            curr.next=prv
            prv=curr
            curr=next_node
        self.head=prv

o=linkedlist()
o.addNode(10)
o.addNode(20)
o.addNode(30)
o.addNode(40)
o.addNode(50)
o.reverse()
o.main()