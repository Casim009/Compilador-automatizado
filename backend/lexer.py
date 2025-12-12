"""
Analizador Léxico para el Mini-Compilador

Secciones principales:
1. Palabras reservadas:
   - Diccionario `reserved`: Define palabras clave como `int`, `float`, `if`, `else`, etc.

2. Tokens:
   - Lista de tokens reconocidos por el analizador léxico.
   - Incluye operadores, delimitadores y literales.
"""
import ply.lex as lex

# Palabras reservadas
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'bool': 'BOOL',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'print': 'PRINT',
    'true': 'TRUE',
    'false': 'FALSE'
}

# Lista de tokens
tokens = [
    'ID',           # Identificadores
    'NUMBER',       # Números enteros
    'FNUMBER',      # Números flotantes
    'PLUS',         # +
    'MINUS',        # -
    'TIMES',        # *
    'DIVIDE',       # /
    'ASSIGN',       # =
    'EQ',           # ==
    'NE',           # !=
    'LT',           # <
    'LE',           # <=
    'GT',           # >
    'GE',           # >=
    'AND',          # &&
    'OR',           # ||
    'NOT',          # !
    'LPAREN',       # (
    'RPAREN',       # )
    'LBRACE',       # {
    'RBRACE',       # }
    'SEMICOLON',    # ;
    'COMMA',        # ,
] + list(reserved.values())

# Reglas de tokens simples
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_ASSIGN    = r'='
t_EQ        = r'=='
t_NE        = r'!='
t_LT        = r'<'
t_LE        = r'<='
t_GT        = r'>'
t_GE        = r'>='
t_AND       = r'&&'
t_OR        = r'\|\|'
t_NOT       = r'!'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_SEMICOLON = r';'
t_COMMA     = r','

# Ignorar espacios y tabs
t_ignore = ' \t'

# Número flotante
def t_FNUMBER(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Número entero
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Identificadores y palabras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Comentarios
def t_COMMENT(t):
    r'//.*'
    pass

# Error léxico
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en línea {t.lineno}")
    t.lexer.skip(1)

# ============================
# Construcción del Lexer
# ============================

def build_lexer():
    """Construye el lexer global (para el parser)."""
    global lexer
    lexer = lex.lex()
    return lexer

def build():
    """Interfaz estándar para el parser."""
    return build_lexer()

# Construir automáticamente el lexer al importar
lexer = lex.lex()

# ============================
# Función pública de análisis
# ============================

def analyze(code):
    lexer.input(code)
    tokens_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_list.append({
            'type': tok.type,
            'value': str(tok.value),
            'line': tok.lineno,
            'position': tok.lexpos
        })
    return tokens_list

# ============================
# Pruebas
# ============================

if __name__ == '__main__':
    test_code = '''
    int x = 5;
    float y = 3.14;
    if (x > 0) {
        print(x);
    }
    '''
    result = analyze(test_code)
    for token in result:
        print(token)
