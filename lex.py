# IN THE NAME OF GOD

import ply.lex as lex


class Lexer:
    tokens = (
        'FIXED_CHARACTER',
        'SEMICOLON',
        'COMMA',
        'PROGRAM_KW',
        'STRUCTURE_KW',
        'OPENING_BRACE',
        'CLOSING_BRACE',
        'CONSTANT_KW',
        'CHAR_KW',
        'BOOLEAN_KW',
        'FLOAT_KW',
        'INTEGER_KW',
        'OPENING_BRACKET',
        'CLOSING_BRACKET',
        'OPENING_PARENTHESES',
        'CLOSING_PARENTHESES',
        'IF_KW',
        'THEN_KW',
        'ELSE_KW',
        'SWITCH_KW',
        'END_KW',
        'CASE_KW',
        'COLON',
        'DEFAULT_KW',
        'WHILE_KW',
        'RETURN_KW',
        'BREAK_KW',
        'EXP',
        'PLUS_EXP',
        'MINUS_EXP',
        'MUL_EXP',
        'DIV_EXP',
        'PLUSPLUS',
        'MINUSMINUS',
        'THEN_OR_KW',
        'THEN_AND_KW',
        'OR_KW',
        'AND_KW',
        'NOT_KW',
        'LT',
        'LE',
        'EQ',
        'GE',
        'GT',
        'PLUS',
        'MINUS',
        'MUL',
        'DIV',
        'MOD',
        'QUESTION_MARK',
        'DOT',
        'TRUE_KW',
        'FALSE_KW',
        # 'MAIN',
        'ID',
        'COMMENT',
        'NUMBER_INT',
        'NUMBER_FLOAT'
    )

    sTable = []

    harf = r'\u0622|\u0627|\u0628|\u067E|\u062A|\u062B|\u062C|\u0686|\u062D|\u062E|\u062F|\u0630|\u0631|\u0632' \
           r'|\u0698|\u0633|\u0634|\u0635|\u0636|\u0637|\u0638|\u0639|\u063A|\u0641|\u0642|\u0643|\u06AF|\u0644' \
           r'|\u0645|\u0646|\u0647|\u0648|\u0649|\u06A9|\u064A|\u06CC|\u06BE|\u06D5|\u06C1|\_'
    adad = r'\u0660|\u0661|\u0662|\u0663|\u0664|\u0665|\u0666|\u0667|\u0668|\u0669|\u06F0|\u06F1|\u06F2|\u06F3' \
           r'|\u06F4|\u06F5|\u06F6|\u06F7|\u06F8|\u06F9|0|1|2|3|4|5|6|7|8|9'
    adadNoneZero = r'\u0661|\u0662|\u0663|\u0664|\u0665|\u0666|\u0667|\u0668|\u0669|\u06F1|\u06F2|\u06F3' \
                   r'|\u06F4|\u06F5|\u06F6|\u06F7|\u06F8|\u06F9|1|2|3|4|5|6|7|8|9'

    semi_colon_farsi = r'\u061B'
    comma_farsi = r'\u060C'

    t_SEMICOLON = r';|' + semi_colon_farsi
    t_COMMA = r',|' + comma_farsi
    t_OPENING_BRACE = r'{'
    t_CLOSING_BRACE = r'}'
    reserved = {
        'برنامه': 'PROGRAM_KW',
        'ساختار': 'STRUCTURE_KW',
        'ثابت': 'CONSTANT_KW',
        'حرف': 'CHAR_KW',
        'منطقی': 'BOOLEAN_KW',
        'اعشاری': 'FLOAT_KW',
        'صحیح': 'INTEGER_KW',
        'اگر': 'IF_KW',
        'آنگاه': 'THEN_KW',
        'وگرنه': 'ELSE_KW',
        'کلید': 'SWITCH_KW',
        'تمام': 'END_KW',
        'حالت': 'CASE_KW',
        'پیشفرض': 'DEFAULT_KW',
        'وقتی': 'WHILE_KW',
        'برگردان': 'RETURN_KW',
        'بشکن': 'BREAK_KW',
        'یا': 'OR_KW',
        'و': 'AND_KW',
        'یاوگرنه': 'THEN_OR_KW',
        'وهمچنین': 'THEN_AND_KW',
        'خلاف': 'NOT_KW',
        'درست': 'TRUE_KW',
        'غلط': 'FALSE_KW',
        # 'اصلی': 'MAIN'
    }

    t_OPENING_BRACKET = r'\['
    t_CLOSING_BRACKET = r'\]'
    t_OPENING_PARENTHESES = r'\('
    t_CLOSING_PARENTHESES = r'\)'

    t_COLON = r':'
    t_EXP = r'='
    t_PLUS_EXP = r'\+='
    t_MINUS_EXP = r'-='
    t_MUL_EXP = r'\*='
    t_DIV_EXP = r'\/='
    t_PLUSPLUS = r'\+\+'
    t_MINUSMINUS = r'--'

    t_LT = r'<'
    t_LE = r'<='
    t_EQ = r'=='
    t_GE = r'>='
    t_GT = r'>'
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_MOD = r'٪|%'
    t_QUESTION_MARK = r'\?|\؟'
    t_DOT = r'\.'

    # t_ID = r'[آ-ی|\_][آ-ی|۰-۹|0-9['
    # t_ID = r'[' + harf + r'][' + harf + r'|' + adad + r']+'
    # def t_NUMBER_INT(self, t):
    #     r'[^\.][\u0660|\u0661|\u0662|\u0663|\u0664|\u0665|\u0666|\u0667|\u0668|\u0669|\u06F0|\u06F1|\u06F2|\u06F3' \
    #        r'|\u06F4|\u06F5|\u06F6|\u06F7|\u06F8|\u06F9|0|1|2|3|4|5|6|7|8|9]+[^\.]'
    #
    #     while (t.value[0] == '0' or t.value[0] == '\u0660' or t.value[0] == '\u06F0') and len(t.value) > 1:
    #         t.value = t.value[1:]
    #
    #     return t
    t_NUMBER_INT = r'[' + adadNoneZero + r']' + r'[' + adad + r']*'
    t_NUMBER_FLOAT = r'(([' + adadNoneZero + r']' + r'[' + adad + r']*)|(0|\u0660|\u06F0))' + r'\.((0|\u0660|\u06F0)|' + r'([' + adad + r']*' + r'[' + adadNoneZero + r']))'

    t_FIXED_CHARACTER = r'\'\\.{1}\''
    t_ignore = ' \t'

    def t_ID(self, t):
        r'[\u0622|\u0627|\u0628|\u067E|\u062A|\u062B|\u062C|\u0686|\u062D|\u062E|\u062F|\u0630|\u0631|\u0632' \
        r'|\u0698|\u0633|\u0634|\u0635|\u0636|\u0637|\u0638|\u0639|\u063A|\u0641|\u0642|\u0643|\u06AF|\u0644' \
        r'|\u0645|\u0646|\u0647|\u0648|\u0649|\u06A9|\u064A|\u06CC|\u06BE|\u06D5|\u06C1|\_][\u0622|\u0627|\u0628|\u067E|\u062A|\u062B|\u062C|\u0686|\u062D|\u062E|\u062F|\u0630|\u0631|\u0632' \
        r'|\u0698|\u0633|\u0634|\u0635|\u0636|\u0637|\u0638|\u0639|\u063A|\u0641|\u0642|\u0643|\u06AF|\u0644' \
        r'|\u0645|\u0646|\u0647|\u0648|\u0649|\u06A9|\u064A|\u06CC|\u06BE|\u06D5|\u06C1|\_|\u0660|\u0661|\u0662|\u0663|\u0664|\u0665|\u0666|\u0667|\u0668|\u0669|\u06F0|\u06F1|\u06F2|\u06F3' \
        r'|\u06F4|\u06F5|\u06F6|\u06F7|\u06F8|\u06F9|0|1|2|3|4|5|6|7|8|9]*'
        t.type = self.reserved.get(t.value, 'ID')  # Check for reserved words
        if t.type == 'ID':
            if t.value not in self.sTable:
                self.sTable.append(t.value)

        return t

    def t_COMMENT(self, t):
        r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/|//.*'
        # r'//.*'
        pass

    def t_newline(self, t):
        r'\r?\n+'
        t.lexer.lineno += t.value.count("\n")

    def t_error(self, t):
        if t.value[0] != "0" and t.value[0] != '\u0660' and t.value[0] != '\u06F0':
            print("Illegal character '%s'" % (t.value[0]))
        t.lexer.skip(1)

    def build(self, **kwargs):
        '''
        build the lexer
        '''
        self.lexer = lex.lex(module=self, **kwargs)

        return self.lexer
