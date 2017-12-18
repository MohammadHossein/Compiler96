from copy import deepcopy
from os import system
from tabnanny import errprint


class toC:
    def __init__(self, quadRuples=[], temps={}, symbolTable={}, arraySize={}):
        self.C = []
        self.define = []
        self.chars = {
            'آ': 'a', 'ا': 'a', 'ب': 'b', 'پ': 'p', 'ت': 't', 'ث': 's', 'ج': 'j', 'چ': 'c', 'ح': 'h', 'خ': 'k',
            'د': 'd', 'ذ': 'z', 'ر': 'r', 'ز': 'z', 'ژ': 'x', 'س': 'S', 'ش': 's', 'ص': 's', 'ض': 'z', 'ط': 't',
            'ظ': 'z', 'ع': 'e', 'غ': 'g', 'ف': 'f', 'ق': 'g', 'ك': 'k', 'گ': 'g', 'ل': 'l', 'م': 'm', 'ن': 'n',
            'ه': 'h', 'و': 'v', 'ى': 'y', 'ک': 'k', 'ي': 'y', 'ی': 'y', 'ھ': 'h', 'ە': 'h', 'ہ': '_', '_': '_',
            '۰': '0', '۵': '5', '۳': '3', '۹': '9', '۲': '2', '۴': '4', '۸': '8', '۷': '7', '۱': '1', '۶': '6'
        }
        self.nums = {'۰': '0', '۵': '5', '۳': '3', '۹': '9', '۲': '2', '۴': '4', '۸': '8', '۷': '7', '۱': '1', '۶': '6'}
        self.arraySize = arraySize
        self.quadRuples = quadRuples
        self.symbolTable = symbolTable
        self.labels = set()
        for quadRuple in self.quadRuples:
            if 'goto' in quadRuple.result:
                if len(quadRuple.result.split()) > 1:
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
                if ID not in self.arraySize.keys():
                    code += self.ids[ID][1] + ' ' + self.toEnglish(ID) + ';\n'
                else:
                    code += self.ids[ID][1] + ' ' + self.toEnglish(ID) + '[' + self.arraySize[ID] + '];\n'
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

    def toEnglishArray(self, ID):
        out = ''
        tempID = ID.split('[', 1)[0]
        out += self.toEnglish(tempID)
        out += '['
        for c in ID[ID.index('[')+1: ID.index(']')]:
            try:
                out += self.nums[c]
            except:
                out += c
        out += ']'
        return out

    def save(self):
        with open('ToC/out/outFile.c', 'w') as output:
            output.write('#include<stdio.h>\n#include<stdlib.h>\n#include<stdbool.h>\n#include<time.h>\n')
            output.write('int main(){\nsrand(time(NULL));\n')
            lineNumber = 0
            for temp in self.temps.keys():
                code = self.defineId(temp)
                output.write(code)
            for ID in self.symbolTable.keys():
                code = self.defineId(ID)
                output.write(code)
            for quadRuple in self.quadRuples:
                code = ''
                # code += self.defineId(quadRuple.arg_one)
                # code += self.defineId(quadRuple.arg_two)
                code += self.addLabel(lineNumber)
                if quadRuple.result in self.temps.keys():
                    # code += self.defineId(quadRuple.result)
                    # code += self.addLabel(lineNumber)
                    quadRuple.arg_one = self.toEnglish(quadRuple.arg_one)
                    quadRuple.arg_two = self.toEnglish(quadRuple.arg_two)
                    quadRuple.result = self.toEnglish(quadRuple.result)
                    code += str(quadRuple) + ';\n'
                elif quadRuple.result in self.ids.keys():
                    # code += self.defineId(quadRuple.result)
                    # code += self.addLabel(lineNumber)
                    quadRuple.arg_one = self.toEnglish(quadRuple.arg_one)
                    quadRuple.arg_two = self.toEnglish(quadRuple.arg_two)
                    quadRuple.result = self.toEnglish(quadRuple.result)
                    code += str(quadRuple) + ';\n'
                elif 'goto' in quadRuple.result:
                    # code += self.addLabel(lineNumber)
                    if len(quadRuple.result.split()) > 1:
                        if quadRuple.arg_two == '':
                            code += 'goto L' + quadRuple.result.split()[1] + ';\n'
                        else:
                            code += 'if ( ' + self.toEnglish(
                                quadRuple.arg_one) + ' ' + quadRuple.op + ' ' + self.toEnglish(
                                quadRuple.arg_two) + ' ) \n' \
                                    + '\t' + 'goto L' + quadRuple.result.split()[1] + ';\n'
                elif '[' in quadRuple.result:
                    quadRuple.arg_one = self.toEnglish(quadRuple.arg_one)
                    quadRuple.arg_two = self.toEnglish(quadRuple.arg_two)
                    quadRuple.result = self.toEnglishArray(quadRuple.result)
                    code += str(quadRuple) + ';\n'
                else:
                    # errprint('Error', quadRuple)
                    pass
                output.write(code)
                lineNumber += 1
            for label in self.labels:
                output.write('L' + label + ':\n')
            for id in self.ids.keys():
                output.write(self.defineId(id))
                type = self.ids[id][1]
                ID = self.ids[id][0]
                if type == 'int':
                    if id in self.arraySize.keys():
                        for i in range(int(self.arraySize[id])):
                            output.write('printf("' + ID + '[' + str(i) + ']: %d\\n",' + ID + '[' + str(i) + ']);\n')
                    else:
                        output.write('printf("' + ID + ': %d\\n",' + ID + ');\n')
                if type == 'float':
                    if id in self.arraySize.keys():
                        for i in range(int(self.arraySize[id])):
                            output.write('printf("' + ID + '[' + str(i) + ']: %f\\n",' + ID + '[' + str(i) + ']);\n')
                    else:
                        output.write('printf("' + ID + ': %d\\n",' + ID + ');\n')
                if type == 'char':
                    if id in self.arraySize.keys():
                        for i in range(int(self.arraySize[id])):
                            output.write('printf("' + ID + '[' + str(i) + ']: %c\\n",' + ID + '[' + str(i) + ']);\n')
                    else:
                        output.write('printf("' + ID + ': %d\\n",' + ID + ');\n')
                if type == 'bool':
                    if id in self.arraySize.keys():
                        for i in range(int(self.arraySize[id])):
                            output.write('printf("' + ID + '[' + str(i) + ']: %d\\n",' + ID + '[' + str(i) + ']);\n')
                    else:
                        output.write('printf("' + ID + ': %d\\n",' + ID + ');\n')
            # output.write('printf("Hello World!\\n");\n')
            output.write('return 0;\n')
            output.write('}')

    def run(self):
        print('=======================================')
        print('Compiling...')
        out = system('gcc ToC/out/outFile.c -o ToC/out/executable.out')
        if out == 0:
            print('Running...\n\n')
            system('ToC/out/executable.out')
        else :
            print(out.read())