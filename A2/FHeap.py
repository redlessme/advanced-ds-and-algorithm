import math
def makeHeap():
    return Fib(0, 0)

class Node:
    def __init__(self, key,value):
        self.key = key  # distance
        self.value=value # label
        self.degree = 0  # number of child
        self.p = 0  # parent
        self.child = 0  # point to one child
        self.left = 0  # left sibling
        self.right = 0  # right sibling
        self.mark = False  # lost child if mark

    def print_node(self):
        if self.child != 0:
            c = self.child
            cl = c.left
            while True:
                print("%d has child: %d" % (self.key, c.key))
                c.printNode()
                if cl == c:
                    break
                c = c.right


class Fib:
    def __init__(self, n, minx):
        self.n = n
        self.min = minx

    def insert(self, key,value=None):
        node = Node(key,value)
        if self.min == 0:
            self.min = node
            node.left = node
            node.right = node
        else:
            node.right = self.min
            node.left = self.min.left
            node.left.right = node
            self.min.left = node
            if node.key < self.min.key:
                self.min = node
        self.n += 1
        return node

    def extract_min(self):
        z = self.min
        if z != 0:
            if z.child != 0:
                c = z.child
                while c.p != 0:
                    cpr = c.left
                    c.p = 0
                    c.left = 0
                    c.right = 0
                    c.left = self.min.left
                    c.right = self.min
                    self.min.left = c
                    c.left.right = c
                    c = cpr
            # delete z
            z.right.left = z.left
            z.left.right = z.right
            z.child = 0
            if z == z.right:
                self.min = 0
            else:
                self.min = z.right
                self.consolidate()
            self.n -= 1
        return z

    def link(self, y, x):  # make y become x's child
        y.right.left = y.left
        y.left.right = y.right
        y.p = x
        x.degree += 1
        y.mark = False
        if x.child == 0:
            x.child = y
            y.right = y
            y.left = y
        else:
            c = x.child
            y.right = c
            y.left = c.left
            c.left = y
            y.left.right = y

    def consolidate(self):
        A = []
        for i in range(0, int((math.log(self.n, 2) + 1))):
            A.append(0)
        current = self.min
        t = current.left
        while True:
            tmp = current.right
            x = current
            d = x.degree
            while A[d] != 0:  # while A[d] is  already occupied with a pointer
                y = A[d]
                if x.key > y.key:
                    x, y = y, x
                self.link(y, x)
                A[d] = 0
                d += 1
            # point x to  A[d] if A[d] is empty
            A[d] = x
            if current == t:  # has completed  one full cycle on the doubly linked list
                break
            # current=x.right
            current = tmp
        self.min = 0
        #  update self.min root list
        for i in range(len(A)):
            if A[i] != 0:
                if self.min == 0:  #
                    self.min = A[i]
                    A[i].left = A[i]
                    A[i].right = A[i]
                else:
                    A[i].right == self.min
                    A[i].left = self.min.left
                    A[i].left.right = A[i]
                    self.min.left = A[i]
                    if A[i].key < self.min.key:
                        self.min = A[i]

    def decrease_key(self, x, k):
        if k > x.key:
            return None
        x.key = k
        y = x.p
        if y != 0 and x.key < y.key:
            self.cut(x, y)
            self.cascading_cut(y)
        if x.key < self.min.key:
            self.min = x

    # if a child x is smaller than its parent y, cut the child off and bring it up to the root list
    def cut(self, x, y):
        if y.degree == 1:
            y.child = 0
            x.p = 0
        else:
            if x == y.child:
                w = x.right
                w.left = x.left
                x.left.right = x.right
                y.child = w
            else:
                w = x.right
                w.left = x.left
                x.left.right = x.right
        y.degree -= 1
        self.insert(x)
        self.n -= 1  # because it's not insert
        x.p = 0
        x.mark = False  # unmarked after promoting to the roor list

    def cascading_cut(self, y):  # continue cust the 'parent'
        z = y.p
        if z != 0:
            if z.mark is False:  # unmark means not lose child
                y.mark = True
            else:
                self.cut(y, z)
                self.cascading_cut(z)

    def delete(self, x):
        self.decrease_key(x, -math.inf)
        self.extract_min()

    def print_heap(self, key):
        pass
        root = self.min
        c = root
        print("min node and root node is: %d " % c.key)
        c.print_node()
        c = c.right
        while c != root:
            print("root node is :%d" % c.key)
            c.print_node()
            c = c.right



