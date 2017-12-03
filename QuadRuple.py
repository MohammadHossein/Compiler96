class QuadRuple:
    def __init__(self, op, arg1, arg2, result):
        self.op = op
        self.arg_one = arg1
        self.arg_two = arg2
        self.result = result

    def __str__(self):
        # return str([self.op,self.arg_one,self.arg_two,self.result])
        if 'goto' in self.result:
            if self.arg_two == '':
                return self.result
            return 'if ( ' + self.arg_one + ' ' + self.op + ' ' + self.arg_two + ' ) ' + self.result
        return self.result + ' = ' + self.arg_one + self.op + self.arg_two
