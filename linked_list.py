class Slist:
    class _Node:
        def __init__(self,element):
            self.data=element
            self.next=None
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
    def is_empty(self):
        return self.count==0
    def length(self):
        return self.count
    def first(self):
        if not self.is_empty():
            return self.head.data
        else:
            return None
    def last(self):
        if not self.is_empty():
            return self.tail.data
        else:
            return None
    def add_first(self,val):
        new_node=self._Node(val)
        if not self.is_empty():
            new_node.next=self.head
            self.head=new_node
        else:
            self.head=self.tail=new_node
        self.count+=1
    def add_tail(self,val):
        new_tail=self._Node(val)
        if not self.is_empty():
            self.tail.next=new_tail
            self.tail=new_tail
        else:
            self.head=self.tail=new_tail
        self.count+=1
    def del_first(self):
        if not self.is_empty():
            data=self.head.data
            self.head=self.head.next
            if self.head is None:
                self.tail=None
            self.count-=1
            return data
    def del_last(self):
        if not self.is_empty():
            data=self.tail.data
            if self.count==1:
                self.head=self.tail=None
            else:
                last=self.tail
                cur=self.head
                while cur.next is not last:
                    cur=cur.next
                self.tail=cur
                self.tail.next=None
            self.count-=1
            return data
    def is_member(self,key):
        if not self.is_empty():
            cur=self.head
            while cur is not None:
                if cur.data==key:
                    break
                else:
                    cur=cur.next
            return cur!=None
    def maximum(self):
        if not self.is_empty():
            max_ele=self.head.data
            cur=self.head.next
            while cur is not None:
                if max_ele<cur.data:
                    max_ele=cur.data
                else:
                    cur=cur.next
            return max_ele
    def minimum(self):
        if not self.is_empty():
            min_ele=self.head.data
            cur=self.head.next
            while cur is not None:
                if min_ele>cur.data:
                    min_ele=cur.data
                else:
                    cur=cur.next
            return min_ele
    def add_after(self,element,key):     #element is the data after which key is to be added
        if not self.is_empty():
            cur=self.head
            while cur is not None:
                if cur.data==element:
                    new_node=self._Node(key)
                    new_node.next=cur.next
                    cur.next=new_node
                    self.count+=1
                    break
                else:
                    cur=cur.next
    def display(self):
        lst=[]
        if not self.is_empty():
            cur=self.head
            while cur is not None:
                lst.append(cur.data)
                cur=cur.next
            print lst
    def del_element(self,element):
        if not self.is_empty():
            cur=self.head
            while cur.next is not None:
                if cur.next.data==element:
                    cur.next=cur.next.next
                else:
                    cur=cur.next
            self.count-=1
    def reverse(self):
        if not self.is_empty():
            lst=[]
            while not self.is_empty():
                lst.append(self.del_last())
                print(lst)
            for i in range(len(lst)):
                self.add_tail(lst[i])
    
