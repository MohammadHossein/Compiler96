import codecs

from Lexer.lex import Lexer
from ToC.toC import toC
from Parser.yacc import Yacc

if __name__ == '__main__':
    f = codecs.open('Samples//array.fa', encoding='utf-8')
    data = f.read()
    f.close()
    # lexer = Lexer().build()
    # lexer.input(data)
    # Tokenize
    '''
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        parsIndex = '-'
        i = -1
        if tok.type == 'ID':
            i = Lexer.sTable.index(tok.value)
        parsIndex = {'-1': '-'}.get(str(i), str(i))
        print(tok.value + "\t" + tok.type + "\t" + str(parsIndex))
    '''
    y = Yacc()
    lexer = Lexer()
    # SymbolTable.SymbolTable.sTable = lexer.sTable
    y.build().parse(data, lexer.build(), False)
    print('---------------------------------------------------------')
    i = 0
    for x in y.quadRuples:
        print(i, x)
        i += 1
    c = toC(y.quadRuples, y.temps, y.symbolTable, y.arraySize)
    c.save()
    c.run()
