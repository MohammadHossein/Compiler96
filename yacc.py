from ply import yacc

import lex


def logger(log):
    print(log)


class Yacc:
    tokens = lex.Lexer.tokens

    def p_barnameh(self, p):
        """barnameh : PROGRAM_KW ID"""
        print(p[0])
        logger('Role1 : barnameh -> برنامه SHENASE tarifha')

    def p_tarifha(self, p):
        """tarifha : tarifha tarif
                    | tarif
        """
        if len(p) == 3:
            logger('Role2.1 : tarifha -> tarifha tarif')
        elif len(p) == 3:
            logger('Role2.2 : tarifha -> tarif')

    def p_tarif_1(self, p):
        """tarif : tarifeSakhtar"""
        logger('Role3.1 : tarif -> tarifeSakhtar')

    def p_tarif_2(self, p):
        """tarif: tarifeMoteghayyer"""
        logger('Role3.1 : tarif -> tarifeMoteghayyer')

    def p_tarif_3(self, p):
        """tarif: tarifeTabe"""
        logger('Role3.1 : tarif -> tarifeTabe')

    def p_tarifeSakhtar(self, p):
        """tarifeSakhtar : STRUCTURE_KW ID OPENING_BRACE tarifhayeMahalli CLOSING_BRACE"""
        logger('Role4 : tarifeSakhtar -> ساختار SHENASE { tarifhayeMahalli }')

    def p_tarifhayeMahalli(self, p):
        """tarifhayeMahalli : tarifhayeMahalli tarifeMoteghayyereMahdud
                            | empty
        """
        if len(p) == 3:
            logger('Role5.1: tarifhayeMahalli -> tarifhayeMahalli tarifeMoteghayyereMahdud')
        elif len(p) == 2:
            logger('Role5.2 :tarifhayeMahalli -> ϵ')

    def p_tarifeMoteghayyereMahdud(self, p):
        """tarifeMoteghayyereMahdud : jenseMahdud tarifhayeMoteghayyerha SEMICOLON"""
        logger('Role6 : tarifeMoteghayyereMahdud -> jenseMahdud tarifhayeMoteghayyerha SEMICOLON')

    def p_jenseMahdud(self, p):
        """jenseMahdud : CONSTANT_KW jens
                        | jens
        """
        if len(p) == 3:
            logger('Role7.1 : jenseMahdud -> CONSTANT_KW jens')
        elif len(p) == 2:
            logger('Role7.2 : jenseMahdud -> jens')

    def p_jens_1(self, p):
        """jens : INTEGER_KW"""
        logger('Role8.1 : jens -> INTEGER_KW')

    def p_jens_2(self, p):
        """jens : FLOAT_KW"""
        logger('Role8.2 : jens -> FLOAT_KW')

    def p_jens_3(self, p):
        """jens : BOOLEAN_KW"""
        logger('Role8.3 : jens -> BOOLEAN_KW')

    def p_jens_4(self, p):
        """jens : CHAR_KW"""
        logger('Role8.4 : jens -> CHAR_KW')

    def p_error(self, p):
        print('syntax error')

    # Empty rule

    def p_empty(self, p):
        """
        empty :
        """
        pass

    def build(self, **kwargs):
        """
        build the parser
        """
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser


parser = Yacc().build()
res = parser.parse('برنامه مثال', lexer=lex.Lexer().build())
print(res)
