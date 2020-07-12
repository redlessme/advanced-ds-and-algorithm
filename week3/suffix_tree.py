class SuffixTree(object):
    class Node(object):
        def __init__(self, lab):
            self.lab = lab  # label on path leading to this node
            self.out = {}  # outgoing edges; maps characters to nodes

    def __init__(self, s):
        """ Make suffix tree, without suffix links, from s in quadratic time
            and linear space """
        s += '$'
        self.root = self.Node(None)
        self.root.out[s[0]] = self.Node(s)  # trie for just longest suf
        # add the rest of the suffixes, from longest to shortest
        for i in range(1, len(s)):
            # start at root; we’ll walk down as far as we can go
            cur = self.root
            j = i
            while j < len(s):
                if s[j] in cur.out:
                    child = cur.out[s[j]]
                    lab = child.lab
                    # Walk along edge until we exhaust edge label or
                    # until we mismatch
                    k = j + 1
                    while k - j < len(lab) and s[k] == lab[k - j]:
                        k += 1
                    if k - j == len(lab):
                        cur = child  # we exhausted the edge
                        j = k
                    else:
                        # we fell off in middle of edge
                        cExist, cNew = lab[k - j], s[k]
                        # create “mid”: new node bisecting edge
                        mid = self.Node(lab[:k - j])
                        mid.out[cNew] = self.Node(s[k:])
                        # original child becomes mid’s child
                        mid.out[cExist] = child
                        # original child’s label is curtailed
                        child.lab = lab[k - j:]
                        # mid becomes new child of original parent
                        cur.out[s[j]] = mid
                else:
                    # Fell off tree at a node: make new edge hanging off it
                    cur.out[s[j]] = self.Node(s[j:])

    def followPath(self, s):
        """ Follow path given by s.  If we fall off tree, return None.  If we
            finish mid-edge, return (node, offset) where 'node' is child and
            'offset' is label offset.  If we finish on a node, return (node,
            None). """
        cur = self.root
        i = 0
        while i < len(s):
            c = s[i]
            if c not in cur.out:
                return (None, None)  # fell off at a node
            child = cur.out[s[i]]
            lab = child.lab
            j = i + 1
            while j - i < len(lab) and j < len(s) and s[j] == lab[j - i]:
                j += 1
            if j - i == len(lab):
                cur = child  # exhausted edge
                i = j
            elif j == len(s):
                return (child, j - i)  # exhausted query string in middle of edge
            else:
                return (None, None)  # fell off in the middle of the edge
        return (cur, None)  # exhausted query string at internal node

    def hasSubstring(self, s):
        """ Return true iff s appears as a substring """
        node, off = self.followPath(s)
        return node is not None

    def hasSuffix(self, s):
        """ Return true iff s is a suffix """
        node, off = self.followPath(s)
        if node is None:
            return False  # fell off the tree
        if off is None:
            # finished on top of a node
            return '$' in node.out
        else:
            # finished at offset 'off' within an edge leading to 'node'
            return node.lab[off] == '$'
if __name__ == '__main__':
    stree = SuffixTree('apple')
    s=stree.root.out

