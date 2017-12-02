class QuadRuple:
    def __init__(self, op, arg1, arg2, result):
        self.op = op
        self.arg_one = arg1
        self.arg_two = arg2
        self.result = result

    def __str__(self):
        return 'op : ' + self.op + '\n' + \
               'arg1 : ' + self.arg_one + '\n' + \
               'arg2 : ' + self.arg_two + '\n' + \
               'result : ' + self.result + '\n'
