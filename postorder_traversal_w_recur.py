from create_btree import BinaryTree
import random

def postorder(node):
    if not node:
        return
    postorder(node.left_node)
    postorder(node.right_node)
    print(" {}".format(node.data), end='')

def main():
    num_list = list(range(10))
    random.shuffle(num_list)
    print("The initial list is : {} \n".format(num_list))
    bt = BinaryTree()
    bt.insert_node(num_list)
    root = bt.root_node
    bt.print_tree(root)

    print("\n Inorder traversal :\n")
    postorder(root)
    print('\n')
    

if __name__=="__main__":
    main()