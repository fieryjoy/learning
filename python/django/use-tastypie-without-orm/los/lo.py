class LO(object):
    def __init__(self):
        self.pk = None
        self.title = None
        self.description = None
        self.url = None

    def __repr__(self):
        return "<%s:'%s' at 0x%x>" % (type(self).__name__, self.title, id(self))

    def is_valid(self):
        return True

    def get_data(self):
        return self.__dict__


def data_for_test():
    data = []
    for i in xrange(1000):
        lo = LO()
        lo.pk = i
        lo.title = "Hello%s" % i
        data.append(lo)
    return data

DATA = data_for_test()
