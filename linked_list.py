import random

class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None

    
    @property
    def data(self):
        return self.value

    @data.setter
    def data(self,value):
        try:
            if value:
                self.value = value
        except ValueError:
            print('Value not found')
            raise


class SLList(object):

    def __init__(self):
        self._head = None
        self._tail = None

    def addNode(self,value):
        node = Node(value)
        if not self._head:
            self._head = node
        else:
            self._tail.next = node
        self._tail = node

    def delNode(self,value):
        temp = self._head
        while temp:
            if temp.data == value:
                del_value  = self._head.next
                temp.data = temp.next.data
                temp.next = temp.next.next
                del del_value
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
    num = 7
    random.shuffle(num_list)
    print('Initial list = ',num_list)
    print('\n')
    list_obj = SLList()
    for value in num_list:
        list_obj.addNode(value)

    print('list before deleting\n')
    list_obj.printList()
    print('number to be deleted = \n',num)
    list_obj.delNode(num)
    print('list after deleting\n')
    list_obj.printList()

if __name__ == '__main__':
    main()

    