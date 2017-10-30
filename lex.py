class Lexer:
    tokens = ('ID',
              'NUMBER',
              'FIXED_CHARACTER',
              'BLANK',
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

    """آ|ا|ب|پ|ت|ث|ج|چ|ح|خ|د|ذ|ر|ز|ژ|س|ش|ص|ض|ط|ظ|ع|غ|ف|ق|ک|گ|ل|م|ن|و|ه|ی"""
    t_ID = r'[][]+'
    t_NUMBER = r''
    t_FIXED_CHARACTER = r''
    t_BLANK = r''
    t_SEMICOLON = r''
    t_COMMA = r''
    t_COMMENT = r''
    t_PROGRAM_KW = r''
    t_STRUCTURE_KW = r''
    t_OPENING_BRACE = r''
    t_CLOSING_BRACE_K = r''
    t_CONSTANT_KW = r''
    t_CHAR_KW = r''
    t_BOOLEAN_KW = r''
    t_FLOAT_KW = r''
    t_INTEGER_KW = r''
    t_OPENING_BRACKET = r''
    t_CLOSING_BRACKET = r''
    t_OPENING_PARENTHESES = r''
    t_COSING_PARENTHESES = r''
    t_IF_KW = r''
    t_THEN_KW = r''
    t_ELSE_KW = r''
    t_SWITCH_KW = r''
    t_END_KW = r''
    t_CASE_KW = r''
    t_COLON = r''
    t_DEFAULT_KW = r''
    t_WHILE_KW = r''
    t_RETURN_KW = r''
    t_BREAK_KW = r''
    t_EXP = r''
    t_PLUS_EXP = r''
    t_MINUS_EXP = r''
    t_MUL_EXP = r''
    t_DIV_EXP = r''
    t_PLUSPLUS = r''
    t_MINUSMINUS = r''
    t_CIRCUIT_OR_KW = r''
    t_CIRCUIT_AND_KW = r''
    t_OR_KW = r''
    t_AND_KW = r''
    t_NOT_KW = r''
    t_LT = r''
    t_LE = r''
    t_EQ = r''
    t_GE = r''
    t_G = r''
    t_PLUS = r''
    t_MINUS = r''
    t_MUL = r''
    t_DIV = r''
    t_MOD = r''
    t_QUESTION_MARK = r''
    t_DOT = r''
    t_TRUE_KW = r''
    t_FALSE_KW = r''
    t_MAIN = r''
