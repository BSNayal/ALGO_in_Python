#reverse a singly linked list
import random
from sll_node import SLLNode


class ReverseSLL(object):

    def __init__(self):
        self._head = None
        self._count = 0 #required only for the worst reverse logic O(n^2)

    def addNode(self, value):
        newNode = SLLNode(value)
        if not self._head:
            self._head = newNode
        else:
            tempNode = self._head
            while(tempNode.next):
                tempNode = tempNode.next
            tempNode.next = newNode
        self._count+=1
    
    def printList(self):
        temp = self._head
        while temp:
            print(" {} ".format(temp.value), end='')
            if temp.next:
                print("->", end='')
            else:
                print("\n")
            temp = temp.next

    def reverse(self):
        #for this we need to keep a count of the links during adding the node
        prev = None
        curr = self._head
        while curr:
            next = curr.next
            curr.next =  prev
            prev = curr
            curr = next
        self._head = prev  
            
def main():
    num_list = list(range(10))
    random.shuffle(num_list)
    print("The initial list is {} \n".format(num_list))
    reverse_sll = ReverseSLL()
    for i in num_list:
        reverse_sll.addNode(i)
    print("List before reversing is :\n")
    reverse_sll.printList()

    print("List after reversing: \n")
    reverse_sll.reverse()
    reverse_sll.printList()

    


if __name__ == '__main__':
    main()


