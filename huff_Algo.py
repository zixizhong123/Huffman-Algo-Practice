'''
    Project Name: Huffman Algorithm Practics
    Name: Zixi Zhong
    Purpose: This program recursively constructs a tree based
    off its preorder and inorder traversals, prints out the
    postorder sequence of the tree, and then decodes
    a sequence of values consisting of 0s and 1s with the
    constructed tree.
'''

import sys


class BinaryTree:
    def __init__(self, value):
        '''
            This class represents a Binary Tree.
            Parameters: self
                        value - an integer value representing
                                the root
            Returns: none, sets value to self._value, self._lchild,
                     and self._rchild
            Pre-condition: The preorder and inorder traversals must be
                           in the process of being traversed over in order
                           to recursively build the binary tree made of
                           smaller binary trees
            Post-condition: The BinaryTree object will have a root (value)
                            and left and right children set to None, and
                            finally be updated later with values depending
                            on the preorder and inorder traversals, until
                            the tree is fully constructed
        '''
        self._value = value
        self._lchild = None
        self._rchild = None


    def set_left(self, target):
        '''
            This method sets target to self._lchild.
            Parameters: self, target
            Returns: None
        '''
        self._lchild = target


    def set_right(self, target):
        '''
            This method sets target to self._rchild.
            Parameters: self, target
            Returns: None
        '''
        self._rchild = target


    def get_val(self):
        '''
            This method returns self._value.
            Parameters: self
            Returns: self._value
        '''
        return self._value


    def get_left(self):
        '''
            This method returns self._lchild.
            Parameters: self
            Returns: self._lchild
        '''
        return self._lchild


    def get_right(self):
        '''
            This method returns self._rchild.
            Parameters: self
            Returns: self._rchild
        '''
        return self._rchild


    def __str__(self):
        '''
            This method formats the BinaryTree object to be
            easily printed wth it's left and right children.
            Parameters: self
            Returns: printable format for BinaryTree
        '''
        if self._value == None:
            return "None"
        return ("({} {} {})".format(self._value, str(self._lchild),
                                    str(self._rchild)))



def read_file():
    """
        Reads in the file and splits it into lists of integers
        for preorder traversal, inorder traversal, and an
        encoded sequence of values.
        Returns: a list of the preorder traversal of the decoding
                 tree, a list of the inorder traversal of the decoding
                 tree, and th encoded sequence of values.
        Pre-condition: none
        Post-condition: Files will be read and split for
                        the rest of the program to process.
    """

    file = input("Input file: ")

    try:
        pfile = open(file)
    except:  # Checks if the file can be opened
        print("ERROR: Could not open file " + file)
        sys.exit()

    pfile = pfile.readlines()

    preorder = pfile[0].split()
    inorder = pfile[1].split()
    encode = pfile[2].strip()

    return preorder, inorder, encode



def build_tree(preorder, inorder):
    """
        Takes in the preorder and inorder traversal lists and builds the
        tree recursively using these lists.
        Parameters: preorder traversal lists, and inorder traversal lists
        Returns: the fully constructed tree
        Pre-condition: preorder and inorder lists must be processed and
                       sent into the function to be broken up and built
        Post-condition: the tree will be fully constructed.
    """

    # Base case
    if preorder == [] or inorder == []:
        return

    root = preorder[0]

    # Breaks the lists by root, left side, and right side
    in_index = inorder.index(root)
    in_left = inorder[:in_index]
    in_right = inorder[in_index + 1:]
    pre_left = preorder[1 : len(in_left) + 1]
    pre_right = preorder[len(in_left) + 1 :]

    # Recursively creates smaller binary trees to make a big binary tree
    tree = BinaryTree(root)
    tree.set_left(build_tree(pre_left, in_left))
    tree.set_right(build_tree(pre_right, in_right))

    return tree



def postorder_traversal(tree):
    """
        Takes in the fully constructed tree and creates a string
        of the tree in the postorder traversal to be printed in
        main().
        Parameters: the fully constructed tree
        Returns: a string of the tree traversed in postorder
        Pre-condition: tree must be fully constructed using the
                       preorder and inorder lists
        Post-condition: The tree will be traversed in post order
                        and create a string in that order
    """
    post = '' # Handles the spaces between the postorder traversal
              # in the string

    # To make sure the function doesn't move on if it doesn't have
    # a left child, so it doesn't add to string if it is None
    if tree.get_left() != None:
        post += postorder_traversal(tree.get_left()) + ' '

    # To make sure the function doesn't move on if it doesn't have
    # a right child, so it doesn't add to string if it is None
    if tree.get_right() != None:
        post += postorder_traversal(tree.get_right()) + ' '

    # Prints the current value (this is all recursed in postorder)
    post += str(tree.get_val())

    return post



def decode(tree, encode):
    """
        Takes in the fully constructed tree and an encoded
        sequence of values, and uses the tree to decode the
        sequence. If the number is 0, it traverses the tree
        to the left, if it is 1, it traverses the tree to
        the right. It only prints out the values at leaf nodes
        and then goes back to the top of the tree and repeats
        until the end of the sequence.
        Parameters: the fully constructed tree, the encode
                    sequence
        Returns: none, prints the decoded sequence
        Pre-condition: tree must be fully constructed using the
                       preorder and inorder lists, and the
                       encoded sequence must be processed
        Post-condition: The encoded sequence will be decoded
    """

    root = tree

    for i in range(len(encode)):

        # If the current number is 0, go to left child
        if int(encode[i]) == 0:
            if root.get_left() == None and root.get_right() == None:
                print(root.get_val(), end="")
                root = tree

            else:
                root = root.get_left()

        # If the current number is 1, go to right child
        else:
            root = root.get_right()

        # If current node is a leaf, print it and go back to the
        # root of the tree
        if root.get_left() == None and root.get_right() == None:
            print(root.get_val(), end="")
            root = tree
    
    '''root = tree
    for i in range(len(encode)):
        # If the current number is 0, go to left child
        if int(encode[i]) == 0:
            root = root.get_left()
        # If the current number is 1, go to right child
        else:
            root = root.get_right()
        # If current node is a leaf, print it and go back to the
        # root of the tree
        if root.get_left() == None and root.get_right() == None:
            print(root.get_val(), end="")
            root = tree'''



def print_val(tree):
    """
        A function used for checking and debugging the tree.
        Parameters: the fully constructed tree
        Returns: none
        Pre-condition: tree must be fully constructed using the
                       preorder and inorder lists
        Post-condition: The current state of the tree will be
                        printed
    """
    if tree == None:
        return

    # Prints the inorder sequence of the tree
    print_val(tree.get_left())
    print(tree)
    print_val(tree.get_right())



def main():
    '''
        This function reads in the preorder and inorder sequences,
        and an encoded sequence. It uses the preorder and inorder
        sequences to recursively construct a tree and prints out
        the postorder sequence of that tree. It then decodes
        a sequence of values consisting of 0s and 1s with the
        constructed tree.
        Parameters: None
        Returns: None
        Pre-condition: none
        Post-condition: files will be processed, the tree will be
                        fully constructed with the preorder and
                        inorder seqences, the postorder sequence
                        will be printed, and the decoded sequence
                        will also be printed.
        .
    '''
    preorder, inorder, encode = read_file()

    tree = build_tree(preorder, inorder)
    post = postorder_traversal(tree)
    post = post.strip()
    print(post)

    decode(tree, encode)
    print()


main()