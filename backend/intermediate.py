# intermediate.py
"""
Generador simple de cuádruplos.
Expone: generate_intermediate_code(ast) -> {'success': True, 'quadruples': [...]}
Cuádruplo: (op, arg1, arg2, result)
op puede ser: '+','-','*','/','assign','print','jfalse','goto','label','and','or','not'
"""

temp_counter = 0
label_counter = 0


# --------------------------
# Generadores de nombres
# --------------------------
def new_temp():
    global temp_counter
    t = f"t{temp_counter}"
    temp_counter += 1
    return t

def new_label():
    global label_counter
    l = f"L{label_counter}"
    label_counter += 1
    return l


# --------------------------
# Expresiones
# --------------------------
def gen_expr(node, quads):
    if not isinstance(node, dict):
        raise Exception(f"Nodo inválido en gen_expr: {node}")

    ntype = node.get('node')

    # --- LITERALES ---
    if ntype in ('number', 'fnumber', 'bool'):
        t = new_temp()
        quads.append(('assign', node['value'], None, t))
        return t

    # --- IDENTIFICADORES ---
    if ntype == 'id':
        return node.get('name')

    # --- BINARIOS ---
    if ntype == 'binop':
        op = node.get('op')

        # normaliza operadores lógicos
        if op == '&&':
            op = 'and'
        elif op == '||':
            op = 'or'

        left = gen_expr(node['left'], quads)
        right = gen_expr(node['right'], quads)
        t = new_temp()
        quads.append((op, left, right, t))
        return t

    # --- UNARIOS ---
    if ntype == 'unop':
        op = node.get('op')
        val = gen_expr(node['expr'], quads)
        t = new_temp()
        quads.append(('not', val, None, t))
        return t

    raise NotImplementedError(f"gen_expr no soporta nodo: {ntype}")


# --------------------------
# Sentencias
# --------------------------
def gen_stmt(s, quads):
    ntype = s.get('node')

    # --- DECLARACIÓN ---
    if ntype == 'decl':
        t = gen_expr(s['expr'], quads)
        quads.append(('assign', t, None, s['id']))

    # --- ASIGNACIÓN ---
    elif ntype == 'assign':
        t = gen_expr(s['expr'], quads)
        quads.append(('assign', t, None, s['id']))

    # --- PRINT ---
    elif ntype == 'print':
        t = gen_expr(s['expr'], quads)
        quads.append(('print', t, None, None))

    # --- IF ---
    elif ntype == 'if':
        cond_temp = gen_expr(s['cond'], quads)
        label_else = new_label()
        label_end = new_label()

        quads.append(('jfalse', cond_temp, None, label_else))

        # bloque entonces
        for st in s.get('then', []):
            gen_stmt(st, quads)

        quads.append(('goto', None, None, label_end))

        # etiqueta ELSE
        quads.append(('label', label_else, None, None))

        # bloque else
        for st in s.get('otherwise', []):
            gen_stmt(st, quads)

        quads.append(('label', label_end, None, None))

    # --- WHILE ---
    elif ntype == 'while':
        lbl_start = new_label()
        lbl_end = new_label()

        quads.append(('label', lbl_start, None, None))
        cond_temp = gen_expr(s['cond'], quads)
        quads.append(('jfalse', cond_temp, None, lbl_end))

        for st in s.get('body', []):
            gen_stmt(st, quads)

        quads.append(('goto', None, None, lbl_start))
        quads.append(('label', lbl_end, None, None))

    else:
        raise NotImplementedError(f"gen_stmt no soporta {ntype}")


# --------------------------
# Entrada principal
# --------------------------
def generate_intermediate_code(ast):
    global temp_counter, label_counter
    temp_counter = 0
    label_counter = 0
    quads = []

    try:
        if ast.get('node') != 'program':
            return {'success': False, 'error': 'AST no es un programa'}

        for s in ast.get('stmts', []):
            gen_stmt(s, quads)

        return {'success': True, 'quadruples': quads}

    except Exception as e:
        return {'success': False, 'error': str(e)}



# Prueba rápida
if __name__ == "__main__":
    test_ast = {
        'node': 'program',
        'stmts': [
            {'node': 'decl', 'id': 'x', 'expr': {'node': 'number', 'value': 5}},
            {'node': 'assign', 'id': 'x',
             'expr': {'node': 'binop', 'op': '+',
                      'left': {'node':'id','name':'x'},
                      'right': {'node':'number','value':3}}}
        ]
    }
    print(generate_intermediate_code(test_ast))
