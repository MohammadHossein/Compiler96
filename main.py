import codecs
from lex import Lexer
from yacc import Yacc

if __name__ == '__main__':
    lexer = Lexer().build()
    f = codecs.open('sample.fa', encoding='utf-8')
    data = f.read()
    f.close()
    lexer.input(data)
    # Tokenize
    """
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
    """
    print(Yacc().build().parse(data, Lexer().build(),True))

