class ToyStorage():
    def __init__(self):
        self.toy_list = []
        
    def add(self, toy):
        self.toy_list.append(toy)
        
    def see_toys(self):
        return self.toy_list