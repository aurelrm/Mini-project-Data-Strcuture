import random as rd 


class Node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insertBinaryTree(self,data): 
        q = []  
        q.append(self)  
        while (len(q)):  
            self = q[0]  
            q.pop(0)  
            if (not self.left): 
                self.left = Node(data)  
                break
            else: 
                q.append(self.left)  
    
            if (not self.right): 
                self.right = Node(data)  
                break
            else: 
                q.append(self.right) 

    def insertAVL(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insertAVL(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insertAVL(data)
        else:
            self.data = data

    def printTreePreOrder(self,root):
        if root:
            print(root.data)
            
            self.printTreePreOrder(root.left)
            self.printTreePreOrder(root.right)
    
    def searchAVL(self,data):
        if self.data:
            if data == self.data:
                return True
            if data < self.data:
                if self.left is None:
                    return False
                else:
                    self.left.searchAVL(data)
            elif data > self.data:
                if self.right is None:
                    return False
                else:
                    self.right.searchAVL(data)
        else:
            return False

    def searchBinaryTree(self,root,data):
        if root:
            print(root.data)
            if root.self.data == data or root.self.right == data:
                return True
            self.searchBinaryTree(root.left,data)
            self.searchBinaryTree(root.right,data)
        


def init_liste():
    liste= []
    while len(liste) < 50:
        n = rd.randint(1,200)
        if n not in liste:
            liste.append(n) 
    return liste

def init_BinaryTree(liste):
    root_BinaryTree = Node(liste[0])
    for each in range(1,len(liste)):
        root_BinaryTree.insertBinaryTree(liste[each])
    return root_BinaryTree

def init_AVL(liste):
    root_AVL = Node(liste[0])
    for each in range(1,len(liste)):
        root_AVL.insertAVL(liste[each])
    return root_AVL

def exo4():
    liste = init_liste()
    print("Nous initialisons la liste")
    print(liste)
    print("Nous initialisons un 'Level order Binary Tree'")
    root_BinaryTree = init_BinaryTree(liste)
    print("Nous initialisons un AVL")
    root_AVL = init_AVL(liste)
    print("Nous imprimons les deux tree avec un parcourt 'Pre-Order'")
    root_BinaryTree.printTreePreOrder(root_BinaryTree)
    print()
    root_AVL.printTreePreOrder(root_AVL)

if __name__ == "__main__":
    exo4()
    input("Appuyer sur une touche pour quitter...")
    


