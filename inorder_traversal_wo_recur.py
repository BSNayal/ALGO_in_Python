from create_btree import BinaryTree
import random

def inorder(node):
    stack = []
    while True:
        if node:
            stack.append(node)
            node = node.left_node
        elif stack:
            node = stack.pop()
            print(" {} ".format(node.data), end='')
            node = node.right_node
        else:
            break

def main():
    num_list = list(range(10))
    random.shuffle(num_list)
    print("The initial list is : {} \n".format(num_list))
    bt = BinaryTree()
    bt.insert_node(num_list)
    root = bt.root_node
    bt.print_tree(root)

    print("\n Inorder traversal :\n")
    inorder(root)
    print('\n')
    

if __name__=="__main__":
    main()