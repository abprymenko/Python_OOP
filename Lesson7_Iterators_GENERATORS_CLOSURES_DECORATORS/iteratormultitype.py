class MultiTypeIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        try:
            if self.index < len(self.iterable):
                current_item = self.iterable[self.index]
                self.index += 1
                return self.__GetValue(current_item)
            raise StopIteration
        except ValueError as ve:
            raise ve
        except StopIteration as si:
            raise si
    def __GetValue(self, item:object):
        try:
            if isinstance(item, str):
                return f"String: {item}"
            elif isinstance(item, int):
                return f"Integer: {item}"
            elif isinstance(item, float):
                return f"Float: {item}"
            else:
                raise ValueError(f"Unsupported type: {type(item)}")
        except ValueError as ve:
            raise ve


if __name__ == "__main__":
    try:
        data = [1, "two", 3.0, "four", 5, 6.5]#, [True]]#=> Unsupported type: <class 'list'>
        multi_type_iterator = MultiTypeIterator(data)
        #AttributeError: 'MultiTypeIterator' object has no attribute '__GetValue'
        #multi_type_iterator.__GetValue(10)
        for item in multi_type_iterator:
            print(item)
    except Exception as ex:
        print(ex)
