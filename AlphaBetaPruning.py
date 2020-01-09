class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid
      self.value = None
      self.alpha = None
      self.beta = None


    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.value = value
    def getNodeValue(self):
        return self.value

    def setAlphaValue(self,value):
        self.alpha = value
    def getAlphaValue(self):
        return self.alpha

    def setBetaValue(self,value):
        self.beta = value
    def getBetaValue(self):
        return self.beta

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

def alphabeta(node, maxturn, alpha, beta):
    if node != None:
        if maxturn:
            if not leafnode(node):
                node.setAlphaValue(alpha)
                node.setBetaValue(beta)
                alphabeta(node.getLeftChild(), False, node.getAlphaValue(), node.getBetaValue())
                leftchild = node.getLeftChild()
                leftchildalpha = leftchild.getAlphaValue()
                leftchildbeta = leftchild.getBetaValue()
                #print("Node: ", node.rootid, ' Alpha: ', node.getAlphaValue(), ' beta: ', node.getBetaValue())
                newalphavalue = max(node.getAlphaValue(), leftchildalpha, leftchildbeta)

                node.setAlphaValue(newalphavalue)

                if node.getAlphaValue() < node.getBetaValue():
                    alphabeta(node.getRightChild(), False, node.getAlphaValue(), node.getBetaValue())
                    rightchild = node.getRightChild()
                    #print("Node: ", node.rootid, ' Alpha: ', node.getAlphaValue(), ' beta: ', node.getBetaValue())
                    rightchildalpha = rightchild.getAlphaValue()
                    rightchildbeta = rightchild.getBetaValue()

                    newalphavalue = max(node.getAlphaValue(), rightchildalpha, rightchildbeta)

                    node.setAlphaValue(newalphavalue)
                else:
                    print('Pruning at ', node.rootid, '--', node.getRightChild().rootid)
                    # print('Pruning at Node: ', node.rootid, ' Alpha: ', node.getAlphaValue(), ' beta: ', node.getBetaValue())
                # print('Max Node: ', node.rootid, ' Alpha: ', node.getAlphaValue(), ' beta: ', node.getBetaValue())
            else:
                node.setAlphaValue(node.getNodeValue())
                node.setBetaValue(beta)
                #print('Max leaf Node: ',node.rootid, ' Alpha: ',node.getAlphaValue(), ' beta: ', node.getBetaValue())
        else:
            if not leafnode(node):
                node.setAlphaValue(alpha)
                node.setBetaValue(beta)
                alphabeta(node.getLeftChild(), True, node.getAlphaValue(), node.getBetaValue())
                leftchild = node.getLeftChild()
                #print("Node: ", node.rootid, ' Alpha: ', node.getAlphaValue(), ' beta: ', node.getBetaValue())
                leftchildalpha = leftchild.getAlphaValue()
                leftchildbeta = leftchild.getBetaValue()

                newbetavalue = min(node.getBetaValue(), leftchildalpha, leftchildbeta)

                node.setBetaValue(newbetavalue)
                if node.getAlphaValue() < node.getBetaValue():
                    alphabeta(node.getRightChild(), True, node.getAlphaValue(), node.getBetaValue())
                    rightchild = node.getRightChild()
                    #print("Node: ", node.rootid, ' Alpha: ', node.getAlphaValue(), ' beta: ', node.getBetaValue())
                    rightchildalpha = rightchild.getAlphaValue()
                    rightchildbeta = rightchild.getBetaValue()

                    newbetavalue = min(node.getBetaValue(), rightchildalpha, rightchildbeta)

                    node.setBetaValue(newbetavalue)
                else:
                    print('Pruning at ', node.rootid,'--',node.getRightChild().rootid)
                    # print('Pruning at node ', node.rootid, ' Alpha: ', node.getAlphaValue(), ' beta: ',
                    #       node.getBetaValue())
                #print('Min Node: ', node.rootid, ' Alpha: ', node.getAlphaValue(), ' beta: ', node.getBetaValue())
            else:
                node.setAlphaValue(alpha)
                node.setBetaValue(node.getNodeValue())
                #print('Min leaf Node: ', node.rootid, ' Alpha: ', node.getAlphaValue(), ' beta: ', node.getBetaValue())

def leafnode(node):
    leftchild = node.getLeftChild()
    rightchild = node.getRightChild()
    if leftchild == None and rightchild == None:
        return True
    else:
        return False

def printterminalvalue(root):
    print("Terminal value: ", root.getAlphaValue())

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


alphabeta(root, True, -1000, 1000)
printterminalvalue(root)
#printTree(root)
