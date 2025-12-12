# optimizer.py
"""
Optimizador sencillo:

Secciones principales:
1. Función is_number(x):
   - Verifica si un valor es un número (entero o flotante).

2. optimize_code(quadruples):
   - Entrada: Lista de cuádruplos.
   - Salida: Diccionario con cuádruplos optimizados y porcentaje de reducción.
   - Fases:
     a. Plegado de constantes: Simplifica operaciones con literales.
     b. Eliminación de asignaciones redundantes: Remueve asignaciones innecesarias como `t = t`.
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
