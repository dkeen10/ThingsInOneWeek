"""
4.1 Tree Representation
Difficulty: ★★☆☆☆

The first step is to parse the regex into a syntax tree. There are many challenges in this list that can teach you about parsing, especially the infix calculator challenge.

The resulting tree should have 4 types of nodes:

Alternation.
Concatenation.
Repetition.
Character.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(f' {self.data}', end=''),
        if self.right:
            self.right.printTree()

    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


def main():
    root = Node(10)
    root.insert(5)
    root.insert(15)
    root.insert(8)
    root.printTree()


if __name__ == "__main__":
    main()
