class Entity:
    trueList = []
    falseList = []
    nextList = []
    type = None
    place = None
    quad = 0

    @staticmethod
    def backpatch(indexes,quad_list, target):
        print(quad_list, '-----------------------------------------')
        for index in indexes:
            quad_list[index].result += ' ' + str(target)

    def __str__(self):
        s = '++++++++\n'
        if self.trueList:
            s += 'trueList : ' + self.trueList.__str__() + '\n'
        if self.falseList:
            s += 'falseList : ' + self.falseList.__str__() + '\n'
        s += str(self.place)
        s += '\n+++++++'
        return s
