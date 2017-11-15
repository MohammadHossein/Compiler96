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


    def p_jomleyeShekast(self, p):
        """jomleyeShekast : BREAK_KW SEMICOLON"""
        logger('Role28 : jomleyeShekast -> BREAK_KW SEMICOLON')


    def p_ebarat_1(self, p):
        """ebarat : taghirpazir EXP ebarat"""
        logger('Role29.1 : ebarat -> taghirpazir EXP ebarat')

    def p_ebarat_1(self, p):
        """ebarat : taghirpazir PLUS_EXP ebarat"""
        logger('Role29.1 : ebarat -> taghirpazir PLUS_EXP ebarat')

    def p_ebarat_2(self, p):
        """ebarat : taghirpazir MINUS_EXP ebarat"""
        logger('Role29.2 : ebarat -> taghirpazir MINUS_EXP ebarat')

    def p_ebarat_3(self, p):
        """ebarat : taghirpazir MUL_EXP ebarat"""
        logger('Role29.3 : ebarat -> taghirpazir MUL_EXP ebarat')

    def p_ebarat_4(self, p):
        """ebarat : taghirpazir DIV_EXP ebarat"""
        logger('Role29.4 : ebarat -> taghirpazir DIV_EXP ebarat')

    def p_ebarat_5(self, p):
        """ebarat : taghirpazir PLUSPLUS"""
        logger('Role29.5 : ebarat -> taghirpazir PLUSPLUS')

    def p_ebarat_6(self, p):
        """ebarat : taghirpazir MINUSMINUS"""
        logger('Role29.6 : ebarat -> taghirpazir MINUSMINUS')

    def p_ebarat_7(self, p):
        """ebarat : ebarateSade"""
        logger('Role29.7 : ebarat -> ebarateSade')


    def p_ebarateSade_1(self, p):
        """ebarateSade : ebarateSade THEN_OR_KW ebarateSade"""
        logger('Role30.1 : ebarateSade -> ebarateSade THEN_OR_KW ebarateSade')

    def p_ebarateSade_2(self, p):
        """ebarateSade : ebarateSade THEN_AND_KW ebarateSade"""
        logger('Role30.2 : ebarateSade -> ebarateSade THEN_AND_KW ebarateSade')

    def p_ebarateSade_3(self, p):
        """ebarateSade : ebarateSade OR_KW ebarateSade"""
        logger('Role30.3 : ebarateSade -> ebarateSade OR_KW ebarateSade')

    def p_ebarateSade_4(self, p):
        """ebarateSade : ebarateSade AND_KW ebarateSade"""
        logger('Role30.4 : ebarateSade -> ebarateSade AND_KW ebarateSade')

    def p_ebarateSade_5(self, p):
        """ebarateSade : NOT_KW ebarateSade"""
        logger('Role30.5 : ebarateSade -> NOT_KW ebarateSade')

    def p_ebarateSade_6(self, p):
        """ebarateSade : ebarateRabetei"""
        logger('Role30.6 : ebarateSade -> ebarateRabetei')


    def p_ebarateRabetei_1(self, p):
        """ebarateRabetei : ebarateRiaziManteghi"""
        logger('Role31.1 : ebarateRabetei -> ebarateRiaziManteghi')

    def p_ebarateRabetei_2(self, p):
        """ebarateRabetei : ebarateRiaziManteghi amalgareRabetei ebarateRiaziManteghi"""
        logger('Role31.2 : ebarateRabetei -> ebarateRiaziManteghi amalgareRabetei ebarateRiaziManteghi')


    def p_amalgareRabetei_1(self, p):
        """amalgareRabetei : LT"""
        logger('Role32.1 : amalgareRabetei -> LT')

    def p_amalgareRabetei_2(self, p):
        """amalgareRabetei : LE"""
        logger('Role32.2 : amalgareRabetei -> LE')

    def p_amalgareRabetei_3(self, p):
        """amalgareRabetei : EQ"""
        logger('Role32.3 : amalgareRabetei -> EQ')

    def p_amalgareRabetei_4(self, p):
        """amalgareRabetei : GE"""
        logger('Role32.4 : amalgareRabetei -> GE')

    def p_amalgareRabetei_5(self, p):
        """amalgareRabetei : G"""
        logger('Role32.5 : amalgareRabetei -> G')



    def p_ebarateRiaziManteghi_1(self, p):
        """ebarateRiaziManteghi : ebarateYegani"""
        logger('Role33.1 : ebarateRiaziManteghi -> ebarateYegani')

    def p_ebarateRiaziManteghi_2(self, p):
        """ebarateRiaziManteghi : ebarateRiaziManteghi amalgareRiazi ebarateRiaziManteghi"""
        logger('Role33.2 : ebarateRiaziManteghi -> ebarateRiaziManteghi amalgareRiazi ebarateRiaziManteghi')



    def p_amalgareRiazi_1(self, p):
        """amalgareRiazi : MINUS"""
        logger('Role34.1 : amalgareRiazi -> MINUS')

    def p_amalgareRiazi_2(self, p):
        """amalgareRiazi : MUL"""
        logger('Role34.2 : amalgareRiazi -> MUL')

    def p_amalgareRiazi_3(self, p):
        """amalgareRiazi : PLUS"""
        logger('Role34.3 : amalgareRiazi -> PLUS')

    def p_amalgareRiazi_4(self, p):
        """amalgareRiazi : DIV"""
        logger('Role34.4 : amalgareRiazi -> DIV')

    def p_amalgareRiazi_5(self, p):
        """amalgareRiazi : MOD"""
        logger('Role34.5 : amalgareRiazi -> MOD')



    def p_ebarateYegani_1(self, p):
        """ebarateYegani : amalgareYegani ebarateYegani"""
        logger('Role35.1 : ebarateYegani -> amalgareYegani ebarateYegani')

    def p_ebarateYegani_2(self, p):
        """ebarateYegani : amel"""
        logger('Role35.2 : ebarateYegani -> amel')

    def p_amalgareYegani_1(self, p):
        """amalgareYegani : MINUS"""
        logger('Role36.1 : amalgareYegani -> MINUS')

    def p_amalgareYegani_2(self, p):
        """amalgareYegani : MUL"""
        logger('Role36.2 : amalgareYegani -> MUL')

    def p_amalgareYegani_3(self, p):
        """amalgareYegani : QUESTION_MARK"""
        logger('Role36.3 : amalgareYegani -> QUESTION_MARK')

    def p_amel_1(self, p):
        """amel : taghirpazir"""
        logger('Role37.1 : amel -> taghirpazir')

    def p_amel_2(self, p):
        """amel : taghirnapazir"""
        logger('Role37.2 : amel -> taghirnapazir')

    def p_taghirpazir_1(self, p):
        """taghirpazir : ID"""
        logger('Role38.1 : taghirpazir -> ID')

    def p_taghirpazir_2(self, p):
        """taghirpazir : taghirpazir OPENING_BRACKET ebarat CLOSING_BRACKET"""
        logger('Role38.2 : taghirpazir -> taghirpazir OPENING_BRACKET ebarat CLOSING_BRACKET')

    def p_taghirpazir_3(self, p):
        """taghirpazir : taghirpazir -> taghirpazir DOT ID"""
        logger('Role38.3 : taghirpazir -> taghirpazir DOT ID')

    def p_taghirnapazir_1(self, p):
        """taghirnapazir : OPENING_PARENTHESES ebarat COSING_PARENTHESES"""
        logger('Role39.1 : taghirnapazir -> (ebarat)')

    def p_taghirnapazir_2(self, p):
        """taghirnapazir : sedaZadan"""
        logger('Role39.2 : taghirnapazir -> sedaZadan')

    # grammar problem
    # def p_taghirnapazir_3(self, p):
    #     """taghirnapazir : sedaZadan"""
    #     logger('Role39.3 : taghirnapazir -> constant')

    def p_sedaZadan(self, p):
        """sedaZadan : ID OPENING_PARENTHESES bordareVorudi COSING_PARENTHESES"""
        logger('Role40 : sedaZadan -> ID ( bordareVorudi )')

    def p_bordareVorudi_1(self, p):
        """bordareVorudi : bordareVorudiha"""
        logger('Role41.1 : bordareVorudi -> bordareVorudiha')

    def p_bordareVorudi_2(self, p):
        """bordareVorudi : bordareVorudiha"""
        logger('Role41.2 : bordareVorudi -> ϵ')

    def p_bordareVorudiha(self, p):
        """bordareVorudiha : bordareVorudiha COMMA
                            | ebarat
        """
        if len(p) == 3:
            logger('Role42.1: bordareVorudiha -> bordareVorudiha COMMA')
        elif len(p) == 2:
            logger('Role42.2 :bordareVorudiha -> ebarat')

    def p_meghdareSabet_1(self, p):
        """meghdareSabet : NUMBER_INT"""
        logger('Role43.1 : meghdareSabet -> NUMBER_INT')

    def p_meghdareSabet_2(self, p):
        """meghdareSabet : NUMBER_FLOAT"""
        logger('Role43.2 : meghdareSabet -> NUMBER_FLOAT')

    def p_meghdareSabet_3(self, p):
        """meghdareSabet : FIXED_CHARACTER"""
        logger('Role43.3 : meghdareSabet -> FIXED_CHARACTER')

    def p_meghdareSabet_4(self, p):
        """meghdareSabet : TRUE_KW"""
        logger('Role43.4 : meghdareSabet -> TRUE_KW')

    def p_meghdareSabet_5(self, p):
        """meghdareSabet : FALSE_KW"""
        logger('Role43.4 : meghdareSabet -> FALSE_KW')

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
