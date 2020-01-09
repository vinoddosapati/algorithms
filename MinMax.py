class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid
      self.value = None

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.value = value
    def getNodeValue(self):
        return self.value

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree


def printTree(node):
        if node != None:
            printTree(node.getLeftChild())
            printTree(node.getRightChild())
            print(node.getNodeValue(), "-- ",node.rootid)

def minmax(node, maxturn):
    if node.value == None:
        if maxturn:
            maxvalue = max(minmax(node.getLeftChild(), False), minmax(node.getRightChild(), False))
            node.setNodeValue(maxvalue)
            return maxvalue
        else:
            minvalue = min(minmax(node.getLeftChild(), True), minmax(node.getRightChild(), True))
            node.setNodeValue(minvalue)
            return minvalue
    else:
        #print(node.value, ' -- ', node.rootid)
        return node.value

def minmaxpath(node, minmaxvalue, path):
    if node != None:
        if node.getNodeValue() == minmaxvalue:
            path.append(node.rootid)
            #print(node.rootid, ",")
            if leafnode(node) and node.getNodeValue() == minmaxvalue:
                return print("path: ", '->'.join(path), '\nTerminal node:', node.rootid, 'with Node Value: ', node.getNodeValue());
            minmaxpath(node.getLeftChild(), minmaxvalue,path)
            minmaxpath(node.getRightChild(), minmaxvalue, path)
            #return '->'.join(path)
    else:
        return path

def leafnode(node):
    leftchild = node.getLeftChild()
    rightchild = node.getRightChild()
    if leftchild == None and rightchild == None:
        return True
    else:
        return False

root = BinaryTree("root")
root.insertLeft("A1")
root.insertRight("A2")
A1 = root.getLeftChild()
A1.insertLeft("B1")
A1.insertRight("B2")
B1 = A1.getLeftChild()
B1.insertLeft("C1")
B1.insertRight("C2")
B2 = A1.getRightChild()
B2.insertLeft("C3")
B2.insertRight("C4")
C1 = B1.getLeftChild()
C1.insertLeft("D1")
D1 = C1.getLeftChild()
D1.setNodeValue(3)
C1.insertRight("D2")
D2 = C1.getRightChild()
D2.setNodeValue(10)
C2 = B1.getRightChild()
C2.insertLeft("D3")
D3 = C2.getLeftChild()
D3.setNodeValue(2)
C2.insertRight("D4")
D4 = C2.getRightChild()
D4.setNodeValue(9)
C3 = B2.getLeftChild()
C3.insertLeft("D5")
D5 = C3.getLeftChild()
D5.setNodeValue(10)
C3.insertRight("D6")
D6 = C3.getRightChild()
D6.setNodeValue(7)
C4 = B2.getRightChild()
C4.insertLeft("D7")
D7 = C4.getLeftChild()
D7.setNodeValue(5)
C4.insertRight("D8")
D8 = C4.getRightChild()
D8.setNodeValue(9)

A2 = root.getRightChild()
A2.insertLeft("B3")
A2.insertRight("B4")
B3 = A2.getLeftChild()
B3.insertLeft("C5")
B3.insertRight("C6")
B4 = A2.getRightChild()
B4.insertLeft("C7")
B4.insertRight("C8")
C5 = B3.getLeftChild()
C5.insertLeft("D9")
D9 = C5.getLeftChild()
D9.setNodeValue(2)
C5.insertRight("D10")
D10 = C5.getRightChild()
D10.setNodeValue(5)
C6 = B3.getRightChild()
C6.insertLeft("D11")
D11 = C6.getLeftChild()
D11.setNodeValue(6)
C6.insertRight("D12")
D12 = C6.getRightChild()
D12.setNodeValue(4)
C7 = B4.getLeftChild()
C7.insertLeft("D13")
D13 = C7.getLeftChild()
D13.setNodeValue(2)
C7.insertRight("D14")
D14 = C7.getRightChild()
D14.setNodeValue(7)
C8 = B4.getRightChild()
C8.insertLeft("D15")
D15 = C8.getLeftChild()
D15.setNodeValue(9)
C8.insertRight("D16")
D16 = C8.getRightChild()
D16.setNodeValue(1)

minmaxvalue = minmax(root, True)
print("MinMax value : ", minmaxvalue)
minmaxpath(root, minmaxvalue, [])

#printTree(root)
