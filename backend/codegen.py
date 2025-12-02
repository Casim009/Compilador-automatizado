# codegen.py
"""
Generación de "código objeto" y ejecución simple.
generate_code(optimized_quadruples) -> {'success': True, 'code': optimized_quadruples}
execute_code(code) -> {'success': True, 'output': '...'}
Nota: en esta versión simple el 'code' es la lista de cuádruplos optimizados.
La ejecución se realiza por una VM que interpreta la lista.
"""

import io
import sys

def generate_code(optimized):
    # Solo encapsulamos la lista y retornamos success
    return {'success': True, 'code': optimized}

def execute_code(code):
    # code es la lista de cuádruplos
    try:
        quads = code
        # primer pase: construir mapa de labels -> índice
        labels = {}
        for i, q in enumerate(quads):
            op, a1, a2, res = q
            if op == 'label':
                labels[a1] = i

        # VM state
        pc = 0
        vars_ = {}   # variables y temporales
        output_buf = io.StringIO()

        # ayuda para obtener valor real (resolver literales y variables)
        def val(x):
            if isinstance(x, (int, float, bool)):
                return x
            # si x es string que representa número?
            try:
                if isinstance(x, str):
                    # try int
                    if x.isdigit(): return int(x)
                    # float?
                    try:
                        return float(x)
                    except:
                        pass
                # otherwise variable lookup
                return vars_.get(x, 0)
            except Exception:
                return vars_.get(x, 0)

        while pc < len(quads):
            op, a1, a2, res = quads[pc]

            if op == 'label':
                pc += 1
                continue

            if op == 'assign':
                # a1 could be temp name or literal
                v = val(a1)
                vars_[res] = v
                pc += 1
                continue

            if op in ('+', '-', '*', '/'):
                l = val(a1)
                r = val(a2)
                if op == '+': vars_[res] = l + r
                elif op == '-': vars_[res] = l - r
                elif op == '*': vars_[res] = l * r
                elif op == '/':
                    # integer division if both ints
                    try:
                        if isinstance(l, int) and isinstance(r, int):
                            vars_[res] = l // r
                        else:
                            vars_[res] = l / r
                    except Exception:
                        vars_[res] = 0
                pc += 1
                continue

            if op == 'not':
                v = val(a1)
                vars_[res] = not bool(v)
                pc += 1
                continue

            if op == 'jfalse':
                cond = val(a1)
                if not bool(cond):
                    # jump to label res
                    lbl = res
                    if lbl in labels:
                        pc = labels[lbl] + 1
                    else:
                        # label not found -> halt
                        break
                else:
                    pc += 1
                continue

            if op == 'goto':
                lbl = res
                if lbl in labels:
                    pc = labels[lbl] + 1
                else:
                    break
                continue

            if op == 'print':
                v = val(a1)
                output_buf.write(str(v) + "\n")
                pc += 1
                continue

            # Unknown op: skip
            pc += 1

        output = output_buf.getvalue()
        return {'success': True, 'output': output}
    except Exception as e:
        return {'success': False, 'error': str(e)}
