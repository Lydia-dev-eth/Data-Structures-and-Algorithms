class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        new_node=Doubly_Linked_List_Node(x)

        if self.tail is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next= self.head
            self.head.prev= new_node
            self.head= new_node
            
    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        new_node=Doubly_Linked_List_Node(x)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next= new_node
            new_node.prev= self.tail
            self.tail= new_node

    def delete_first(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        if self.head is not None:
            x =self.head.item
            node=self.head.next
            if node is not None:
                self.head= node
                self.head.prev= None
            else:
                self.tail=None
                self.head=None
        return x

    def delete_last(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        if self.tail is not None:
            x= self.tail.item
            node=self.tail.prev
            if node is not None:
                self.tail=node
                self.tail.next=None
            else:
                self.tail=None
                self.head=None

        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        ###########################

        if x1==self.head and x2== self.tail:
            L2.head= x1
            self.head=None
            L2.tail= x2
            self.tail=None
        elif x1== self.head:
            L2.head= self.head
            self.head= x2.next
            self.head.prev= None
            L2.tail=x2
            L2.tail.next= None
        elif x2== self.tail:
            L2.head= x1
            self.tail= x1.prev
            self.tail.next=None
            L2.head.prev=None
            L2.tail=x2
        else:
            L2.head= x1
            L2.tail=x2
            x1.prev.next= x2.next
            x2.next.prev= x1.prev
            L2.head.prev=None
            L2.tail.next=None
        

        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################s
        if L2.head is None:
            return

        if x == self.tail:
            self.tail.next = L2.head
            L2.head.prev = self.tail

            self.tail = L2.tail
            self.tail.next = None
            L2.head = None
            L2.tail = None

        else:
            x.next.prev = L2.tail
            L2.tail.next = x.next
            L2.head.prev = x
            x.next = L2.head

            L2.head = None
            L2.tail = None