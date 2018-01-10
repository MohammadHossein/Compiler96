from copy import deepcopy
from os import system


class toC:
    def __init__(self, quadRuples=[], temps={}, symbolTable={}, arraySize={}, returnID='returnID', params={},structs={}):
        self.C = []
        print(temps)
        self.structs = structs
        self.params = params
        self.returnID = returnID
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
                temp = quadRuple.result.split()
                if len(temp) > 1:
                    if 'Func' not in temp[1] and temp[1] != 'MAIN':
                        self.labels.add(temp[1])
        ids = deepcopy(symbolTable)
        self.ids = {}
        number = 0
        print(ids)
        for id in ids.keys():
            self.ids[id] = ('ID' + str(number), ids[id])
            number += 1
        for struct in self.structs.keys():
            self.ids[struct] = self.structs[struct]
        # print IDS
        print('------------IDs---------------\n')
        for key, value in self.ids.items():
            print(key, value[0],value[1], sep='\t\t')
        print('\n')

        self.temps = temps

    def defineId(self, ID):
        code = ''
        if ID not in self.define:
            if ID in self.temps.keys():
                code += self.temps[ID] + ' ' + ID + ';\n'
            elif ID in self.ids.keys():
                star = ''
                if ID in self.params.keys():
                    star = '*'
                if ID not in self.arraySize.keys():
                    code += self.ids[ID][1] + star + ' ' + self.toEnglish(ID) + ';\n'
                else:
                    code += self.ids[ID][1] + star + ' ' + self.toEnglish(ID) + '[' + self.arraySize[ID] + '];\n'
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
        print(ID,end='  ')
        if '[' in ID:
            ID = ID[0:ID.index('[')]
            if ID in self.ids.keys():
                ID = '*' + self.ids[ID][0]
        elif '*' not in ID:
            if ID in self.ids.keys():
                ID = self.ids[ID][0]
        else:
            ID = ID.replace('*', '')
            if ID in self.ids.keys():
                ID = '*' + self.ids[ID][0]
        print(ID)
        return ID

    def toEnglishArray(self, ID):
        out = ''
        tempID = ID.split('[', 1)[0]
        out += self.toEnglish(tempID)
        out += '['
        for c in ID[ID.index('[') + 1: ID.index(']')]:
            try:
                out += self.nums[c]
            except:
                out += c
        out += ']'
        return out

    def save(self):
        with open('ToC/out/outFile.c', 'w') as output:
            output.write(
                '#include<stdio.h>\n#include<stdlib.h>\n#include<stdbool.h>\n#include<time.h>\n#include<setjmp.h>\n'
                'jmp_buf buf[1000];\nint jmp = 0;\nlong * sp,paramCount,*paramTemp1,*paramTemp2,*top;\nlong stack[1000];\n')
            output.write('int main(){\nsp = stack;\ntop = stack;\nsrand(time(NULL));\n' +
                         'void* ' + self.returnID + ' = (void*)malloc(sizeof(float));\n')
            lineNumber = 0
            for temp in self.temps.keys():
                code = self.defineId(temp)
                output.write(code)
            for ID in self.ids.keys():
                code = self.defineId(ID)
                output.write(code)
            for quadRuple in self.quadRuples:
                code = ''
                if quadRuple.result in self.structs.keys():
                    quadRuple.result = self.ids[quadRuple.result][0]
                if quadRuple.arg_one in self.structs.keys():
                    quadRuple.arg_one = self.ids[quadRuple.arg_one][0]
                if quadRuple.arg_two in self.structs.keys():
                    quadRuple.arg_two = self.ids[quadRuple.arg_two][0]
                # code += self.defineId(quadRuple.arg_one)
                # code += self.defineId(quadRuple.arg_two)
                code += self.addLabel(lineNumber)
                if '*' in quadRuple.arg_one and '(' in quadRuple.arg_one:
                    code+= str(quadRuple) + ';\n'
                elif quadRuple.result in self.temps.keys():
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
                            temp = quadRuple.result.split()
                            if temp[1] != 'MAIN' and 'Func' not in temp[1]:
                                code += 'goto L' + temp[1] + ';\n'
                            else:
                                code += 'goto ' + temp[1] + ';\n'
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
                elif quadRuple.op == 'label':
                    code += str(quadRuple) + '\n'
                else:
                    quadRuple.arg_one = self.toEnglish(quadRuple.arg_one)
                    quadRuple.arg_two = self.toEnglish(quadRuple.arg_two)
                    code += str(quadRuple) + ';\n'
                    # errprint('Error', quadRuple)
                    # pass
                output.write(code)
                lineNumber += 1
            for label in self.labels:
                output.write('L' + label + ':\n')
            for id in self.ids.keys():
                output.write(self.defineId(id))
                type = self.ids[id][1]
                ID = self.ids[id][0]
                print(ID,type)
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
                        output.write('printf("' + ID + ': %f\\n",' + ID + ');\n')
                if type == 'char':
                    if id in self.arraySize.keys():
                        for i in range(int(self.arraySize[id])):
                            output.write('printf("' + ID + '[' + str(i) + ']: %c\\n",' + ID + '[' + str(i) + ']);\n')
                    else:
                        output.write('printf("' + ID + ': %c\\n",' + ID + ');\n')
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
        else:
            print(out.read())
