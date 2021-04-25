class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class Linked:
    def __init__(self):
        self.head = None

    def insert_at_begin(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data)
        itr.next = node

    def insert_at_mid(self,data):
        itr = self.head
        length = 0
        while itr:
            itr = itr.next
            length+=1
        if length%2==0:
            length = length//2
        else:
            length = (length+1)//2
        itr = self.head
        count = 0
        while itr:
            if count == length-1:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
            count+=1

    def insert_at(self,data,index):
        itr = self.head
        length = 0
        while itr:
            itr = itr.next
            length += 1
        if index == 0:
            node = Node(data,self.head)
            self.head = node
            return
        if index<0 or index>length:
            print('Invalid')
            return
        itr = self.head
        length = 0
        while itr:
            if index-1 == length:
                itr.next = Node(data,itr.next)
                break
            length+=1
            itr = itr.next

    def print(self):
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def delete(self,index):
        length = 0
        itr = self.head
        while itr:
            if index-1 == length:
                itr.next = itr.next.next
                break
            length+=1
            itr = itr.next

    def merge(self,ll,ll1):
        itr = ll
        while itr.next:
            itr = itr.next
        itr.next = ll1
    
    def merge_sorted(self,ll,ll1):
        dummy = Node(0)
        new = dummy
        while True:
            if ll is None:
                new.next = ll1
                break
            elif ll1 is None:
                new.next = ll
                break
            else:
                if ll.data<=ll1.data:
                    new.next = ll.next
                    ll = ll.next
                else:
                    new.next = ll1.next
                    ll1 = ll1.next
            new = new.next
        return dummy.next

ll = Linked()
ll1 = Linked()
l = Linked()
ll.insert_at_begin(1)
ll.insert_at_begin(2)
ll.insert_at_begin(3)
ll.insert_at_end(4)
ll.insert_at_end(5)
ll.insert_at_mid(6)
ll.insert_at(7,0)
ll.delete(3)
ll1.insert_at_begin(1)
ll1.insert_at_begin(2)
ll1.insert_at_begin(3)
l.head = ll.merge_sorted(ll.head,ll1.head)
l.print()
ll1.print()
ll.print()