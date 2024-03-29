from create_btree import BinaryTree
import random

def preorder(node):
    if not node:
        return
    print(" {}".format(node.data), end='')
    preorder(node.left_node)
    preorder(node.right_node)

def main():
    num_list = list(range(10))
    random.shuffle(num_list)
    print("The initial list is : {} \n".format(num_list))
    bt = BinaryTree()
    bt.insert_node(num_list)
    root = bt.root_node
    bt.print_tree(root)

    print("\nPreorder traversal :\n")
    preorder(root)
    print('\n')
    

if __name__=="__main__":
    main()