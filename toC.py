from os import system

from copy import deepcopy

from QuadRuple import QuadRuple


class toC:
    def __init__(self, quadRuples=[], temps={}, symbolTable={}):
        self.C = []
        self.define = []
        self.chars = {}
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
            self.ids[id] = ('ID' + str(number), ids[id])
            number += 1
        # print IDS
        print('------------IDs---------------\n')
        for key, value in self.ids.items():
            print(key, value[0], sep='\t\t')
        print('\n')

        self.temps = temps

    def defineId(self, ID):
        code = ''
        if ID not in self.define:
            if ID in self.temps.keys():
                code += self.temps[ID] + ' ' + ID + ';\n'
            elif ID in self.ids.keys():
                code += self.ids[ID][1] + ' ' + self.toEnglish(ID) + ';\n'
            else:
                # print('Riiiiiiiiidam to define',ID)
                return code
            self.define.append(ID)
        return code

    def addLabel(self, lineNumber):
        code = ''
        if str(lineNumber) in self.labels:
            code += 'L' + str(lineNumber) + ':\n'
            self.labels.remove(str(lineNumber))
        return code

    def toEnglish(self, ID):
        if ID in self.ids.keys():
            ID = self.ids[ID][0]
        return ID

    def save(self):
        with open('outFile.c', 'w') as output:
            output.write('#include<stdio.h>\n#include<stdlib.h>\n#include<stdbool.h>\n')
            output.write('int main(){\n')
            lineNumber = 0
            for quadRuple in self.quadRuples:
                code = ''
                code += self.defineId(quadRuple.arg_one)
                code += self.defineId(quadRuple.arg_two)
                if quadRuple.result in self.temps.keys():
                    code += self.defineId(quadRuple.result)
                    code += self.addLabel(lineNumber)
                    quadRuple.arg_one = self.toEnglish(quadRuple.arg_one)
                    quadRuple.arg_two = self.toEnglish(quadRuple.arg_two)
                    code += str(quadRuple) + ';\n'
                elif quadRuple.result in self.ids.keys():
                    code += self.defineId(quadRuple.result)
                    code += self.addLabel(lineNumber)
                    quadRuple.arg_one = self.toEnglish(quadRuple.arg_one)
                    quadRuple.arg_two = self.toEnglish(quadRuple.arg_two)
                    quadRuple.result = self.toEnglish(quadRuple.result)
                    code += str(quadRuple) + ';\n'
                elif 'goto' in quadRuple.result:
                    code += self.addLabel(lineNumber)
                    if quadRuple.arg_two == '':
                        code += 'goto L' + quadRuple.result.split()[1] + ';\n'
                    else:
                        code += 'if ( ' + self.toEnglish(quadRuple.arg_one) + ' ' + quadRuple.op + ' ' + self.toEnglish(quadRuple.arg_two) + ' ) \n' \
                                + '\t' + 'goto L' + quadRuple.result.split()[1] + ';\n'

                output.write(code)
                lineNumber += 1
            for label in self.labels:
                output.write('L' + label + ':\n')
            for id in self.ids.keys():
                output.write(self.defineId(id))
                type = self.ids[id][1]
                ID = self.ids[id][0]
                if type == 'int':
                    output.write('printf("' + ID + ': %d\\n",' + ID + ');\n')
                if type == 'float':
                    output.write('printf("' + ID + ': %f\\n",' + ID + ');\n')
                if type == 'char':
                    output.write('printf("' + ID + ': %c\\n",' + ID + ');\n')
                if type == 'bool':
                    output.write('printf("' + ID + ': %d\\n",' + ID + ');\n')

            # output.write('printf("Hello World!\\n");\n')
            output.write('return 0;\n')
            output.write('}')

    def run(self):
        print('=======================================')
        print('Compiling...')
        if system('gcc outFile.c -o executable.out') == 0:
            print('Running...\n\n')
            system('./executable.out')
