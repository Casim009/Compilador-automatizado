# semantic.py
"""
Análisis semántico simple.
Expone: analyze_semantics(ast) -> {
    'success': True, 
    'symbol_table': {...}
} 
o {
    'success': False, 
    'errors': [...]
}
"""

def analyze_semantics(ast):
    errors = []
    symbols = {}  # name -> {type: 'int', 'value': ...}

    # -----------------------------
    # Función principal de visita
    # -----------------------------
    def visit(node):
        if not isinstance(node, dict):
            return

        ntype = node.get('node')

        # ---- PROGRAM ----
        if ntype == 'program':
            for s in node.get('stmts', []):
                visit(s)

        # ---- DECLARACIÓN ----
        elif ntype == 'decl':
            name = node.get('id')
            if name in symbols:
                errors.append(f"Variable '{name}' ya declarada")
            else:
                expr = node.get('expr')
                val = eval_constant(expr)
                symbols[name] = {
                    'type': node.get('type', 'int'),
                    'value': val
                }
            visit(node.get('expr'))

        # ---- ASIGNACIÓN ----
        elif ntype == 'assign':
            name = node.get('id')
            if name not in symbols:
                errors.append(f"Variable '{name}' no declarada")
                symbols[name] = {'type': 'int', 'value': None}

            visit(node.get('expr'))
            symbols[name]['value'] = None  # valor dinámico

        # ---- PRINT ----
        elif ntype == 'print':
            visit(node.get('expr'))

        # ---- IF ----
        elif ntype == 'if':
            visit(node.get('cond'))
            for s in node.get('then', []):
                visit(s)
            for s in node.get('otherwise', []):
                visit(s)

        # ---- WHILE ----
        elif ntype == 'while':
            visit(node.get('cond'))
            for s in node.get('body', []):
                visit(s)

        # ---- OPERADORES ----
        elif ntype == 'binop':
            visit(node.get('left'))
            visit(node.get('right'))

        elif ntype == 'unop':
            visit(node.get('expr'))

        # ---- IDENTIFICADOR ----
        elif ntype == 'id':
            name = node.get('name')
            if name and name not in symbols:
                errors.append(f"Variable '{name}' no declarada")

        # Literales (number, fnumber, bool) → sin análisis
        return

    # ---------------------------------------
    # Evaluación parcial de expresiones
    # ---------------------------------------
    def eval_constant(expr):
        if not isinstance(expr, dict):
            return None

        t = expr.get('node')

        if t == 'number':
            return expr.get('value')

        if t == 'fnumber':
            return expr.get('value')

        if t == 'bool':
            return expr.get('value')

        # Expresiones binarias
        if t == 'binop':
            l = eval_constant(expr.get('left'))
            r = eval_constant(expr.get('right'))
            op = expr.get('op')

            if l is None or r is None:
                return None

            try:
                if op == '+': return l + r
                if op == '-': return l - r
                if op == '*': return l * r
                if op == '/': return l / r
                if op == '>': return l > r
                if op == '<': return l < r
                if op == '>=': return l >= r
                if op == '<=': return l <= r
                if op == '==': return l == r
                if op == '!=': return l != r
            except Exception:
                return None

        return None

    # ---------------------------------------
    # EJECUTAR ANÁLISIS
    # ---------------------------------------
    try:
        visit(ast)
    except Exception as e:
        errors.append("Error interno en análisis semántico: " + str(e))

    if errors:
        return {'success': False, 'errors': errors}
    return {'success': True, 'symbol_table': symbols}


# Permite prueba independiente
if __name__ == "__main__":
    test = {
        'node': 'program',
        'stmts': [
            {'node': 'decl', 'type': 'int', 'id': 'x',
             'expr': {'node': 'number', 'value': 5}},
            {'node': 'assign', 'id': 'x',
             'expr': {'node': 'binop', 'op': '+',
                      'left': {'node': 'id', 'name': 'x'},
                      'right': {'node': 'number', 'value': 3}}},
        ]
    }

    print(analyze_semantics(test))
