import ply.lex as lex


class Lexer:
    tokens = ('ID',
              'NUMBER',
              'FIXED_CHARACTER',
              'SEMICOLON',
              'COMMA',
              'COMMENT',
              'PROGRAM_KW',
              'STRUCTURE_KW',
              'OPENING_BRACE',
              'CLOSING_BRACE_K',
              'CONSTANT_KW',
              'CHAR_KW',
              'BOOLEAN_KW',
              'FLOAT_KW',
              'INTEGER_KW',
              'OPENING_BRACKET',
              'CLOSING_BRACKET',
              'OPENING_PARENTHESES',
              'COSING_PARENTHESES',
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
              'CIRCUIT_OR_KW',
              'CIRCUIT_AND_KW',
              'OR_KW',
              'AND_KW',
              'NOT_KW',
              'LT',
              'LE',
              'EQ',
              'GE',
              'G',
              'PLUS',
              'MINUS',
              'MUL',
              'DIV',
              'MOD',
              'QUESTION_MARK',
              'DOT',
              'TRUE_KW',
              'FALSE_KW',
              'MAIN',
              )

    harf = r'\u0622|\u0627|\u0628|\u067E|\u062A|\u062B|\u062C|\u0686|\u062D|\u062E|\u062F|\u0630|\u0631|\u0632' \
           r'|\u0698|\u0633|\u0634|\u0635|\u0636|\u0637|\u0638|\u0639|\u063A|\u0641|\u0642|\u0643|\u06AF|\u0644' \
           r'|\u0645|\u0646|\u0647|\u0648|\u0649'
    adad = r'\u0660|\u0661|\u0662|\u0663|\u0664|\u0665|\u0666|\u0667|\u0668|\u0669|\u06F0|\u06F1|\u06F2|\u06F3' \
           r'|\u06F4|\u06F5|\u06F6|\u06F7|\u06F8|\u06F9|0|1|2|3|4|5|6|7|8|9'
    semi_colon_farsi = r'\u061B'
    comma_farsi = r'\u060C'

    t_SEMICOLON = r';'
    t_COMMA = r',|' + comma_farsi

    def t_COMMENT(self, t):
        r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/'
        pass

    t_PROGRAM_KW = r'برنامه'
    t_STRUCTURE_KW = r'ساختار'
    t_OPENING_BRACE = r'}'
    t_CLOSING_BRACE_K = r'{'
    t_CONSTANT_KW = r'ثابت'
    t_CHAR_KW = r'حرف'
    t_BOOLEAN_KW = r'منطقی'

    def t_FLOAT_KW(self, t):
        r'اعشاری'
        try:
            t.value = float(t.value)
        except ValueError:
            print("Float value too large %d", t.value)
            t.value = 0
        return t

    def t_INTEGER_KW(self, t):
        r'صحیح'
        try:
            t.value = int(t.value)
        except ValueError:
            print("Integer value too large %d", t.value)
        return t

    t_OPENING_BRACKET = r'\]'
    t_CLOSING_BRACKET = r'\['
    t_OPENING_PARENTHESES = r'\)'
    t_COSING_PARENTHESES = r'\('
    t_IF_KW = r'اگر'
    t_THEN_KW = r'آنگاه'
    t_ELSE_KW = r'وگرنه'
    t_SWITCH_KW = r'کلید'
    t_END_KW = r'تمام'
    t_CASE_KW = r'حالت'
    t_COLON = r':'
    t_DEFAULT_KW = r'پیشفرض'
    t_WHILE_KW = r'وقتی'
    t_RETURN_KW = r'برگردان'
    t_BREAK_KW = r'بشکن'
    t_EXP = r'='
    t_PLUS_EXP = r'\+='
    t_MINUS_EXP = r'-='
    t_MUL_EXP = r'\*='
    t_DIV_EXP = r'\/='
    t_PLUSPLUS = r'\+\+'
    t_MINUSMINUS = r'--'
    t_CIRCUIT_OR_KW = r'یا'
    t_CIRCUIT_AND_KW = r'و'
    t_OR_KW = r'یا وگرنه'
    t_AND_KW = r'و همچنین'
    t_NOT_KW = r'خلاف'
    t_LT = r'<'
    t_LE = r'<='
    t_EQ = r'=='
    t_GE = r'>='
    t_G = r'>'
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_MOD = r'٪'
    t_QUESTION_MARK = r'\?|\؟'
    t_DOT = r'\.'
    t_TRUE_KW = r'درست'
    t_FALSE_KW = r'غلط'
    t_MAIN = r'اصلی'
    t_ID = r'[' + harf + r'][' + harf + r'|' + adad + r']+'
    t_NUMBER = r'[' + adad + r']+'
    t_FIXED_CHARACTER = r'\\.{1}'
    t_ignore = r' \t\r\f\v'


    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    def t_error(self, t):
        print("Illegal character '%s'" % t.value)
        t.lexer.skip(1)

    def build(self, **kwargs):
        '''
        build the lexer
        '''
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer


# Test it out
data = '''
ساختار فاکتوریل }
صحیح شماره = ۵ ؛
صحیح مقدار؛
}
ساختار ریاضی }
ثابت اعشاری پی = ۳.۱۴ ؛
}
صحیح نتیجه؛
منطقی الکی = غلط؛
حرف بیمقدار؛
صحیح توان_دوم )صحیح عدد( برگردان عدد * عدد؛
صحیح محاسبه_فاکتوریل )صحیح شماره( }
صحیح شمارنده = ۱ ؛
صحیح نتیجه = ۱ ؛
اگر شماره == ۰ یا شماره == ۱ آنگاه }برگردان ۱ }؛
وگرنه }
وقتی )شمارنده >= شماره( }
نتیجه *= شمارنده؛
شمارنده++؛
}
}
}
صحیح اصلی )( }
فاکتوریل.مقدار = محاسبه_فاکتور یل )فاکتوریل.شمار ه(؛
برگردان فاکتوریل.مقدار؛
}
'''
lexer = Lexer().build()
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
