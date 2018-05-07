"""
Rtree Module
"""


class node(object):
    """
    Node class, including location info MBR,
    level 0 means in low level,
    index is the index in the database,
    father is the parent node
    """

    def __init__(self, MBR=None, level=0, index=None, father=None):
        if (MBR == None):
            self.MBR = {'xmin': None, 'xmax': None, 'ymin': None, 'ymax': None}
        else:
            self.MBR = MBR
        self.level = level
        self.index = index
        self.father = father


class Rtree(object):
    """
    Rtree Node, including Location info MBR
    level is the number of levels
    m is the min entry number
    M is the max entry number
    father is the father node
    """

    def __init__(self, leaves=None, MBR=None, level=1, m=1, M=3, father=None):
        self.leaves = []
        if (MBR == None):
            self.MBR = {'xmin': None, 'xmax': None, 'ymin': None, 'ymax': None}
        else:
            self.MBR = MBR
        self.level = level
        self.m = m
        self.M = M
        self.father = father

    def ChooseLeaf(self, node):
        """
        Choose a node to insert.
        :param node:
        :return:
        """

        if self.level == node.level + 1:
            # if current node level is higher than the node we want to insert, we find the good point.
            return self
        else:
            # Or iter its child nodes, to find the node with min area.
            increment = [(i, space_increase(self.leaves[i].MBR, node.MBR)) for i in range(len(self.leaves))]
            res = min(increment, key=lambda x: x[1])
            return self.leaves[res[0]].ChooseLeaf(node)

    def SplitNode(self):
        """
        Split Node
        :return:
        """
        # if current node has no father node, it must need to produce a father node to contain 2 split node.
        if self.father == None:
            # Father point level is 1 larger then current node
            self.father = Rtree(level=self.level + 1, m=self.m, M=self.M)
            self.father.leaves.append(self)
        # Produce a new point, with same m, M, father
        leaf1 = Rtree(level=self.level, m=self.m, M=self.M, father=self.father)
        leaf2 = Rtree(level=self.level, m=self.m, M=self.M, father=self.father)

        # use PickSeeds for leaf1 and leaf2
        self.PickSeeds(leaf1, leaf2)

        # iter rest child nodes and insert
        while len(self.leaves) > 0:
            # if rest child node insert into one group to make number of nodes > m
            # just insert all, and adjust MBR
            if len(leaf1.leaves) > len(leaf2.leaves) and len(leaf2.leaves) + len(self.leaves) == self.m:
                for leaf in self.leaves:
                    leaf2.MBR = merge(leaf2.MBR, leaf.MBR)
                    leaf2.leaves.append(leaf)
                    leaf.father = leaf2
                self.leaves = []
                break
            if len(leaf2.leaves) > len(leaf1.leaves) and len(leaf1.leaves) + len(self.leaves) == self.m:
                for leaf in self.leaves:
                    leaf1.MBR = merge(leaf1.MBR, leaf.MBR)
                    leaf1.leaves.append(leaf)
                    leaf.father = leaf1
                self.leaves = []
                break

            # Or use pickNext to assign a next node to leaf1 and leaf2
            self.PickNext(leaf1, leaf2)

        # Current node's father node delete current node and add 2 new nodes and finish split
        self.father.leaves.remove(self)
        self.father.leaves.append(leaf1)
        self.father.leaves.append(leaf2)
        self.father.MBR = merge(self.father.MBR, leaf1.MBR)
        self.father.MBR = merge(self.father.MBR, leaf2.MBR)

    def PickSeeds(self, leaf1, leaf2):
        """
        Assign child node for 2 group
        :param leaf1:
        :param leaf2:
        :return:
        """
        d = 0
        t1 = 0
        t2 = 0

        # iter all possible children nodes, to find the max difference.
        for i in range(len(self.leaves)):
            for j in range(i + 1, len(self.leaves)):
                MBR_new = merge(self.leaves[i].MBR, self.leaves[j].MBR)
                S_new = 1.0 * (MBR_new['xmax'] - MBR_new['xmin']) * (MBR_new['ymax'] - MBR_new['ymin'])
                S1 = 1.0 * (self.leaves[i].MBR['xmax'] - self.leaves[i].MBR['xmin']) * (
                        self.leaves[i].MBR['ymax'] - self.leaves[i].MBR['ymin'])
                S2 = 1.0 * (self.leaves[j].MBR['xmax'] - self.leaves[j].MBR['xmin']) * (
                        self.leaves[j].MBR['ymax'] - self.leaves[j].MBR['ymin'])
                if S_new - S1 - S2 > d:
                    t1 = i
                    t2 = j
                    d = S_new - S1 - S2
        n2 = self.leaves.pop(t2)
        n2.father = leaf1
        leaf1.leaves.append(n2)
        leaf1.MBR = leaf1.leaves[0].MBR
        n1 = self.leaves.pop(t1)
        n1.father = leaf2
        leaf2.leaves.append(n1)
        leaf2.MBR = leaf2.leaves[0].MBR

    def PickNext(self, leaf1, leaf2):
        """
        Assign 1 node fro 2 groups
        :param leaf1:
        :param leaf2:
        :return:
        """
        d = 0
        t = 0

        # iter child nodes to find the node with max difference add after inserting 2 nodes
        for i in range(len(self.leaves)):
            d1 = space_increase(merge(leaf1.MBR, self.leaves[i].MBR), leaf1.MBR)
            d2 = space_increase(merge(leaf2.MBR, self.leaves[i].MBR), leaf2.MBR)
            if abs(d1 - d2) > abs(d):
                d = d1 - d2
                t = i
        if d > 0:
            target = self.leaves.pop(t)
            leaf2.MBR = merge(leaf2.MBR, target.MBR)
            target.father = leaf2
            leaf2.leaves.append(target)
        else:
            target = self.leaves.pop(t)
            leaf1.MBR = merge(leaf1.MBR, target.MBR)
            target.father = leaf1
            leaf1.leaves.append(target)

    def AdjustTree(self):
        """
        Adjust tree from button to up
        :return:
        """
        p = self
        while p != None:
            # If current node's leaves number is more than M, just split and adjust father node MBR
            if len(p.leaves) > p.M:
                p.SplitNode()
            else:
                # Or just adjust father point MBR
                if p.father != None:
                    p.father.MBR = merge(p.father.MBR, p.MBR)
            p = p.father

    def Search(self, MBR):
        """
        Search a rectangle range with MBR
        :param MBR:
        :return:
        """
        result = []
        # If current is leaf node, just add nodes to result
        if self.level == 1:
            for leaf in self.leaves:
                if intersect(MBR, leaf.MBR):
                    result.append(leaf.index)
            return result
        # Or search with the child node, add result.
        else:
            for leaf in self.leaves:
                if intersect(MBR, leaf.MBR):
                    result = result + leaf.Search(MBR)
            return result

    def FindLeaf(self, node):
        """
        Find a certain Node
        :param node:
        :return:
        """
        result = []
        # If current node is not leaf node, just iter to find all the node with MBR
        if self.level != 1:
            for leaf in self.leaves:
                if contain(leaf.MBR, node.MBR):
                    result.append(leaf.FindLeaf(node))
            for x in result:
                if x != None:
                    return x
        # If current node is leaf, just iter this node to check whether index is same, and return
        else:
            for leaf in self.leaves:
                if leaf.index == node.index:
                    return self

    def CondenseTree(self):
        """
        Condense the tree
        :return:
        """

        # Q is used to store the nodes to be inserted.
        Q = []
        p = self
        q = self
        while p != None:
            p.MBR = {'xmin': None, 'xmax': None, 'ymin': None, 'ymax': None}

            for leaf in p.leaves:
                p.MBR = merge(p.MBR, leaf.MBR)

            if len(p.leaves) < self.m and p.father != None:
                p.father.leaves.remove(p)
                if len(p.leaves) != 0:
                    Q = Q + p.leaves
            q = p
            p = p.father

        for node in Q:
            q = Insert(q, node)

    def CondenseRoot(self):
        """
        Condense the root node
        :return:
        """
        p = self
        q = p
        while len(p.leaves) == 1 and p.father == None and p.level != 1:
            p = p.leaves[0]
            q.leaves = []
            p.father = None
            q = p
        return p


def Insert(root, node):
    """
    Insert a new root, return updated root node.
    :param root:
    :param node:
    :return:
    """
    target = root.ChooseLeaf(node)
    node.father = target
    target.leaves.append(node)
    target.MBR = merge(target.MBR, node.MBR)
    target.AdjustTree()
    if root.father != None:
        root = root.father
    return root


def Delete(root, node):
    """
    Delete a node, return update root node
    :param root:
    :param node:
    :return:
    """
    target = root.FindLeaf(node)
    if target == None:
        # print 'no result'
        print("no result")
        return root
    target.leaves.remove(node)
    target.CondenseTree()
    root = root.CondenseRoot()
    return root


def merge(MBR1, MBR2):
    """
    Merge 2 MBRs
    :param MBR1:
    :param MBR2:
    :return:
    """
    if MBR1['xmin'] == None:
        return MBR2
    if MBR2['xmin'] == None:
        return MBR1
    MBR = {}
    MBR['xmin'] = min(MBR1['xmin'], MBR2['xmin'])
    MBR['ymin'] = min(MBR1['ymin'], MBR2['ymin'])
    MBR['xmax'] = max(MBR1['xmax'], MBR2['xmax'])
    MBR['ymax'] = max(MBR1['ymax'], MBR2['ymax'])
    return MBR


def space_increase(MBR1, MBR2):
    """
    Calculate area add difference of MBR1 after MBR1 combine with MBR2
    :param MBR1:
    :param MBR2:
    :return:
    """
    xmin = min(MBR1['xmin'], MBR2['xmin'])
    ymin = min(MBR1['ymin'], MBR2['ymin'])
    xmax = max(MBR1['xmax'], MBR2['xmax'])
    ymax = max(MBR1['ymax'], MBR2['ymax'])
    return 1.0 * ((xmax - xmin) * (ymax - ymin) - (MBR1['xmax'] - MBR1['xmin']) * (MBR1['ymax'] - MBR1['ymin']))


def intersect(MBR1, MBR2):
    """
    heck whether MBR1 and MBR2 intersect with each other
    :param MBR1:
    :param MBR2:
    :return:
    """
    if MBR1['xmin'] > MBR2['xmax'] or MBR1['xmax'] < MBR2['xmin'] or MBR1['ymin'] > MBR2['ymax'] or MBR1['ymax'] < MBR2[
        'ymin']:
        return 0
    return 1


def contain(MBR1, MBR2):
    """
    check whether MBR1 contains MBR2
    :param MBR1:
    :param MBR2:
    :return:
    """
    return (MBR1['xmax'] >= MBR2['xmax'] and MBR1['xmin'] <= MBR2['xmin'] and MBR1['ymax'] >= MBR2['ymax'] and MBR1[
        'ymin'] <= MBR2['ymin'])
