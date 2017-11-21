from ply import yacc

import lex


def logger(log):
    print(log)


class Yacc:
    tokens = lex.Lexer.tokens

    precedence = (
        ('left', 'OR_KW', 'THEN_OR_KW'),
        ('left', 'AND_KW', 'THEN_AND_KW'),
        ('left', 'EQ'),
        ('left', 'LT', 'GT', 'LE', 'GE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MOD'),
        ('left', 'MUL', 'DIV'),
        ('right', 'NOT_KW', 'MINUSMINUS', 'PLUSPLUS'),
    )

    def p_barnameh(self, p):
        """barnameh : PROGRAM_KW ID tarifha"""
        print(p[0])
        logger('Rule 1 : barnameh -> برنامه SHENASE tarifha')

    def p_tarifha(self, p):
        """tarifha : tarifha tarif
                    | tarif
        """
        if len(p) == 3:
            logger('Rule 2.1 : tarifha -> tarifha tarif')
        elif len(p) == 2:
            logger('Rule 2.2 : tarifha -> tarif')

    def p_tarif_1(self, p):
        """tarif : tarifeSakhtar"""
        logger('Rule 3.1 : tarif -> tarifeSakhtar')

    def p_tarif_2(self, p):
        """tarif : tarifeMotheghayyer"""
        logger('Rule 3.1 : tarif -> tarifeMotheghayyer')

    def p_tarif_3(self, p):
        """tarif : tarifeTabe"""
        logger('Rule 3.1 : tarif -> tarifeTabe')

    def p_tarifeSakhtar(self, p):
        """tarifeSakhtar : STRUCTURE_KW ID OPENING_BRACE tarifhayeMahalli CLOSING_BRACE"""
        logger('Rule 4 : tarifeSakhtar -> ساختار SHENASE { tarifhayeMahalli }')

    def p_tarifhayeMahalli(self, p):
        """tarifhayeMahalli : tarifhayeMahalli tarifeMotheghayyereMahdud
                            | empty
        """
        if len(p) == 3:
            logger('Rule 5.1: tarifhayeMahalli -> tarifhayeMahalli tarifeMotheghayyereMahdud')
        elif len(p) == 2:
            logger('Rule 5.2 :tarifhayeMahalli -> 𝜀')

    def p_tarifeMotheghayyereMahdud(self, p):
        """tarifeMotheghayyereMahdud : jenseMahdud tarifhayeMotheghayyerha SEMICOLON"""
        logger('Rule 6 : tarifeMotheghayyereMahdud -> jenseMahdud tarifhayeMotheghayyerha ;')

    def p_jenseMahdud(self, p):
        """jenseMahdud : CONSTANT_KW jens
                        | jens
        """
        if len(p) == 3:
            logger('Rule 7.1 : jenseMahdud -> ثابت jens')
        elif len(p) == 2:
            logger('Rule 7.2 : jenseMahdud -> jens')

    def p_jens_1(self, p):
        """jens : INTEGER_KW"""
        logger('Rule 8.1 : jens -> صحیح')

    def p_jens_2(self, p):
        """jens : FLOAT_KW"""
        logger('Rule 8.2 : jens -> اعشاری')

    def p_jens_3(self, p):
        """jens : BOOLEAN_KW"""
        logger('Rule 8.3 : jens -> منطقی')

    def p_jens_4(self, p):
        """jens : CHAR_KW"""
        logger('Rule 8.4 : jens -> حرف')

    def p_tarifeMotheghayyer(self, p):
        """tarifeMotheghayyer : jens tarifhayeMotheghayyerha SEMICOLON"""
        logger('Rule 9 : tarifeMotheghayyer -> jens tarifhayeMotheghayyerha ;')

    def p_tarifhayeMotegayyerha(self, p):
        """tarifhayeMotheghayyerha : tarifeMeghdareAvvalie
                                |   tarifhayeMotheghayyerha COMMA tarifeMeghdareAvvalie
        """
        if len(p) == 2:
            logger('Rule 10.1 : tarifhayeMotheghayyerha -> tarifeMeghdareAvvalie')
        elif len(p) == 4:
            logger('Rule 10.2 : tarifhayeMotheghayyerha -> tarifhayeMotheghayyerha , tarifeMeghdareAvvalie')

    def p_tarifeMeghdareAvvalie(self, p):
        """tarifeMeghdareAvvalie : tarifeShenaseyeMoteghayyer
                                |  tarifeShenaseyeMoteghayyer EXP ebarateSade
        """
        if len(p) == 2:
            logger('Rule 11.1 : tarifeMeghdareAvvalie -> tarifeShenaseyeMoteghayyer')
        elif len(p) == 4:
            logger('Rule 11.2 : tarifeMeghdareAvvalie -> tarifeShenaseyeMoteghayyer EXP ebarateSade')

    def p_tarifeShenaseyeMoteghayyer(self, p):
        """tarifeShenaseyeMoteghayyer : ID
                                | ID OPENING_BRACKET NUMBER_INT CLOSING_BRACE
        """
        if len(p) == 2:
            logger('Rule 12.1 : tarifeShenaseyeMoteghayyer -> ID')
        elif len(p) == 5:
            logger('Rule 12.1 : tarifeShenaseyeMoteghayyer -> ID [ NUMBER_INT ]')

    def p_tarifeTabe(self, p):
        """tarifeTabe : jens ID OPENING_PARENTHESES vorudi CLOSING_PARENTHESES jomle
                    |   ID OPENING_PARENTHESES vorudi CLOSING_PARENTHESES jomle
        """
        if len(p) == 7:
            logger('Rule 13.1 tarifeTabe -> jens ID ( vorudi ) jomle')
        elif len(p) == 6:
            logger('Rule 13.2 tarifeTabe -> ID ( vorudi ) jomle')

    def p_vorudi1(self, p):
        """vorudi : vorudiha"""
        logger('Rule 14.1 vorudi -> vorudiha')

    def p_vorudi2(self, p):
        """vorudi : empty"""
        logger('Rule 14.2 vorudi -> 𝜀')

    def p_vorudiha(self, p):
        """vorudiha : vorudiha SEMICOLON jensVorudiha
                    | jensVorudiha
        """
        if len(p) == 4:
            logger('Rule 15.1 : vorudiha -> vorudiha ; jensVorudiha')
        elif len(p) == 2:
            logger('Rule 15.2 : vorudiha -> jensVorudiha')

    def p_jensVorudiha(self, p):
        """jensVorudiha : jens shenaseyeVorudiha"""
        logger('Rule 16 : jensVorudiha -> jens shenaseyeVorudiha')

    def p_shenaseyeVorudiha(self, p):
        """shenaseyeVorudiha : shenaseyeVorudiha COMMA shenaseyeVorudi
                            | shenaseyeVorudi
        """
        if len(p) == 4:
            logger('Rule 17.1 : shenaseyeVorudiha -> shenaseyeVorudiha , shenaseyeVorudi')
        elif len(p) == 2:
            logger('Rule 17.2 : shenaseyeVorudiha -> shenaseyeVorudi')

    def p_shenaseyeVorudi(self, p):
        """shenaseyeVorudi : ID
                            | ID OPENING_BRACE CLOSING_BRACE
        """
        if len(p) == 2:
            logger('Rule 18.1 : shenaseyeVorudi -> ID')
        if len(p) == 4:
            logger('Rule 18.2 : shenaseyeVorudi -> ID [ ]')

    def p_jomle_1(self, p):
        """jomle : jomleyeMorakkab"""
        logger('Rule 19.1 : jomle -> jomleyeMorakkab')

    def p_jomle_2(self, p):
        """jomle : jomleyeEbarat"""
        logger('Rule 19.2 : jomle -> jomleyeEbarat')

    def p_jomle_3(self, p):
        """jomle : jomleyeEntekhab"""
        logger('Rule 19.3 : jomle -> jomleyeEntekhab')

    def p_jomle_4(self, p):
        """jomle : jomleyeTekrar"""
        logger('Rule 19.4 : jomle -> jomleyeTekrar')

    def p_jomle_5(self, p):
        """jomle : jomleyeBazgasht"""
        logger('Rule 19.5 : jomle -> jomleyeBazgasht')

    def p_jomle_6(self, p):
        """jomle : jomleyeShekast"""
        logger('Rule 19.6 : jomle -> jomleyeShekast')

    def p_jomleyeMorakkab(self, p):
        """jomleyeMorakkab : OPENING_BRACE tarifhayeMahalli jomleha CLOSING_BRACE"""
        logger('Rule 20 : jomleyeMorakkab -> { tarifhayeMahalli jomleha }')

    def p_jomleha(self, p):
        """jomleha : jomleha jomle
                    | empty
        """
        if len(p) == 3:
            logger('Rule 21.1 : jomleha -> jomleha jomle')
        elif len(p) == 2:
            logger('Rule 21.2 : jomleha -> 𝜀')

    def p_jomleyeEbarat(self, p):
        """jomleyeEbarat : ebarat SEMICOLON
                        | SEMICOLON
        """
        if len(p) == 3:
            logger('Rule 22.1 : jomleyeEbarat -> ebarat ;')
        elif len(p) == 2:
            logger('Rule 22.2 : jomleyeEbarat -> ;')

    def p_jomleyeEntekhab(self, p):
        """jomleyeEntekhab : IF_KW ebarateSade THEN_KW jomle
                        | IF_KW ebarateSade THEN_KW jomle ELSE_KW jomle
                        | SWITCH_KW OPENING_PARENTHESES ebarateSade CLOSING_PARENTHESES onsoreHalat onsorePishfarz END_KW
        """
        if len(p) == 5:
            logger('Rule 23.1 : jomleyeEntekhab -> اگر ebarateSade آنگاه jomle')
        if len(p) == 7:
            logger('Rule 23.2 : jomleyeEntekhab -> اگر ebarateSade آنگاه jomle وگرنه jomle')
        if len(p) == 8:
            logger('Rule 23.3 : jomleyeEntekhab -> کلید ( ebarateSade ) onsoreHalat onsorePishfarz تمام')

    def p_onsoreHalat(self, p):
        """onsoreHalat : CASE_KW NUMBER_INT COLON jomle SEMICOLON
                    |   onsoreHalat CASE_KW NUMBER_INT COLON jomle SEMICOLON
        """
        if len(p) == 6:
            logger('Rule 24.1 : onsoreHalat -> حالت NUMBER_INT : jomle ;')
        elif len(p) == 7:
            logger('Rule 24.2 : onsoreHalat -> onsoreHalat حالت NUMBER_INT : jomle ;')

    def p_onsorePishfarz(self, p):
        """onsorePishfarz : DEFAULT_KW COLON jomle SEMICOLON
                        |   empty
        """
        if len(p) == 4:
            logger('Rule 25.1 : onsorePishfarz -> پیشفرض : jomle ;')
        elif len(p) == 2:
            logger('Rule 25.1 : onsorePishfarz -> 𝜀')

    def p_jomleyeTekrar(self, p):
        """jomleyeTekrar : WHILE_KW OPENING_PARENTHESES ebarateSade CLOSING_PARENTHESES jomle"""

        logger('Rule 26 : jomleyeTekrar -> وقتی ( ebarateSade ) jomle')

    def p_jomleyeBazgasht(self, p):
        """jomleyeBazgasht : RETURN_KW SEMICOLON
                        |   RETURN_KW ebarat SEMICOLON
        """
        if len(p) == 3:
            logger('Rule 27.1 : jomleyeBazgasht -> برگردان ;')
        if len(p) == 4:
            logger('Rule 27.1 : jomleyeBazgasht -> برگردان ebarat ;')

    def p_jomleyeShekast(self, p):
        """jomleyeShekast : BREAK_KW SEMICOLON"""
        logger('Rule 28 : jomleyeShekast -> BREAK_KW SEMICOLON')

    def p_ebarat_1(self, p):
        """ebarat : taghirpazir EXP ebarat"""
        logger('Rule 29.1 : ebarat -> taghirpazir EXP ebarat')

    def p_ebarat_2(self, p):
        """ebarat : taghirpazir PLUS_EXP ebarat"""
        logger('Rule 29.2 : ebarat -> taghirpazir PLUS_EXP ebarat')

    def p_ebarat_3(self, p):
        """ebarat : taghirpazir MINUS_EXP ebarat"""
        logger('Rule 29.3 : ebarat -> taghirpazir MINUS_EXP ebarat')

    def p_ebarat_4(self, p):
        """ebarat : taghirpazir MUL_EXP ebarat"""
        logger('Rule 29.4 : ebarat -> taghirpazir MUL_EXP ebarat')

    def p_ebarat_5(self, p):
        """ebarat : taghirpazir DIV_EXP ebarat"""
        logger('Rule 29.5 : ebarat -> taghirpazir DIV_EXP ebarat')

    def p_ebarat_6(self, p):
        """ebarat : taghirpazir PLUSPLUS"""
        logger('Rule 29.6 : ebarat -> taghirpazir PLUSPLUS')

    def p_ebarat_7(self, p):
        """ebarat : taghirpazir MINUSMINUS"""
        logger('Rule 29.7 : ebarat -> taghirpazir MINUSMINUS')

    def p_ebarat_8(self, p):
        """ebarat : ebarateSade"""
        logger('Rule 29.8 : ebarat -> ebarateSade')

    def p_ebarateSade_1(self, p):
        """ebarateSade : ebarateSade THEN_OR_KW ebarateSade"""
        logger('Rule 30.1 : ebarateSade -> ebarateSade THEN_OR_KW ebarateSade')

    def p_ebarateSade_2(self, p):
        """ebarateSade : ebarateSade THEN_AND_KW ebarateSade"""
        logger('Rule 30.2 : ebarateSade -> ebarateSade THEN_AND_KW ebarateSade')

    def p_ebarateSade_3(self, p):
        """ebarateSade : ebarateSade OR_KW ebarateSade"""
        logger('Rule 30.3 : ebarateSade -> ebarateSade OR_KW ebarateSade')

    def p_ebarateSade_4(self, p):
        """ebarateSade : ebarateSade AND_KW ebarateSade"""
        logger('Rule 30.4 : ebarateSade -> ebarateSade AND_KW ebarateSade')

    def p_ebarateSade_5(self, p):
        """ebarateSade : NOT_KW ebarateSade"""
        logger('Rule 30.5 : ebarateSade -> NOT_KW ebarateSade')

    def p_ebarateSade_6(self, p):
        """ebarateSade : ebarateRabetei"""
        logger('Rule 30.6 : ebarateSade -> ebarateRabetei')

    def p_ebarateRabetei_1(self, p):
        """ebarateRabetei : ebarateRiaziManteghi"""
        logger('Rule 31.1 : ebarateRabetei -> ebarateRiaziManteghi')

    def p_ebarateRabetei_2(self, p):
        """ebarateRabetei : ebarateRiaziManteghi amalgareRabetei ebarateRiaziManteghi"""
        logger('Rule 31.2 : ebarateRabetei -> ebarateRiaziManteghi amalgareRabetei ebarateRiaziManteghi')

    def p_amalgareRabetei_1(self, p):
        """amalgareRabetei : LT"""
        logger('Rule 32.1 : amalgareRabetei -> LT')

    def p_amalgareRabetei_2(self, p):
        """amalgareRabetei : LE"""
        logger('Rule 32.2 : amalgareRabetei -> LE')

    def p_amalgareRabetei_3(self, p):
        """amalgareRabetei : EQ"""
        logger('Rule 32.3 : amalgareRabetei -> EQ')

    def p_amalgareRabetei_4(self, p):
        """amalgareRabetei : GE"""
        logger('Rule 32.4 : amalgareRabetei -> GE')

    def p_amalgareRabetei_5(self, p):
        """amalgareRabetei : GT"""
        logger('Rule 32.5 : amalgareRabetei -> GT')

    def p_ebarateRiaziManteghi_1(self, p):
        """ebarateRiaziManteghi : ebarateYegani"""
        logger('Rule 33.1 : ebarateRiaziManteghi -> ebarateYegani')

    def p_ebarateRiaziManteghi_2(self, p):
        """ebarateRiaziManteghi : ebarateRiaziManteghi amalgareRiazi ebarateRiaziManteghi"""
        logger('Rule 33.2 : ebarateRiaziManteghi -> ebarateRiaziManteghi amalgareRiazi ebarateRiaziManteghi')

    def p_amalgareRiazi_1(self, p):
        """amalgareRiazi : MINUS"""
        logger('Rule 34.1 : amalgareRiazi -> MINUS')

    def p_amalgareRiazi_2(self, p):
        """amalgareRiazi : MUL"""
        logger('Rule 34.2 : amalgareRiazi -> MUL')

    def p_amalgareRiazi_3(self, p):
        """amalgareRiazi : PLUS"""
        logger('Rule 34.3 : amalgareRiazi -> PLUS')

    def p_amalgareRiazi_4(self, p):
        """amalgareRiazi : DIV"""
        logger('Rule 34.4 : amalgareRiazi -> DIV')

    def p_amalgareRiazi_5(self, p):
        """amalgareRiazi : MOD"""
        logger('Rule 34.5 : amalgareRiazi -> MOD')

    def p_ebarateYegani_1(self, p):
        """ebarateYegani : amalgareYegani ebarateYegani"""
        logger('Rule 35.1 : ebarateYegani -> amalgareYegani ebarateYegani')

    def p_ebarateYegani_2(self, p):
        """ebarateYegani : amel"""
        logger('Rule 35.2 : ebarateYegani -> amel')

    def p_amalgareYegani_1(self, p):
        """amalgareYegani : MINUS"""
        logger('Rule 36.1 : amalgareYegani -> MINUS')

    def p_amalgareYegani_2(self, p):
        """amalgareYegani : MUL"""
        logger('Rule 36.2 : amalgareYegani -> MUL')

    def p_amalgareYegani_3(self, p):
        """amalgareYegani : QUESTION_MARK"""
        logger('Rule 36.3 : amalgareYegani -> QUESTION_MARK')

    def p_amel_1(self, p):
        """amel : taghirpazir"""
        logger('Rule 37.1 : amel -> taghirpazir')

    def p_amel_2(self, p):
        """amel : taghirnapazir"""
        logger('Rule 37.2 : amel -> taghirnapazir')

    def p_taghirpazir_1(self, p):
        """taghirpazir : ID"""
        logger('Rule 38.1 : taghirpazir -> ID')

    def p_taghirpazir_2(self, p):
        """taghirpazir : taghirpazir OPENING_BRACKET ebarat CLOSING_BRACKET"""
        logger('Rule 38.2 : taghirpazir -> taghirpazir OPENING_BRACKET ebarat CLOSING_BRACKET')

    def p_taghirpazir_3(self, p):
        """taghirpazir :  taghirpazir DOT ID"""
        logger('Rule 38.3 : taghirpazir -> taghirpazir DOT ID')

    def p_taghirnapazir_1(self, p):
        """taghirnapazir : OPENING_PARENTHESES ebarat CLOSING_PARENTHESES"""
        logger('Rule 39.1 : taghirnapazir -> (ebarat)')

    def p_taghirnapazir_2(self, p):
        """taghirnapazir : sedaZadan"""
        logger('Rule 39.2 : taghirnapazir -> sedaZadan')

    def p_taghirnapazir_3(self, p):
        """taghirnapazir : meghdareSabet"""
        logger('Rule 39.3 : taghirnapazir -> meghdareSabet')

    def p_sedaZadan(self, p):
        """sedaZadan : ID OPENING_PARENTHESES bordareVorudi CLOSING_PARENTHESES"""
        logger('Rule 40 : sedaZadan -> ID ( bordareVorudi )')

    def p_bordareVorudi_1(self, p):
        """bordareVorudi : bordareVorudiha"""
        logger('Rule 41.1 : bordareVorudi -> bordareVorudiha')

    def p_bordareVorudi_2(self, p):
        """bordareVorudi : empty"""
        logger('Rule 41.2 : bordareVorudi -> ϵ')

    def p_bordareVorudiha(self, p):
        """bordareVorudiha : bordareVorudiha COMMA
                            | ebarat
        """
        if len(p) == 3:
            logger('Rule 42.1: bordareVorudiha -> bordareVorudiha COMMA')
        elif len(p) == 2:
            logger('Rule 42.2 :bordareVorudiha -> ebarat')

    def p_meghdareSabet_1(self, p):
        """meghdareSabet : NUMBER_INT"""
        logger('Rule 43.1 : meghdareSabet -> NUMBER_INT')

    def p_meghdareSabet_2(self, p):
        """meghdareSabet : NUMBER_FLOAT"""
        logger('Rule 43.2 : meghdareSabet -> NUMBER_FLOAT')

    def p_meghdareSabet_3(self, p):
        """meghdareSabet : FIXED_CHARACTER"""
        logger('Rule 43.3 : meghdareSabet -> FIXED_CHARACTER')

    def p_meghdareSabet_4(self, p):
        """meghdareSabet : TRUE_KW"""
        logger('Rule 43.4 : meghdareSabet -> TRUE_KW')

    def p_meghdareSabet_5(self, p):
        """meghdareSabet : FALSE_KW"""
        logger('Rule 43.4 : meghdareSabet -> FALSE_KW')

    def p_error(self, p):
        print('syntax error')

    # Empty Rule 

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
