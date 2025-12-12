# parser.py
"""
Parser simple con PLY.

Secciones principales:
1. Representación de nodos:
   - node(type_, **kwargs): Crea nodos serializables para el AST.

2. Precedencias:
   - Tupla `precedence`: Define la precedencia de operadores como `+`, `*`, `AND`, etc.

3. Gramática:
   - p_program(p): Regla inicial para el programa.
   - p_stmt_list_multi(p): Maneja múltiples sentencias.
   - p_stmt(p): Define las sentencias válidas (declaraciones, asignaciones, etc.).
"""

import ply.yacc as yacc
from lexer import tokens, build as _build_lexer
import json

# --------------------------------------
#   Representación de nodos serializables
# --------------------------------------
def node(type_, **kwargs):
    d = {'node': type_}
    d.update(kwargs)
    return d

# --------------------------------------
#   Precedencias
# --------------------------------------
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NE'),
    ('nonassoc', 'GT', 'LT', 'GE', 'LE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'NOT'),
)

# --------------------------------------
#   Gramática
# --------------------------------------

def p_program(p):
    "program : stmt_list"
    p[0] = node('program', stmts=p[1])

def p_stmt_list_multi(p):
    "stmt_list : stmt_list stmt"
    p[0] = p[1] + [p[2]]

def p_stmt_list_single(p):
    "stmt_list : stmt"
    p[0] = [p[1]]

def p_stmt(p):
    """stmt : decl_stmt
            | assign_stmt
            | print_stmt
            | if_stmt
            | while_stmt"""
    p[0] = p[1]

def p_decl_stmt(p):
    "decl_stmt : INT ID ASSIGN expr SEMICOLON"
    p[0] = node('decl', type='int', id=p[2], expr=p[4])

def p_assign_stmt(p):
    "assign_stmt : ID ASSIGN expr SEMICOLON"
    p[0] = node('assign', id=p[1], expr=p[3])

def p_print_stmt(p):
    "print_stmt : PRINT LPAREN expr RPAREN SEMICOLON"
    p[0] = node('print', expr=p[3])

def p_if_stmt(p):
    "if_stmt : IF LPAREN expr RPAREN LBRACE stmt_list RBRACE"
    p[0] = node('if', cond=p[3], then=p[6], otherwise=[])

def p_while_stmt(p):
    "while_stmt : WHILE LPAREN expr RPAREN LBRACE stmt_list RBRACE"
    p[0] = node('while', cond=p[3], body=p[6])

def p_expr_binop(p):
    """expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | expr GT expr
            | expr LT expr
            | expr GE expr
            | expr LE expr
            | expr EQ expr
            | expr NE expr
            | expr AND expr
            | expr OR expr
    """
    p[0] = node('binop', op=p[2], left=p[1], right=p[3])

def p_expr_unop(p):
    "expr : NOT expr"
    p[0] = node('unop', op=p[1], expr=p[2])

def p_expr_group(p):
    "expr : LPAREN expr RPAREN"
    p[0] = p[2]

def p_expr_number(p):
    "expr : NUMBER"
    p[0] = node('number', value=p[1])

def p_expr_fnumber(p):
    "expr : FNUMBER"
    p[0] = node('fnumber', value=p[1])

def p_expr_truefalse(p):
    """expr : TRUE
            | FALSE"""
    p[0] = node('bool', value=(p.slice[1].type == "TRUE"))

def p_expr_id(p):
    "expr : ID"
    p[0] = node('id', name=p[1])

def p_error(p):
    if p:
        raise SyntaxError(f"Syntax error at token '{p.value}' (type: {p.type}) line {getattr(p, 'lineno', '?')}")
    else:
        raise SyntaxError("Syntax error at EOF")

# --------------------------------------
#   Construcción única del parser
# --------------------------------------

_parser = None

def _build_parser():
    global _parser
    if _parser is None:
        _build_lexer()     # Asegurar lexer primero
        _parser = yacc.yacc(debug=False)
    return _parser

# --------------------------------------
#   API pública
# --------------------------------------

def parse(source_code):
    try:
        parser = _build_parser()
        ast = parser.parse(source_code)
        return {'success': True, 'ast': ast}
    except Exception as e:
        return {'success': False, 'error': str(e)}

# --------------------------------------
#   Test
# --------------------------------------

if __name__ == "__main__":
    src = """
    int x = 5;
    while (x < 8) {
        print(x);
        x = x + 1;
    }
    """
    res = parse(src)
    print(json.dumps(res, indent=2))
