"""
API Flask para el Mini-Compilador
Servidor backend con endpoints RESTful

Secciones principales:
1. Importaciones: Importa módulos necesarios para Flask, CORS y los componentes del compilador.
2. Configuración de la aplicación: Configura Flask y habilita CORS para permitir peticiones desde el frontend.
3. Rutas:
   - `/`: Ruta de prueba para verificar que el servidor está funcionando.
   - `/health`: Ruta para verificar el estado del servidor.
   - `/compile`: Recibe código fuente, lo procesa a través de las fases del compilador y devuelve los resultados.
   - `/analyze/lexical`: Realiza análisis léxico del código fuente.
   - `/analyze/syntax`: Realiza análisis sintáctico del código fuente.
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import time

# Importar módulos del compilador
from lexer import analyze as lexer_analyze
from parser import parse as parser_parse
from semantic import analyze_semantics
from intermediate import generate_intermediate_code
from optimizer import optimize_code
from codegen import generate_code, execute_code

app = Flask(__name__)
CORS(app)  # Permitir peticiones del frontend


# ==========================
#     RUTA HOME (NUEVA)
# ==========================
@app.route('/', methods=['GET'])
def home():
    """Ruta principal para evitar 404"""
    return jsonify({
        'message': 'Mini-Compilador API funcionando',
        'status': 'ok',
        'endpoints': [
            '/compile',
            '/analyze/lexical',
            '/analyze/syntax',
            '/examples',
            '/health'
        ]
    }), 200


# ==========================
#     /health
# ==========================
@app.route('/health', methods=['GET'])
def health():
    """Verifica el estado del servidor."""
    return jsonify({'status': 'ok', 'message': 'Mini-Compilador API activa'})


# ==========================
#     /compile
# ==========================
@app.route('/compile', methods=['POST'])
def compile_code():
    """
    Endpoint principal: compila todo el código

    Se procesa el código fuente a través de las siguientes fases:
    1. Análisis Léxico: Se obtienen los tokens del código fuente.
    2. Análisis Sintáctico: Se genera el árbol de sintaxis abstracta (AST).
    3. Análisis Semántico: Se verifican errores semánticos y se genera la tabla de símbolos.
    4. Generación de Código Intermedio: Se traduce el AST a un código intermedio.
    5. Optimización: Se optimiza el código intermedio.
    6. Generación de Código: Se genera el código final a partir del código optimizado.
    7. Ejecución: Se ejecuta el código generado.

    Retorna:
    - Resultado de cada fase del compilador.
    - Métricas del proceso de compilación.
    """
    try:
        data = request.get_json()
        source_code = data.get('code', '')
        
        if not source_code.strip():
            return jsonify({
                'success': False,
                'error': 'No se proporcionó código fuente'
            }), 400
        
        start_time = time.time()
        result = {'success': True, 'phases': {}}
        
        # ---- FASE 1: LÉXICO ----
        tokens = lexer_analyze(source_code)
        result['phases']['lexical'] = {
            'success': True,
            'tokens': tokens,
            'count': len(tokens)
        }
        
        # ---- FASE 2: SINTÁCTICO ----
        parse_result = parser_parse(source_code)
        if not parse_result['success']:
            result['success'] = False
            result['error'] = parse_result['error']
            result['phase_error'] = 'syntax'
            return jsonify(result), 200
        
        result['phases']['syntax'] = {
            'success': True,
            'ast': parse_result['ast']
        }
        
        # ---- FASE 3: SEMÁNTICO ----
        semantic_result = analyze_semantics(parse_result['ast'])
        if not semantic_result['success']:
            result['success'] = False
            result['error'] = '; '.join(semantic_result['errors'])
            result['phase_error'] = 'semantic'
            result['phases']['semantic'] = semantic_result
            return jsonify(result), 200
        
        result['phases']['semantic'] = semantic_result
        
        # ---- FASE 4: INTERMEDIO ----
        intermediate_result = generate_intermediate_code(parse_result['ast'])
        if not intermediate_result['success']:
            result['success'] = False
            result['error'] = intermediate_result.get('error')
            result['phase_error'] = 'intermediate'
            return jsonify(result), 200
        
        result['phases']['intermediate'] = intermediate_result
        
        # ---- FASE 5: OPTIMIZACIÓN ----
        optimization_result = optimize_code(intermediate_result['quadruples'])
        result['phases']['optimization'] = optimization_result
        
        # ---- FASE 6: CODEGEN ----
        codegen_result = generate_code(optimization_result['optimized'])
        if not codegen_result['success']:
            result['success'] = False
            result['error'] = codegen_result.get('error')
            result['phase_error'] = 'codegen'
            return jsonify(result), 200
        
        result['phases']['codegen'] = codegen_result
        
        # ---- FASE 7: EJECUCIÓN ----
        execution_result = execute_code(codegen_result['code'])
        result['phases']['execution'] = execution_result
        
        # ---- MÉTRICAS ----
        end_time = time.time()
        result['metrics'] = {
            'compilation_time': round((end_time - start_time) * 1000, 2),
            'tokens_count': len(tokens),
            'quadruples_original': len(intermediate_result['quadruples']),
            'quadruples_optimized': len(optimization_result['optimized']),
            'code_reduction': optimization_result['reduction'],
            'lines_of_code': len(source_code.split('\n'))
        }
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error interno del servidor: {str(e)}'
        }), 500


# ==========================
#   /analyze/lexical
# ==========================
@app.route('/analyze/lexical', methods=['POST'])
def analyze_lexical():
    """
    Realiza análisis léxico del código fuente.

    Retorna:
    - Tokens generados.
    - Cantidad de tokens.
    """
    try:
        data = request.get_json()
        source_code = data.get('code', '')

        tokens = lexer_analyze(source_code)

        return jsonify({
            'success': True,
            'tokens': tokens,
            'count': len(tokens)
        }), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


# ==========================
#   /analyze/syntax
# ==========================
@app.route('/analyze/syntax', methods=['POST'])
def analyze_syntax():
    """
    Realiza análisis sintáctico del código fuente.

    Retorna:
    - Resultado del análisis sintáctico, incluyendo el AST.
    """
    try:
        data = request.get_json()
        source_code = data.get('code', '')

        parse_result = parser_parse(source_code)
        return jsonify(parse_result), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


# ==========================
#      /examples
# ==========================
@app.route('/examples', methods=['GET'])
def get_examples():
    """
    Proporciona ejemplos de código para pruebas.

    Retorna:
    - Lista de ejemplos de código.
    """
    examples = [
        {
            'name': 'Hola Mundo',
            'code': '''int x = 42;
print(x);'''
        },
        {
            'name': 'Operaciones Aritméticas',
            'code': '''int a = 10;
int b = 5;
int suma = a + b;
int producto = a * b;
print(suma);
print(producto);'''
        },
        {
            'name': 'Condicional If-Else',
            'code': '''int edad = 18;
if (edad >= 18) {
    print(1);
} else {
    print(0);
}'''
        },
        {
            'name': 'Ciclo While',
            'code': '''int contador = 0;
while (contador < 5) {
    print(contador);
    contador = contador + 1;
}'''
        },
        {
            'name': 'Ejemplo Completo',
            'code': '''int x = 10;
int y = 20;
int resultado = 0;

if (x < y) {
    resultado = y - x;
} else {
    resultado = x - y;
}

int contador = 0;
while (contador < resultado) {
    print(contador);
    contador = contador + 1;
}'''
        }
    ]

    return jsonify({'examples': examples}), 200


# ==========================
#      MAIN
# ==========================
if __name__ == '__main__':
    print("=== Mini-Compilador API ===")
    print("Servidor iniciando en http://localhost:5000")
    print("Endpoints disponibles:")
    print("  - POST /compile")
    print("  - POST /analyze/lexical")
    print("  - POST /analyze/syntax")
    print("  - GET  /examples")
    print("  - GET  /health")
    print("  - GET  /")
    app.run(debug=True, port=5000)
