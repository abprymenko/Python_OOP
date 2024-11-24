class Generator:
    def __init__(self, items:list):
        self.Items:list = items

    def __getitem__(self, index):
        if index < 0 or index >= len(self.Items):
            raise IndexError(f'Index - {index} out of range.')
        return self.Items[index]

    def __iter__(self):
        for item in self.Items:
            yield item
