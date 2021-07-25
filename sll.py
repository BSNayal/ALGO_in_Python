import random
from sll_node import SLLNode
class SLList(object):

    def __init__(self):
        self._head = None

    def addNode(self,value):
        node = SLLNode(value)
        if not self._head:
            self._head = node
        else:
            temp = self._head
            while(temp.next):
                temp = temp.next
            temp.next = node

    def delNode(self,value):
        temp = self._head
        if self._head.value == value:
            self._head = self._head.next
            del temp
        else:
            prev = self._head
            while(temp):
                if temp.value == value:
                    prev.next = temp.next
                    del temp
                    break
                else:
                    prev = temp
                    temp = temp.next

    def printList(self):
        temp = self._head
        while temp:
            print(temp.data, end = '')
            if temp.next:
                print(' -> ', end = '')
            else:
                print('\n')
            temp = temp.next


def main():
    num_list = list(range(10))
    random.shuffle(num_list)
    print('Initial list = ',num_list)
    num=random.randint(0,10)
    print('\n')
    list_obj = SLList()
    for value in num_list:
        list_obj.addNode(value)

    print('list before deleting\n')
    list_obj.printList()
    print('number to be deleted = {}\n'.format(num))
    list_obj.delNode(num)
    print('list after deleting\n')
    list_obj.printList()

if __name__ == '__main__':
    main()

    