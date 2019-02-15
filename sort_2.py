class SortShape(object):
    def __init__(self):
        pass
    def sortShape(self,list):
        list.sort(key = lambda x: x.order)