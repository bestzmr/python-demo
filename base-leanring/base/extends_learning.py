class Base(object):
    def __init__(self,base_id,name):
        self.base_id = base_id
        self.name = name
        print("I'm a Base object")


class Sub(Base):
    def __init__(self):
        # super().__init__(base_id, name)
        super(Sub, self).__init__(base_id=2,name='sub')
        print("I'm a Sub object")


if __name__ == '__main__':
    pass
