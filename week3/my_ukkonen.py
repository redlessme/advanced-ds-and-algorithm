from operator import attrgetter
leafEnd = -1
class Node:
    def __init__(self,leaf):
        self.children = {}
        self.suffixIndex = None
        self.start = None
        self.end = None
        self.suffixLink = None
        self.leaf=leaf

    def __eq__(self, node):
        atg = attrgetter('start', 'end', 'suffixIndex')

        return atg(self) == atg(node)

    def __ne__(self, node):
        atg = attrgetter('start', 'end', 'suffixIndex')
        return atg(self) != atg(node)


    def __getattribute__(self, name):
        if name == 'end':
            if self.leaf:
                return leafEnd
        return super(Node, self).__getattribute__(name)

class SuffixTree:

    def __init__(self, data):
        """Initiate the tree."""
        self._string = data
        self.lastNewNode = None
        self.activeNode = None
        """activeEdge is represeted as input string character
          index (not the character itself)"""
        self.activeEdge = -1
        self.activeLength = 0
        # remainingSuffixCount tells how many suffixes yet to
        # be added in tree
        self.remaining= 0
        self.rootEnd = None
        self.splitEnd = None
        self.size = -1  # Length of input string
        self.root = None

    def edge_length(self, node):
        return node.end - node.start + 1

    def walk_down(self, current_node):
        """Walk down from current node.
        activePoint change for walk down (APCFWD) using
        Skip/Count Trick  (Trick 1). If activeLength is greater
        than current edge length, set next  internal node as
        activeNode and adjust activeEdge and activeLength
        accordingly to represent same activePoint.
        """
        length = self.edge_length(current_node)
        if (self.activeLength >= length):
            self.activeEdge += length
            self.activeLength -= length
            self.activeNode = current_node
            return True
        return False

    def new_node(self, start, end=None, leaf=False):
        """For root node, suffixLink will be set to NULL
        For internal nodes, suffixLink will be set to root
        by default in  current extension and may change in
        next extension"""
        node = Node(leaf)
        node.suffixLink = self.root
        node.start = start
        node.end = end
        """suffixIndex will be set to -1 by default and
           actual suffix index will be set later for leaves
           at the end of all phases"""
        node.suffixIndex = -1
        return node

    def extendSuffix(self,pos):
        # Extension rule1: it is a general case that all leaves have created should be extended by the  new 'pos'
        global leafEnd
        leafEnd=pos
        """it records how many suffix need to create"""
        self.remaining+=1
        """it means no internal node waits for suffix link reset """
        self.lastNewNode=None
        while self.remaining>0:
            if self.activeLength==0:# from root
                self.activeEdge=pos
            if self.activeNode.children.get(self._string[self.activeEdge]) is None:
                """Extension rule 2: a new leaf edge is created"""
                self.activeNode.children[self._string[self.activeEdge]]=self.new_node(pos,leaf=True)
                if self.lastNewNode is not None:
                    self.lastNewNode.suffixLink=self.activeNode

            else:
                 # get next node
                _next = self.activeNode.children.get(self._string[self.activeEdge])
                if self.walk_down(_next):  # Do walkdown
                    # Start from _next node (the new activeNode)
                    continue
                if (self._string[_next.start + self.activeLength] == self._string[pos]):
                    if ((self.lastNewNode is not None) and (self.activeNode != self.root)):
                        self.lastNewNode.suffixLink = self.activeNode
                        self.lastNewNode = None
                    # APCFER3
                    self.activeLength += 1
                    break
                self.splitEnd = _next.start + self.activeLength - 1

                #Extension 2:now it is not end at leaf and next character is not the character we  are processing
                # New internal node
                inter_node = self.new_node(_next.start, self.splitEnd)
                self.activeNode.children[self._string[self.activeEdge]] = inter_node
                inter_node.children[self._string[pos]] = self.new_node(pos, leaf=True)
                _next.start += self.activeLength
                inter_node.children[self._string[_next.start]] = _next
                #after  create a  new  inter-node, we check whether there is an iter-node created  in same  phase and last extension,
                #if it exists, linking from last inter-node to current inter-node
                if (self.lastNewNode is not None):
                    self.lastNewNode.suffixLink = inter_node
                self.lastNewNode = inter_node
            self.remaining -= 1
            if ((self.activeNode == self.root) and (self.activeLength > 0)):  # APCFER2C1
                self.activeLength -= 1
                self.activeEdge = pos - self.remaining + 1
            elif (self.activeNode != self.root):  # APCFER2C2
                self.activeNode = self.activeNode.suffixLink


    def buildSuffixTree(self):
        self.size=len(self._string)
        self.rootEnd=-1
        self.root=self.new_node(-1,self.rootEnd)
        self.activeNode=self.root

        for i in range(self.size):
            self.extendSuffix(i)
    def walk_dfs(self, current):
        start, end = current.start, current.end
        yield self._string[start: end + 1]

        for node in current.children.values():
            if node:
                yield from self.walk_dfs(node)
    def print_dfs(self):
        for sub in self.walk_dfs(self.root):
            print(sub)

if __name__ == '__main__':
    string='abcabxabcd$'
    s=SuffixTree(string)
    s.buildSuffixTree()

    #
    s.print_dfs()










