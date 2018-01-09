class QuadRuple:
    def __init__(self, op, arg1, arg2, result):
        self.op = op
        self.arg_one = arg1
        self.arg_two = arg2
        self.result = result
        self.toEnglish = {
            '۱': '1',
            '۲': '2',
            '۳': '3',
            '۴': '4',
            '۵': '5',
            '۶': '6',
            '۷': '7',
            '۸': '8',
            '۹': '9',
            '۰': '0',
        }

    def __str__(self):
        result = self.result
        if self.arg_two is not None:
            for char in self.arg_two:
                if char in self.toEnglish.keys():
                    self.arg_two = self.arg_two.replace(char, self.toEnglish[char])
        else:
            self.arg_two = 'None'
        if self.arg_one is not None:
            for char in self.arg_one:
                if char in self.toEnglish.keys():
                    self.arg_one = self.arg_one.replace(char, self.toEnglish[char])
        else:
            self.arg_one = 'None'

        op = self.op
        if 'goto' in result:
            if self.arg_two == '':
                return result
            return 'if ( ' + self.arg_one + ' ' + op + ' ' + self.arg_two + ' ) ' + result
        elif op == 'label':
            return self.result + ':'
        elif op == 'setjmp':
            return self.result + ' = setjmp(' + self.arg_one + ')'
        elif result == 'longjmp':
            return 'longjmp(' + self.arg_one + ',' + self.arg_two + ')'
        elif op == 'rand':
            return result + ' = rand(' + self.arg_one + ')'
        elif op == '=[]':
            return result + ' = ' + self.arg_one + '[' + self.arg_two + ']'
        elif op == '' and self.arg_one == '' and self.arg_two == '' and self.result == '':
            return ''
        return result + ' = ' + self.arg_one + op + self.arg_two
