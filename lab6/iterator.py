class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __next__(self):
        if self.index < len(self.collection):
            cur = self.collection[self.index]
            self.index += 1
            return cur
        else:
            raise StopIteration

