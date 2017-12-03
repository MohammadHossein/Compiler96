class Entity:
    trueList = []
    falseList = []
    nextList = []
    type = None
    place = None
    quad = 0

    @staticmethod
    def backpatch(quad_list, target):
        for quad in quad_list:
            quad.arg_one = target

    def __str__(self):
        s = ''
        if self.trueList:
            s += 'trueList : ' + self.trueList.__str__()
        if self.falseList:
            s += 'falseList : ' + self.trueList.__str__()
        s += self.place
        return s
