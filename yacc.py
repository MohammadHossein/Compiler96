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
        """tarif: tarifeMotheghayyer"""
        logger('Role3.1 : tarif -> tarifeMotheghayyer')

    def p_tarif_3(self, p):
        """tarif: tarifeTabe"""
        logger('Role3.1 : tarif -> tarifeTabe')

    def p_tarifeSakhtar(self, p):
        """tarifeSakhtar : STRUCTURE_KW ID OPENING_BRACE tarifhayeMahalli CLOSING_BRACE"""
        logger('Role4 : tarifeSakhtar -> ساختار SHENASE { tarifhayeMahalli }')

    def p_tarifhayeMahalli(self, p):
        """tarifhayeMahalli : tarifhayeMahalli tarifeMotheghayyereMahdud
                            | empty
        """
        if len(p) == 3:
            logger('Role5.1: tarifhayeMahalli -> tarifhayeMahalli tarifeMotheghayyereMahdud')
        elif len(p) == 2:
            logger('Role5.2 :tarifhayeMahalli -> 𝜀')

    def p_tarifeMotheghayyereMahdud(self, p):
        """tarifeMotheghayyereMahdud : jenseMahdud tarifhayeMotheghayyerha SEMICOLON"""
        logger('Role6 : tarifeMotheghayyereMahdud -> jenseMahdud tarifhayeMotheghayyerha ;')

    def p_jenseMahdud(self, p):
        """jenseMahdud : CONSTANT_KW jens
                        | jens
        """
        if len(p) == 3:
            logger('Role7.1 : jenseMahdud -> ثابت jens')
        elif len(p) == 2:
            logger('Role7.2 : jenseMahdud -> jens')

    def p_jens_1(self, p):
        """jens : INTEGER_KW"""
        logger('Role8.1 : jens -> صحیح')

    def p_jens_2(self, p):
        """jens : FLOAT_KW"""
        logger('Role8.2 : jens -> اعشاری')

    def p_jens_3(self, p):
        """jens : BOOLEAN_KW"""
        logger('Role8.3 : jens -> منطقی')

    def p_jens_4(self, p):
        """jens : CHAR_KW"""
        logger('Role8.4 : jens -> حرف')

    def p_tarifeMotheghayyer(self,p):
        """tarifeMotheghayyer : jens tarifhayeMotheghayyerha SEMICOLON"""
        logger('Role9 : tarifeMotheghayyer -> jens tarifhayeMotheghayyerha ;')

    def p_tarifhayeMotegayyerha(self,p):
        """tarifhayeMotheghayyerha : tarifeMeghdareAvvalie
                                |   tarifhayeMotheghayyerha COMMA tarifeMeghdareAvvalie
        """
        if len(p)==2:
            logger('Role10.1 : tarifhayeMotheghayyerha -> tarifeMeghdareAvvalie')
        elif len(p) == 4:
            logger('Role10.2 : tarifhayeMotheghayyerha -> tarifhayeMotheghayyerha , tarifeMeghdareAvvalie')

    def p_tarifeMeghdareAvvalie(self,p):
        """tarifeMeghdareAvvalie : tarifeShenaseyeMoteghayyer
                                |  tarifeShenaseyeMoteghayyer EXP ebarateSade
        """
        if len(p) == 2:
            logger('Role11.1 : tarifeMeghdareAvvalie -> tarifeShenaseyeMoteghayyer')
        elif len(p) == 4:
            logger('Role11.2 : tarifeMeghdareAvvalie -> tarifeShenaseyeMoteghayyer EXP ebarateSade')
    def p_tarifeShenaseyeMoteghayyer(self,p):
        """tarifeShenaseyeMoteghayyer : ID
                                | ID OPENING_BRACKET NUMBER_INT CLOSINGBRACE
        """
        if len(p) == 2 :
            logger('Role12.1 : tarifeShenaseyeMoteghayyer -> ID')
        elif len(p) == 5:
            logger('Role12.1 : tarifeShenaseyeMoteghayyer -> ID [ NUMBER_INT ]')
    def p_tarifeTabe(self,p):
        """tarifeTabe : jens ID OPENING_PARENTHESES vorudi CLOSING_PARENTHESES jomle
                    |   ID OPENING_PARENTHESES vorudi CLOSING_PARENTHESES jomle
        """
        if len(p) == 7:
            logger('Role13.1 tarifeTabe -> jens ID ( vorudi ) jomle')
        elif len(p) == 6:
            logger('Role13.2 tarifeTabe -> ID ( vorudi ) jomle')
    def p_vorudi1(self,p):
        """vorudi : vorudiha"""
        logger('Role14.1 vorudi -> vorudiha')

    def p_vorudi2(self,p):
        """vorudi : empty"""
        logger('Role14.2 vorudi -> 𝜀')

    def p_vorudiha(self,p):
        """vorudiha : vorudiha SEMICOLON jensVorudiha
                    | jensVorudiha
        """
        if len(p) == 4:
            logger('Role15.1 : vorudiha -> vorudiha ; jensVorudiha')
        elif len(p) == 2:
            logger('Role15.2 : vorudiha -> jensVorudiha')

    def p_jensVorudiha(self,p):
        """jensVorudiha : jens shenaseyeVorudiha"""
        logger('Role16 : jensVorudiha -> jens shenaseyeVorudiha')
    def p_shenaseyeVorudiha(self,p):
        """shenaseyeVorudiha : shenaseyeVorudiha COMMA shenaseyeVorudi
                            | shenaseyeVorudi
        """
        if len(p) == 4:
            logger('Role17.1 : shenaseyeVorudiha -> shenaseyeVorudiha , shenaseyeVorudi')
        elif len(p) == 2:
            logger('Role17.2 : shenaseyeVorudiha -> shenaseyeVorudi')

    def p_shenaseyeVorudi(self,p):
        """shenaseyeVorudi : ID
                            | ID OPENING_BRACE CLOSING_BRACE
        """
        if len(p) == 2:
            logger('Role18.1 : shenaseyeVorudi -> ID')
        if len(p) == 4:
            logger('Role18.2 : shenaseyeVorudi -> ID [ ]')
    def p_jomle_1(self,p):
        """jomle : jomleyeMorakkab"""
        logger('Role19.1 : jomle -> jomleyeMorakkab')
    def p_jomle_2(self,p):
        """jomle : jomleyeEbarat"""
        logger('Role19.2 : jomle -> jomleyeEbarat')
    def p_jomle_3(self,p):
        """jomle : jomleyeEntekhab"""
        logger('Role19.3 : jomle -> jomleyeEntekhab')
    def p_jomle_4(self,p):
        """jomle : jomleyeTekrar"""
        logger('Role19.4 : jomle -> jomleyeTekrar')
    def p_jomle_5(self,p):
        """jomle : jomleyeBazgasht"""
        logger('Role19.5 : jomle -> jomleyeBazgasht')
    def p_jomle_6(self,p):
        """jomle : jomleyeShekast"""
        logger('Role19.6 : jomle -> jomleyeShekast')
    def p_jomleyeMorakkab(self,p):
        """jomleyeMorakkab : OPENING_BRACE tarifhayeMahalli jomleha CLOSING_BRACE"""
        logger('Role20 : jomleyeMorakkab -> { tarifhayeMahalli jomleha }')

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
