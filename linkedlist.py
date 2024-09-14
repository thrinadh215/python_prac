class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def addNOde(self,data):
        newnode=node(data)
        if self.head == None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
    def main(self):
        while self.head:
            print(self.head.data, end=' ->' if self.head.next else '\n')
            self.head=self.head.next
        
o=linkedlist()
o.addNOde(10)
o.addNOde(20)
o.addNOde(30)
o.addNOde(40)
o.addNOde(50)
o.main()