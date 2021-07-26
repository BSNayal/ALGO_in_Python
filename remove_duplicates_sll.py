# We remove duplicates from a singly link list
import random
from sll_node import SLLNode

class RemDupSLL(object):
    def __init__(self):
        self._head=None

    def addNode(self, value):
        newNode = SLLNode(value)
        if not self._head:
            self._head=newNode
        else:
            tempNode = self._head
            while tempNode.next:
                tempNode = tempNode.next
            tempNode.next=newNode

    def printList(self):
        tempNode=self._head
        while(tempNode):
            print(" {} ".format(tempNode.value), end="")
            if tempNode.next:
                print(" -> ", end="")
            else:
                print("\n")
            tempNode = tempNode.next

    def remove_duplicates(self):
        tempNode = self._head
        while(tempNode):
            currNode = tempNode
            while(currNode.next):
                if tempNode.value==currNode.next.value:
                    currNode.next=currNode.next.next
                else:
                    currNode=currNode.next
            tempNode = tempNode.next

def main():
    num_list = list(range(10))
    num_list = random.choices(num_list, k=10)
    print("Initial list: {}".format(num_list))
    rem_dup_sll = RemDupSLL()
    for i in num_list:
        rem_dup_sll.addNode(i)

    print("Initial linked list:\n")
    rem_dup_sll.printList()

    print("List after removing duplicates:\n")
    rem_dup_sll.remove_duplicates()
    rem_dup_sll.printList()

if __name__=="__main__":
    main()