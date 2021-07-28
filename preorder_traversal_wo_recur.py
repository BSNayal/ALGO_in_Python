from create_btree import BinaryTree
import random

def preorder(node):
    stack = [node]
    while(stack):
        curr = stack.pop()
        print(" {}".format(curr.data), end='')
        if curr.right_node:
            stack.append(curr.right_node)
        if curr.left_node:
            stack.append(curr.left_node)

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