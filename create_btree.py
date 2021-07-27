import random

class Node(object):
    def __init__(self,value):
        self._value = value
        self._l_node = None
        self._r_node = None

    @property
    def data(self):
        return self._value
    
    @data.setter
    def data(self,value):
        self._value = value

    @property 
    def left_node(self):
        return self._l_node

    @left_node.setter
    def left_node(self,value):
        self._l_node = value

    @property
    def right_node(self):
        return self._r_node

    @right_node.setter
    def right_node(self,value):
        self._r_node = value


class BinaryTree(object):
    def __init__(self):
        self._root_node = None

    def insert_node(self,num_list):
        if not num_list:
            return None

        index = int(len(num_list)/2)
        node = Node(num_list[index])
        if not self._root_node:
            self._root_node = node
        
        node.left_node = self.insert_node(num_list[:index])
        node.right_node = self.insert_node(num_list[index+1:])
        return node

    @property
    def root_node(self):
        return self._root_node

    def print_tree(self,node):
        if not node:
            return
        temp = node
        print('root node = ',temp.data)
        if temp.left_node:
            print('left node = {}\t'.format(temp.left_node.data),end = '')
        else:
            print('left node = None')
        if temp.right_node:
            print('right node = ',temp.right_node.data)
        else:
            print('right node = None')
        self.print_tree(temp.left_node)
        self.print_tree(temp.right_node)

    def print_pre_order(self,node):
        if not node:
            return None
        print('node value = ',node.data)
        self.print_pre_order(node.left_node)
        self.print_pre_order(node.right_node)

    def print_in_order(self,node):
        if not node:
            return None
        self.print_in_order(node.left_node)
        print('node value = ', node.data)
        self.print_in_order(node.right_node)

    def print_post_order(self,node):
        if not node:
            return None
        self.print_post_order(node.left_node)
        self.print_post_order(node.right_node)
        print('node value = ',node.data)



def main():
    num_list = sorted(random.sample(range(100),10))
    print("current list = ", num_list)
    btree = BinaryTree()
    btree.insert_node(num_list)
    #btree.print_tree(btree.root_node)
    btree.print_pre_order(btree.root_node)
    btree.print_in_order(btree.root_node)
    btree.print_post_order(btree.root_node)


if __name__ == '__main__':
    main()         

        