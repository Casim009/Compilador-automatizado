# optimizer.py
"""
Optimizador sencillo:
- Plegado de constantes (cuando ambos operandos son literales numéricos)
- Eliminación de asignaciones redundantes (t = t)
Expone: optimize_code(quadruples) -> {'optimized': [...], 'reduction': X}
"""

def is_number(x):
    return isinstance(x, int) or isinstance(x, float)

def optimize_code(quadruples):
    # Primer pase: plegado de constantes
    folded = []
    for q in quadruples:
        op, a1, a2, res = q
        if op in ('+', '-', '*', '/'):
            # a1 and a2 could be names (strings) or temporals or literals
            if is_number(a1) and is_number(a2):
                # compute
                try:
                    if op == '+': val = a1 + a2
                    elif op == '-': val = a1 - a2
                    elif op == '*': val = a1 * a2
                    elif op == '/': val = a1 / a2 if a2 != 0 else 0
                    folded.append(('assign', val, None, res))
                    continue
                except Exception:
                    pass
        folded.append(q)

    # Segundo pase: eliminar asignaciones redundantes tipo assign t, None, t
    optimized = []
    for q in folded:
        op, a1, a2, res = q
        if op == 'assign' and a1 == res:
            # t = t -> eliminar
            continue
        optimized.append(q)

    # Calcular reducción
    original = len(quadruples)
    final = len(optimized)
    reduction = round(100.0 * (original - final) / original, 2) if original > 0 else 0.0

    return {'optimized': optimized, 'reduction': reduction}
