class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class ll:
    def __init__(self):
        self.head = None

    def insert_at_begin(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    
    def insert_at_mid(self,data):
        if self.head is None:
            print('Linked list is empty')
            return
        ptr = self.head
        length = 0
        while ptr.next:
            ptr = ptr.next
            length+=1
        if length%2==0:
            length = length//2
        else:
            length = (length+1)//2
        ptr = self.head
        while length > 1:
            ptr  = ptr.next
            length-=1
        node = Node(data,None)
        node.next = ptr.next
        ptr.next = node

    def insert_at(self,data,x):
        if x<0 or x>self.get_length():
            print('Invalid')
            return
        if x==0:
            self.insert_at_begin(data)
        count = 0
        itr = self.head
        while itr:
            if count == x-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1


    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def delete(self,x):
        if x<0 or x>self.get_length():
            print('Invalid')
            return
        count = 0
        itr = self.head
        while itr:
            if count == x-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

linked = ll()
linked.insert_at_begin(12)
linked.insert_at_begin(21)
linked.insert_at_end(22)
linked.insert_at_mid(1)
linked.print()
linked.delete(1)
linked.print()
linked.insert_at(1,1)
linked.print()
p = linked.get_length()
print(p)