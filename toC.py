from os import system


class toC:
    def __init__(self, quadRuples=[], ids=[], temps={}):
        self.C = []
        self.quadRuples = quadRuples
        self.ids = {}
        ids.remove('اصلی')
        number = 1
        for id in ids:
            self.ids[id] = 'ID' + str(number)
            number += 1
        self.temps = temps

    def toC(self):
        pass

    def save(self):
        define = []
        with open('outFile.c', 'w') as output:
            output.write('#include<stdio.h>\n#include<stdlib.h>\n')
            output.write('int main(){\n')
            for quadRuple in self.quadRuples:
                code = ''
                if quadRuple.result in self.temps.keys():
                    if quadRuple.result not in define:
                        print('==========')
                        print(quadRuple)
                        print(self.temps[quadRuple.result])
                        code += self.temps[quadRuple.result] + ' ' + quadRuple.result + ';\n'
                    code += str(quadRuple) + ';\n'
                elif quadRuple.result in self.ids.keys():
                    quadRuple.result = self.ids[quadRuple.result]
                    code += str(quadRuple) + ';\n'
                elif 'goto' in quadRuple.result:
                    if quadRuple.arg_two == '':
                        code += quadRuple.result + ';\n'
                    else:
                        code += 'if ( ' + quadRuple.arg_one + ' ' + quadRuple.op + ' ' + quadRuple.arg_two + ' ) ' + quadRuple.result + ';\n'

                output.write(code)
            output.write('printf("Hello World!\\n");\n')
            output.write('return 0;\n')
            output.write('}')

    def run(self):
        # print('=======================================')
        print('Compiling...')
        if system('gcc outFile.c -o executable.out') == 0:
            print('Running...\n\n')
            system('./executable.out')
