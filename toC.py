from os import system

from copy import deepcopy

from QuadRuple import QuadRuple


class toC:
    def __init__(self, quadRuples=[], temps={},symbolTable={}):
        self.C = []
        self.quadRuples = quadRuples
        self.symbolTable = symbolTable
        self.labels = set()
        for quadRuple in self.quadRuples:
            if 'goto' in quadRuple.result:
                self.labels.add(quadRuple.result.split()[1])
        ids = deepcopy(symbolTable)
        self.ids = {}
        number = 0
        for id in ids.keys():
            self.ids[id] = ('ID' + str(number),ids[id])
            number += 1
        # print IDS
        print('------------IDs---------------\n')
        for key,value in self.ids.items():
            print('{:1} {:<20}'.format(key,value[0]))


        self.temps = temps

    def toC(self):
        pass

    def save(self):
        define = []
        with open('outFile.c', 'w') as output:
            output.write('#include<stdio.h>\n#include<stdlib.h>\n')
            output.write('int main(){\n')
            lineNumber = 0
            for quadRuple in self.quadRuples:
                code = ''
                if quadRuple.result in self.temps.keys():
                    if quadRuple.result not in define:
                        code += self.temps[quadRuple.result] + ' ' + quadRuple.result + ';\n'
                        define.append(quadRuple.result)
                    if str(lineNumber) in self.labels:
                        code += 'L' + str(lineNumber) + ':\n'
                        self.labels.remove(str(lineNumber))
                    code += str(quadRuple) + ';\n'
                    if quadRuple.arg_one in self.ids.keys():
                        quadRuple.arg_one = self.ids[quadRuple.arg_one][0]
                    if quadRuple.arg_two in self.ids.keys():
                        quadRuple.arg_two = self.ids[quadRuple.arg_two][0]
                elif quadRuple.result in self.ids.keys():
                    if self.ids[quadRuple.result][0] not in define:
                        code += self.ids[quadRuple.result][1] + ' ' + self.ids[quadRuple.result][0] + ';\n'
                        define.append(self.ids[quadRuple.result][0])
                    if str(lineNumber) in self.labels:
                        code += 'L' + str(lineNumber) + ':\n'
                        self.labels.remove(str(lineNumber))
                    quadRuple.result = self.ids[quadRuple.result][0]
                    if quadRuple.arg_one in self.ids.keys():
                        quadRuple.arg_one = self.ids[quadRuple.arg_one][0]
                    if quadRuple.arg_two in self.ids.keys():
                        quadRuple.arg_two = self.ids[quadRuple.arg_two][0]
                    code += str(quadRuple) + ';\n'
                elif 'goto' in quadRuple.result:
                    if str(lineNumber) in self.labels:
                        code += 'L' + str(lineNumber) + ':\n'
                        self.labels.remove(str(lineNumber))
                    if quadRuple.arg_two == '':
                        code += 'goto L' + quadRuple.result.split()[1] + ';\n'
                    else:
                        code += 'if ( ' + quadRuple.arg_one + ' ' + quadRuple.op + ' ' + quadRuple.arg_two + ' ) \n'\
                                + '\t' + 'goto L' + quadRuple.result.split()[1] + ';\n'

                output.write(code)
                lineNumber += 1
            for label in self.labels:
                output.write('L' + label + ':\n')
            for id in self.ids.keys():
                type = self.ids[id][1]
                ID = self.ids[id][0]
                if type == 'int':
                    output.write('printf("%d\\n",' + ID + ');\n')
                if type == 'float':
                    output.write('printf("%f\\n",' + ID + ');\n')
                if type == 'char':
                    output.write('printf("%c\\n",' + ID + ');\n')
                if type == 'bool':
                    output.write('printf("%d\\n",' + ID + ');\n')

            output.write('printf("Hello World!\\n");\n')
            output.write('return 0;\n')
            output.write('}')

    def run(self):
        print('=======================================')
        print('Compiling...')
        if system('gcc outFile.c -o executable.out') == 0:
            print('Running...\n\n')
            system('./executable.out')
