class Student(object):
    __slots__ = ('name', 'age',)


class GraduateStudent(Student):
    __slots__ = ('sex', 'id',)


class Screen(object):
    @property
    def width(self):
        return self.twidth

    @property
    def height(self):
        return self.theight

    @width.setter
    def width(self, value):
        self.twidth = value

    @height.setter
    def height(self, value):
        self.theight = value

    @property
    def resolution(self):
        return self.theight * self.twidth


if __name__ == '__main__':
    # gs = GraduateStudent()
    # gs.name = 'merlin'
    # gs.age = '12'
    # gs.sex = '男'
    # gs.id = '123'
    # print(gs.name)
    # print(gs.age)
    # print(gs.sex)
    # print(gs.id)
    s = Screen()
    s.height = 2
    s.width = 5
    print(s.resolution)
