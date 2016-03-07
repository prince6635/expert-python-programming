def test_iterators():
    it = iter('abcde')
    for i in range(5):
        print(it.next())

class MyIterator(object):
    """Customized iterator"""
    def __init__(self, step):
        self.step = step
    def next(self):
        """Return the next element"""
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step
    def __iter__(self):
        """Return the iterator itself"""
        return self


if __name__ == '__main__':
    test_iterators()
    for it in MyIterator(5):
        print(it)
