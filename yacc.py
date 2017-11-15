from ply import yacc

import lex


def logger(log):
    print(log)


class Yacc:
    tokens = lex.Lexer.tokens

    def p_error(self):
        print('syntax error')

    def p_barnameh(self, p):
        'barameh : برنامه ID'
        print(p)
        logger('Role1 : barnameh -> برنامه ID tarifha')

    def p_tarifha(self, p):
        '''tarifha : tarifha tarif
                    | tarif
        '''
        logger()

    # Empty rule
    def p_empty(self, p):
        '''
        empty :
        '''
        pass

    def build(self, **kwargs):
        '''
        build the parser
        '''
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser


