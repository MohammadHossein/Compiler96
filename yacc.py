from operator import itemgetter

from ply import yacc

import lex
import logging

from Entity import Entity
from QuadRuple import QuadRuple


def logger(p, log):
    # print(log, [str(x) for x in p], sep='\t')
    print(log)
    # pass


class Yacc:
    tokens = lex.Lexer.tokens
    quadRuples = []
    symbolTable = lex.Lexer.sTable

    c = 0

    def newTemp(self):
        self.c += 1
        return 'Temp' + str(self.c)

    precedence = (
        ('left', 'OR_KW', 'THEN_OR_KW'),
        ('left', 'AND_KW', 'THEN_AND_KW'),
        ('left', 'EQ'),
        ('left', 'LT', 'GT', 'LE', 'GE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MOD'),
        ('left', 'MUL', 'DIV'),
        ('right', 'NOT_KW', 'MINUSMINUS', 'PLUSPLUS'),
        ('nonassoc','ELSE_KW')
    )

    def p_barnameh(self, p):
        """barnameh : PROGRAM_KW ID tarifha"""
        logger(p, 'Rule 1 : barnameh -> برنامه SHENASE tarifha')

    def p_tarifha(self, p):
        """tarifha : tarifha tarif
                    | tarif
        """
        if len(p) == 3:
            logger(p, 'Rule 2.1 : tarifha -> tarifha tarif')
        elif len(p) == 2:
            logger(p, 'Rule 2.2 : tarifha -> tarif')

    def p_tarif_1(self, p):
        """tarif : tarifeSakhtar"""
        logger(p, 'Rule 3.1 : tarif -> tarifeSakhtar')

    def p_tarif_2(self, p):
        """tarif : tarifeMotheghayyer"""
        logger(p, 'Rule 3.1 : tarif -> tarifeMotheghayyer')

    def p_tarif_3(self, p):
        """tarif : tarifeTabe"""
        logger(p, 'Rule 3.1 : tarif -> tarifeTabe')

    def p_tarifeSakhtar(self, p):
        """tarifeSakhtar : STRUCTURE_KW ID OPENING_BRACE tarifhayeMahalli CLOSING_BRACE"""
        logger(p, 'Rule 4 : tarifeSakhtar -> ساختار SHENASE { tarifhayeMahalli }')

    def p_tarifhayeMahalli(self, p):
        """tarifhayeMahalli : tarifhayeMahalli tarifeMotheghayyereMahdud
                            | empty
        """
        if len(p) == 3:
            logger(p, 'Rule 5.1: tarifhayeMahalli -> tarifhayeMahalli tarifeMotheghayyereMahdud')
        elif len(p) == 2:
            logger(p, 'Rule 5.2 :tarifhayeMahalli -> 𝜀')

    def p_tarifeMotheghayyereMahdud(self, p):
        """tarifeMotheghayyereMahdud : jenseMahdud tarifhayeMotheghayyerha SEMICOLON"""
        logger(p, 'Rule 6 : tarifeMotheghayyereMahdud -> jenseMahdud tarifhayeMotheghayyerha ;')

    def p_jenseMahdud(self, p):
        """jenseMahdud : CONSTANT_KW jens
                        | jens
        """
        if len(p) == 3:
            logger(p, 'Rule 7.1 : jenseMahdud -> ثابت jens')
        elif len(p) == 2:
            logger(p, 'Rule 7.2 : jenseMahdud -> jens')

    def p_jens_1(self, p):
        """jens : INTEGER_KW"""
        logger(p, 'Rule 8.1 : jens -> صحیح')

    def p_jens_2(self, p):
        """jens : FLOAT_KW"""
        logger(p, 'Rule 8.2 : jens -> اعشاری')

    def p_jens_3(self, p):
        """jens : BOOLEAN_KW"""
        logger(p, 'Rule 8.3 : jens -> منطقی')

    def p_jens_4(self, p):
        """jens : CHAR_KW"""
        logger(p, 'Rule 8.4 : jens -> حرف')

    def p_tarifeMotheghayyer(self, p):
        """tarifeMotheghayyer : jens tarifhayeMotheghayyerha SEMICOLON"""
        logger(p, 'Rule 9 : tarifeMotheghayyer -> jens tarifhayeMotheghayyerha ;')

    def p_tarifhayeMotegayyerha(self, p):
        """tarifhayeMotheghayyerha : tarifeMeghdareAvvalie
                                |   tarifhayeMotheghayyerha COMMA tarifeMeghdareAvvalie
        """
        if len(p) == 2:
            logger(p, 'Rule 10.1 : tarifhayeMotheghayyerha -> tarifeMeghdareAvvalie')
        elif len(p) == 4:
            logger(p, 'Rule 10.2 : tarifhayeMotheghayyerha -> tarifhayeMotheghayyerha , tarifeMeghdareAvvalie')

    def p_tarifeMeghdareAvvalie(self, p):
        """tarifeMeghdareAvvalie : tarifeShenaseyeMoteghayyer
                                |  tarifeShenaseyeMoteghayyer EXP ebarateSade
        """
        if len(p) == 2:
            logger(p, 'Rule 11.1 : tarifeMeghdareAvvalie -> tarifeShenaseyeMoteghayyer')
        elif len(p) == 4:
            logger(p, 'Rule 11.2 : tarifeMeghdareAvvalie -> tarifeShenaseyeMoteghayyer EXP ebarateSade')

    def p_tarifeShenaseyeMoteghayyer(self, p):
        """tarifeShenaseyeMoteghayyer : ID
                                | ID OPENING_BRACKET NUMBER_INT CLOSING_BRACKET
        """
        if len(p) == 2:
            logger(p, 'Rule 12.1 : tarifeShenaseyeMoteghayyer -> ID')
        elif len(p) == 5:
            logger(p, 'Rule 12.1 : tarifeShenaseyeMoteghayyer -> ID [ NUMBER_INT ]')

    def p_tarifeTabe(self, p):
        """tarifeTabe : jens ID OPENING_PARENTHESES vorudi CLOSING_PARENTHESES jomle
                    |   ID OPENING_PARENTHESES vorudi CLOSING_PARENTHESES jomle
        """
        if len(p) == 7:
            logger(p, 'Rule 13.1 tarifeTabe -> jens ID ( vorudi ) jomle')
        elif len(p) == 6:
            logger(p, 'Rule 13.2 tarifeTabe -> ID ( vorudi ) jomle')

    def p_vorudi1(self, p):
        """vorudi : vorudiha"""
        logger(p, 'Rule 14.1 vorudi -> vorudiha')

    def p_vorudi2(self, p):
        """vorudi : empty"""
        logger(p, 'Rule 14.2 vorudi -> 𝜀')

    def p_vorudiha(self, p):
        """vorudiha : vorudiha SEMICOLON jensVorudiha
                    | jensVorudiha
        """
        if len(p) == 4:
            logger(p, 'Rule 15.1 : vorudiha -> vorudiha ; jensVorudiha')
        elif len(p) == 2:
            logger(p, 'Rule 15.2 : vorudiha -> jensVorudiha')

    def p_jensVorudiha(self, p):
        """jensVorudiha : jens shenaseyeVorudiha"""
        logger(p, 'Rule 16 : jensVorudiha -> jens shenaseyeVorudiha')

    def p_shenaseyeVorudiha(self, p):
        """shenaseyeVorudiha : shenaseyeVorudiha COMMA shenaseyeVorudi
                            | shenaseyeVorudi
        """
        if len(p) == 4:
            logger(p, 'Rule 17.1 : shenaseyeVorudiha -> shenaseyeVorudiha , shenaseyeVorudi')
        elif len(p) == 2:
            logger(p, 'Rule 17.2 : shenaseyeVorudiha -> shenaseyeVorudi')

    def p_shenaseyeVorudi(self, p):
        """shenaseyeVorudi : ID
                            | ID OPENING_BRACE CLOSING_BRACE
        """
        if len(p) == 2:
            logger(p, 'Rule 18.1 : shenaseyeVorudi -> ID')
        if len(p) == 4:
            logger(p, 'Rule 18.2 : shenaseyeVorudi -> ID [ ]')

    def p_jomle_1(self, p):
        """jomle : jomleyeMorakkab"""
        logger(p, 'Rule 19.1 : jomle -> jomleyeMorakkab')

    def p_jomle_2(self, p):
        """jomle : jomleyeEbarat"""
        logger(p, 'Rule 19.2 : jomle -> jomleyeEbarat')

    def p_jomle_3(self, p):
        """jomle : jomleyeEntekhab"""
        logger(p, 'Rule 19.3 : jomle -> jomleyeEntekhab')

    def p_jomle_4(self, p):
        """jomle : jomleyeTekrar"""
        logger(p, 'Rule 19.4 : jomle -> jomleyeTekrar')

    def p_jomle_5(self, p):
        """jomle : jomleyeBazgasht"""
        logger(p, 'Rule 19.5 : jomle -> jomleyeBazgasht')

    def p_jomle_6(self, p):
        """jomle : jomleyeShekast"""
        logger(p, 'Rule 19.6 : jomle -> jomleyeShekast')

    def p_jomleyeMorakkab(self, p):
        """jomleyeMorakkab : OPENING_BRACE tarifhayeMahalli jomleha CLOSING_BRACE"""
        logger(p, 'Rule 20 : jomleyeMorakkab -> { tarifhayeMahalli jomleha }')

    def p_jomleha(self, p):
        """jomleha : jomleha jomle
                    | empty
        """
        if len(p) == 3:
            logger(p, 'Rule 21.1 : jomleha -> jomleha jomle')
        elif len(p) == 2:
            logger(p, 'Rule 21.2 : jomleha -> 𝜀')

    def p_jomleyeEbarat(self, p):
        """jomleyeEbarat : ebarat SEMICOLON
        """
        if len(p) == 3:
            logger(p, 'Rule 22.1 : jomleyeEbarat -> ebarat ;')
        elif len(p) == 2:
            logger(p, 'Rule 22.2 : jomleyeEbarat -> ;')

    def p_jomleyeEntekhab(self, p):
        """jomleyeEntekhab : IF_KW ebarateSade THEN_KW jomle
                        | IF_KW ebarateSade THEN_KW jomle ELSE_KW jomle
                        | SWITCH_KW OPENING_PARENTHESES ebarateSade CLOSING_PARENTHESES onsoreHalat onsorePishfarz END_KW
        """
        if len(p) == 5:
            logger(p, 'Rule 23.1 : jomleyeEntekhab -> اگر ebarateSade آنگاه jomle')
        if len(p) == 7:
            logger(p, 'Rule 23.2 : jomleyeEntekhab -> اگر ebarateSade آنگاه jomle وگرنه jomle')
        if len(p) == 8:
            logger(p, 'Rule 23.3 : jomleyeEntekhab -> کلید ( ebarateSade ) onsoreHalat onsorePishfarz تمام')

    def p_onsoreHalat(self, p):
        """onsoreHalat : CASE_KW NUMBER_INT COLON jomle
                    |   onsoreHalat CASE_KW NUMBER_INT COLON jomle
        """
        if len(p) == 6:
            logger(p, 'Rule 24.1 : onsoreHalat -> حالت NUMBER_INT : jomle ;')
        elif len(p) == 7:
            logger(p, 'Rule 24.2 : onsoreHalat -> onsoreHalat حالت NUMBER_INT : jomle ;')

    def p_onsorePishfarz(self, p):
        """onsorePishfarz : DEFAULT_KW COLON jomle
                        |   empty
        """
        if len(p) == 4:
            logger(p, 'Rule 25.1 : onsorePishfarz -> پیشفرض : jomle ;')
        elif len(p) == 2:
            logger(p, 'Rule 25.1 : onsorePishfarz -> 𝜀')

    def p_jomleyeTekrar(self, p):
        """jomleyeTekrar : WHILE_KW OPENING_PARENTHESES ebarateSade CLOSING_PARENTHESES jomle"""

        logger(p, 'Rule 26 : jomleyeTekrar -> وقتی ( ebarateSade ) jomle')

    def p_jomleyeBazgasht(self, p):
        """jomleyeBazgasht : RETURN_KW SEMICOLON
                        |   RETURN_KW ebarat SEMICOLON
        """
        if len(p) == 3:
            logger(p, 'Rule 27.1 : jomleyeBazgasht -> برگردان ;')
        if len(p) == 4:
            logger(p, 'Rule 27.1 : jomleyeBazgasht -> برگردان ebarat ;')

    def p_jomleyeShekast(self, p):
        """jomleyeShekast : BREAK_KW SEMICOLON"""
        logger(p, 'Rule 28 : jomleyeShekast -> بشکن ;')

    def p_ebarat_1(self, p):
        """ebarat : taghirpazir EXP ebarat"""
        # TODO
        p[0] = Entity()
        if p[3].type == 'arith':
            self.quadRuples.append(QuadRuple('', p[3].place, '', p[1].place))
        elif p[3].type == 'bool':
            Entity.backpatch(p[3].trueList, self.quadRuples, len(self.quadRuples))
            self.quadRuples.append(QuadRuple('', '1', '', p[1].place))
            self.quadRuples.append(QuadRuple('', '', '', 'goto' + str(len(self.quadRuples) + 2)))
            Entity.backpatch(p[3].falseList, self.quadRuples, len(self.quadRuples))
            self.quadRuples.append(QuadRuple('', '0', '', p[1].place))

        logger(p, 'Rule 29.1 : ebarat -> taghirpazir = ebarat')

    def p_ebarat_2(self, p):
        """ebarat : taghirpazir PLUS_EXP ebarat"""
        p[0] = Entity()
        self.quadRuples.append(QuadRuple('+', p[1].place, p[3].place, p[1].place))
        logger(p, 'Rule 29.2 : ebarat -> taghirpazir += ebarat')

    def p_ebarat_3(self, p):
        """ebarat : taghirpazir MINUS_EXP ebarat"""
        p[0] = Entity()
        self.quadRuples.append(QuadRuple('-', p[1].place, p[3].place, p[1].place))
        logger(p, 'Rule 29.3 : ebarat -> taghirpazir -= ebarat')

    def p_ebarat_4(self, p):
        """ebarat : taghirpazir MUL_EXP ebarat"""
        p[0] = Entity()
        self.quadRuples.append(QuadRuple('*', p[1].place, p[3].place, p[1].place))
        logger(p, 'Rule 29.4 : ebarat -> taghirpazir *= ebarat')

    def p_ebarat_5(self, p):
        """ebarat : taghirpazir DIV_EXP ebarat"""
        p[0] = Entity()
        self.quadRuples.append(QuadRuple('/', p[1].place, p[3].place, p[1].place))
        logger(p, 'Rule 29.5 : ebarat -> taghirpazir /= ebarat')

    def p_ebarat_6(self, p):
        """ebarat : taghirpazir PLUSPLUS"""
        p[0] = Entity()
        self.quadRuples.append(QuadRuple('+', p[1].place, '1', p[1].place))
        logger(p, 'Rule 29.6 : ebarat -> taghirpazir ++')

    def p_ebarat_7(self, p):
        """ebarat : taghirpazir MINUSMINUS"""
        p[0] = Entity()
        self.quadRuples.append(QuadRuple('-', p[1].place, '1', p[1].place))
        logger(p, 'Rule 29.7 : ebarat -> taghirpazir --')

    def p_ebarat_8(self, p):
        """ebarat : ebarateSade"""
        p[0] = p[1]
        logger(p, 'Rule 29.8 : ebarat -> ebarateSade')

    def p_ebarateSade_1(self, p):
        """ebarateSade : ebarateSade THEN_OR_KW ebarateSade"""
        logger(p, 'Rule 30.1 : ebarateSade -> ebarateSade یاوگرنه ebarateSade')

    def p_ebarateSade_2(self, p):
        """ebarateSade : ebarateSade THEN_AND_KW ebarateSade"""
        logger(p, 'Rule 30.2 : ebarateSade -> ebarateSade وهمچنین ebarateSade')

    def p_ebarateSade_3(self, p):  # TODO
        """ebarateSade : ebarateSade OR_KW empty ebarateSade"""  # M -> empty added
        p[0] = Entity()
        if p[1].type == 'bool' and p[4].type == 'bool':
            Entity.backpatch(p[1].falseList, self.quadRuples, p[3].quad)
            p[0].trueList = p[1].trueList + p[4].trueList
            p[0].falseList = p[4].falseList
            p[0].type = 'bool'
        elif p[1].type == 'bool' and p[4].type == 'arith':
            temp = Entity()
            temp.trueList.append(len(self.quadRuples))
            self.quadRuples.append(QuadRuple('>',p[4].place,'0','goto'))    # TODO - chekc shavad ke > bozorgtar ast ya kuchektar
            temp.falseList.append(len(self.quadRuples))
            self.quadRuples.append(QuadRuple('','','','goto'))
            p[0].trueList = p[1].trueList + [len(self.quadRuples)]
            Entity.backpatch(p[1].falseList, self.quadRuples, p[3].quad)
            p[0].trueList = p[1].trueList + temp.trueList
            p[0].falseList = temp.falseList
            p[0].type = 'bool'

        logger(p, 'Rule 30.3 : ebarateSade -> ebarateSade یا ebarateSade')

    def p_ebarateSade_4(self, p):
        """ebarateSade : ebarateSade AND_KW ebarateSade"""
        logger(p, 'Rule 30.4 : ebarateSade -> ebarateSade و ebarateSade')

    def p_ebarateSade_5(self, p):
        """ebarateSade : NOT_KW ebarateSade"""
        p[0] = Entity()
        p[0].trueList = p[1].falseList
        p[0].falseList = p[1].trueList
        logger(p, 'Rule 30.5 : ebarateSade -> ! ebarateSade')

    def p_ebarateSade_6(self, p):
        """ebarateSade : ebarateRabetei"""
        p[0] = p[1]
        logger(p, 'Rule 30.6 : ebarateSade -> ebarateRabetei')

    def p_ebarateRabetei_1(self, p):
        """ebarateRabetei : ebarateRiaziManteghi"""
        p[0] = p[1]
        logger(p, 'Rule 31.1 : ebarateRabetei -> ebarateRiaziManteghi')

    def p_ebarateRabetei_2(self, p):
        """ebarateRabetei : ebarateRiaziManteghi amalgareRabetei ebarateRiaziManteghi"""
        p[0] = Entity()
        p[0].trueList.append(len(self.quadRuples))
        p[0].falseList.append(len(self.quadRuples) + 1)
        print(p[0])
        self.quadRuples.append(QuadRuple(p[2].place, p[1].place, p[3].place, 'goto'))
        self.quadRuples.append(QuadRuple('', '', '', 'goto'))
        p[0].type = 'bool'
        logger(p, 'Rule 31.2 : ebarateRabetei -> ebarateRiaziManteghi amalgareRabetei ebarateRiaziManteghi')

    def p_amalgareRabetei_1(self, p):
        """amalgareRabetei : LT"""
        p[0] = Entity()
        p[0].place = p[1]
        logger(p, 'Rule 32.1 : amalgareRabetei -> <')

    def p_amalgareRabetei_2(self, p):
        """amalgareRabetei : LE"""
        p[0] = Entity()
        p[0].place = p[1]
        logger(p, 'Rule 32.2 : amalgareRabetei -> <=')

    def p_amalgareRabetei_3(self, p):
        """amalgareRabetei : EQ"""
        p[0] = Entity()
        p[0].place = p[1]
        logger(p, 'Rule 32.3 : amalgareRabetei -> ==')

    def p_amalgareRabetei_4(self, p):
        """amalgareRabetei : GE"""
        p[0] = Entity()
        p[0].place = p[1]
        logger(p, 'Rule 32.4 : amalgareRabetei -> >=')

    def p_amalgareRabetei_5(self, p):
        """amalgareRabetei : GT"""
        p[0] = Entity()
        p[0].place = p[1]
        logger(p, 'Rule 32.5 : amalgareRabetei -> >')

    def p_ebarateRiaziManteghi_1(self, p):
        """ebarateRiaziManteghi : ebarateYegani"""
        p[0] = p[1]
        logger(p, 'Rule 33.1 : ebarateRiaziManteghi -> ebarateYegani')

    def p_ebarateRiaziManteghi_2(self, p):
        """ebarateRiaziManteghi : ebarateRiaziManteghi PLUS ebarateRiaziManteghi
                                | ebarateRiaziManteghi MINUS ebarateRiaziManteghi
                                | ebarateRiaziManteghi MUL ebarateRiaziManteghi
                                | ebarateRiaziManteghi DIV ebarateRiaziManteghi
                                | ebarateRiaziManteghi MOD ebarateRiaziManteghi """
        p[0] = Entity()
        print(p[1], p[3], sep='\n')
        p[0].place = self.newTemp()
        if p[1].type == 'arith' and p[3].type == 'arith':
            self.quadRuples.append(QuadRuple(p[2], p[1].place, p[3].place, p[0].place))
            # self.quadRuples.append(QuadRuple(p[2].place, p[1].place, p[3].place, p[0].place))
        elif p[1].type == 'arith' and p[3].type == 'bool':
            Entity.backpatch(p[3].trueList, self.quadRuples, len(self.quadRuples))
            self.quadRuples.append(QuadRuple(p[2], p[1].place, '1', p[0].place))
            # self.quadRuples.append(QuadRuple(p[2].place, p[1].place, '1', p[0].place))
            self.quadRuples.append(QuadRuple('', '', '', 'goto ' + str(len(self.quadRuples) + 2)))
            Entity.backpatch(p[3].falseList, self.quadRuples, len(self.quadRuples))
            self.quadRuples.append(QuadRuple(p[2], p[1].place, '0', p[0].place))
            # self.quadRuples.append(QuadRuple(p[2].place, p[1].place, '0', p[0].place))
        elif p[1].type == 'bool' and p[3].type == 'arith':
            Entity.backpatch(p[1].trueList, self.quadRuples, len(self.quadRuples))
            self.quadRuples.append(QuadRuple(p[2], p[3].place, '1', p[0].place))
            # self.quadRuples.append(QuadRuple(p[2].place, p[3].place, '1', p[0].place))
            self.quadRuples.append(QuadRuple('', '', '', 'goto ' + str(len(self.quadRuples) + 2)))
            Entity.backpatch(p[1].falseList, self.quadRuples, len(self.quadRuples))
            self.quadRuples.append(QuadRuple(p[2], p[3].place, '0', p[0].place))
            # self.quadRuples.append(QuadRuple(p[2].place, p[3].place, '0', p[0].place))
        elif p[3].type == 'bool' and p[1].type == 'bool':
            t1 = self.newTemp()
            Entity.backpatch(p[1].trueList, self.quadRuples, len(self.quadRuples))
            self.quadRuples.append(QuadRuple('', '1', '', t1))
            self.quadRuples.append(QuadRuple('', '', '', 'goto ' + str(len(self.quadRuples) + 2)))
            Entity.backpatch(p[1].falseList, self.quadRuples, len(self.quadRuples))
            self.quadRuples.append(QuadRuple('', '0', '', t1))
            self.quadRuples.append(QuadRuple('', '', '', 'goto ' + str(p[3].trueList[0])))
            Entity.backpatch(p[3].trueList, self.quadRuples, len(self.quadRuples))
            self.quadRuples.append(QuadRuple('+', t1, '1', p[0].place))
            self.quadRuples.append(QuadRuple('', '', '', 'goto ' + str(len(self.quadRuples) + 2)))
            Entity.backpatch(p[3].falseList, self.quadRuples, len(self.quadRuples))
            self.quadRuples.append(QuadRuple('', t1, '', p[0].place))
        else:
            print('Ridiiiiiiiiiiiim')

        p[0].type = 'arith'
        logger(p, 'Rule 33.2 : ebarateRiaziManteghi -> ebarateRiaziManteghi amalgareRiazi ebarateRiaziManteghi')

    # def p_amalgareRiazi_1(self, p):
    #     """amalgareRiazi : MINUS"""
    #     p[0] = Entity()
    #     p[0].place = '-'
    #     logger(p, 'Rule 34.1 : amalgareRiazi -> -')
    #
    # def p_amalgareRiazi_2(self, p):
    #     """amalgareRiazi : MUL"""
    #     p[0] = Entity()
    #     p[0].place = '*'
    #     logger(p, 'Rule 34.2 : amalgareRiazi -> *')
    #
    # def p_amalgareRiazi_3(self, p):
    #     """amalgareRiazi :  PLUS """
    #     p[0] = Entity()
    #     p[0].place = '+'
    #     logger(p, 'Rule 34.3 : amalgareRiazi -> +')
    #
    # def p_amalgareRiazi_4(self, p):
    #     """amalgareRiazi : DIV"""
    #     p[0] = Entity()
    #     p[0].place = '/'
    #     logger(p, 'Rule 34.4 : amalgareRiazi -> /')
    #
    # def p_amalgareRiazi_5(self, p):
    #     """amalgareRiazi : MOD"""
    #     p[0] = Entity()
    #     p[0].place = '%'
    #     logger(p, 'Rule 34.5 : amalgareRiazi -> %')

    def p_ebarateYegani_1(self, p):
        # TODO
        """ebarateYegani : amalgareYegani ebarateYegani"""
        logger(p, 'Rule 35.1 : ebarateYegani -> amalgareYegani ebarateYegani')

    def p_ebarateYegani_2(self, p):
        """ebarateYegani : amel"""
        p[0] = p[1]
        logger(p, 'Rule 35.2 : ebarateYegani -> amel')

    def p_amalgareYegani_1(self, p):
        """amalgareYegani : MINUS"""
        logger(p, 'Rule 36.1 : amalgareYegani -> -')

    def p_amalgareYegani_2(self, p):
        """amalgareYegani : MUL"""
        logger(p, 'Rule 36.2 : amalgareYegani -> *')

    def p_amalgareYegani_3(self, p):
        """amalgareYegani : QUESTION_MARK"""
        logger(p, 'Rule 36.3 : amalgareYegani -> ?')

    def p_amel_1(self, p):
        """amel : taghirpazir"""
        p[0] = p[1]
        logger(p, 'Rule 37.1 : amel -> taghirpazir')

    def p_amel_2(self, p):
        """amel : taghirnapazir"""
        p[0] = p[1]
        logger(p, 'Rule 37.2 : amel -> taghirnapazir')

    def p_taghirpazir_1(self, p):
        """taghirpazir : ID"""
        logger(p, 'Rule 38.1 : taghirpazir -> ID')
        p[0] = Entity()
        p[0].place = p[1]

    def p_taghirpazir_2(self, p):
        # TODO
        """taghirpazir : taghirpazir OPENING_BRACKET ebarat CLOSING_BRACKET"""
        logger(p, 'Rule 38.2 : taghirpazir -> taghirpazir [ ebarat ]')

    def p_taghirpazir_3(self, p):
        """taghirpazir :  taghirpazir DOT ID"""
        logger(p, 'Rule 38.3 : taghirpazir -> taghirpazir . ID')

    def p_taghirnapazir_1(self, p):
        """taghirnapazir : OPENING_PARENTHESES ebarat CLOSING_PARENTHESES"""
        p[0] = p[2]
        logger(p, 'Rule 39.1 : taghirnapazir -> (ebarat)')

    def p_taghirnapazir_2(self, p):
        """taghirnapazir : sedaZadan"""
        logger(p, 'Rule 39.2 : taghirnapazir -> sedaZadan')

    def p_taghirnapazir_3(self, p):
        """taghirnapazir : meghdareSabet"""
        p[0] = p[1]
        p[0].type = 'arith'
        logger(p, 'Rule 39.3 : taghirnapazir -> meghdareSabet')

    def p_sedaZadan(self, p):
        """sedaZadan : ID OPENING_PARENTHESES bordareVorudi CLOSING_PARENTHESES"""
        logger(p, 'Rule 40 : sedaZadan -> ID ( bordareVorudi )')

    def p_bordareVorudi_1(self, p):
        # TODO
        """bordareVorudi : bordareVorudiha"""
        logger(p, 'Rule 41.1 : bordareVorudi -> bordareVorudiha')

    def p_bordareVorudi_2(self, p):
        """bordareVorudi : empty"""
        logger(p, 'Rule 41.2 : bordareVorudi -> ϵ')

    def p_bordareVorudiha(self, p):
        """bordareVorudiha : bordareVorudiha COMMA
                            | ebarat
        """
        if len(p) == 3:
            logger(p, 'Rule 42.1: bordareVorudiha -> bordareVorudiha ,')
        elif len(p) == 2:
            logger(p, 'Rule 42.2 :bordareVorudiha -> ebarat')

    def p_meghdareSabet_1(self, p):
        """meghdareSabet : NUMBER_INT"""
        p[0] = Entity()
        p[0].place = p[1]
        logger(p, 'Rule 43.1 : meghdareSabet -> NUMBER_INT')

    def p_meghdareSabet_2(self, p):
        """meghdareSabet : NUMBER_FLOAT"""
        p[0] = Entity()
        p[0].place = p[1]
        logger(p, 'Rule 43.2 : meghdareSabet -> NUMBER_FLOAT')

    def p_meghdareSabet_3(self, p):
        """meghdareSabet : FIXED_CHARACTER"""
        p[0] = Entity()
        p[0].place = p[1]
        logger(p, 'Rule 43.3 : meghdareSabet -> FIXED_CHARACTER')

    def p_meghdareSabet_4(self, p):
        """meghdareSabet : TRUE_KW"""
        p[0] = Entity()
        p[0].place = p[1]
        logger(p, 'Rule 43.4 : meghdareSabet -> TRUE_KW')

    def p_meghdareSabet_5(self, p):
        """meghdareSabet : FALSE_KW"""
        p[0] = Entity()
        p[0].place = p[1]
        logger(p, 'Rule 43.4 : meghdareSabet -> FALSE_KW')

    def p_error(self, p):
        print('syntax error')
        # if p:
        #     print("Syntax error at token", p.type)
        #     Just discard the token and tell the parser it's okay.
        # self.parser.errok()
        # else:
        #     print("Syntax error at EOF")

    # Empty Rule

    def p_empty(self, p):
        """
        empty :
        """
        p[0] = Entity()
        p[0].quad = len(self.quadRuples)

    def build(self, **kwargs):
        """
        build the parser
        """
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
