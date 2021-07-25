class SLLNode(object):

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

