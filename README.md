🔧 Mini-Compilador Interactivo
Proyecto Final - Lenguajes y Autómatas II
Compilador completo con interfaz web para un lenguaje de programación simplificado. Implementa todas las fases de compilación desde análisis léxico hasta generación de código ejecutable.

📋 Características
Fases del Compilador

✅ Análisis Léxico - Reconocimiento de tokens
✅ Análisis Sintáctico - Construcción del AST
✅ Análisis Semántico - Tabla de símbolos y verificación de tipos
✅ Generación de Código Intermedio - Cuádruplos
✅ Optimización - Plegado de constantes y eliminación de código muerto
✅ Generación de Código Objeto - Código Python ejecutable
✅ Ejecución - Interpretación del código generado

Funcionalidades Avanzadas

🌳 Visualización del AST en formato JSON
⏭️ Compilación paso a paso con visualización de cada fase
🚀 Optimizador visual con comparación antes/después
❌ Detección de errores léxicos, sintácticos y semánticos
📊 Dashboard de métricas con estadísticas de compilación


🎯 Lenguaje Soportado
Tipos de Datos
javascriptint x = 10;
float y = 3.14;
bool activo = true;
Operadores
javascript// Aritméticos: +, -, *, /
int suma = 5 + 3;

// Relacionales: ==, !=, <, <=, >, >=
bool mayor = x > y;

// Lógicos: &&, ||, !
bool resultado = (x > 0) && (y < 10);
Estructuras de Control
javascript// Condicional
if (x > 0) {
    print(x);
} else {
    print(0);
}

// Ciclo
while (x < 10) {
    print(x);
    x = x + 1;
}

🚀 Instalación y Ejecución
Prerrequisitos

Python 3.8+
Node.js 14+
pip
npm

Backend (Python + Flask)
bash# 1. Navegar a la carpeta backend
cd backend

# 2. Crear entorno virtual (recomendado)
python -m venv venv

# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate

# 3. Instalar dependencias
pip install flask flask-cors ply

# 3.1 instalar dependcias de diseño
cd ..mini-compilador\frontend

npm install tailwindcss framer-motion react-icons
npx tailwindcss init


# 4. Ejecutar servidor
python app.py
El servidor estará disponible en: http://localhost:5000
Frontend (React)
bash# 1. Navegar a la carpeta frontend
cd frontend

# 2. Instalar dependencias
npm install

# 3. Ejecutar aplicación
npm start
La aplicación web se abrirá automáticamente en: http://localhost:3000

📁 Estructura del Proyecto
mini-compilador/
├── backend/
│   ├── app.py              # API Flask principal
│   ├── lexer.py            # Análisis léxico (PLY)
│   ├── parser.py           # Análisis sintáctico (PLY)
│   ├── semantic.py         # Análisis semántico
│   ├── intermediate.py     # Generación de cuádruplos
│   ├── optimizer.py        # Optimización de código
│   ├── codegen.py          # Generación de código Python
│   └── requirements.txt    # Dependencias Python
│
├── frontend/
│   ├── public/
│   │   └── index.html      # HTML base
│   ├── src/
│   │   ├── App.js          # Componente principal
│   │   ├── Editor.js       # Editor de código
│   │   ├── Results.js      # Visualización de resultados
│   │   ├── api.js          # Servicio API
│   │   └── index.js        # Entry point
│   └── package.json        # Dependencias Node
│
└── README.md               # Este archivo

🔌 API Endpoints
POST /compile
Compila código completo (todas las fases)
Request:
json{
  "code": "int x = 10;\nprint(x);"
}
Response:
json{
  "success": true,
  "phases": {
    "lexical": { "tokens": [...] },
    "syntax": { "ast": {...} },
    "semantic": { "symbol_table": [...] },
    "intermediate": { "quadruples": [...] },
    "optimization": { "optimized": [...] },
    "codegen": { "code": "..." },
    "execution": { "output": "10\n" }
  },
  "metrics": {
    "compilation_time": 45.2,
    "tokens_count": 8,
    "code_reduction": 25.0
  }
}
GET /examples
Obtiene ejemplos de código predefinidos
GET /health
Verifica el estado del servidor

🧪 Ejemplos de Uso
Ejemplo 1: Variables y Operaciones
javascriptint a = 10;
int b = 5;
int suma = a + b;
print(suma);
Ejemplo 2: Condicional
javascriptint edad = 20;
if (edad >= 18) {
    print(1);
} else {
    print(0);
}
Ejemplo 3: Ciclo While
javascriptint i = 0;
while (i < 5) {
    print(i);
    i = i + 1;
}
Ejemplo 4: Completo
javascriptint x = 10;
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
}

📊 Métricas Mostradas

⏱️ Tiempo de compilación (ms)
🔤 Cantidad de tokens generados
📄 Líneas de código fuente
⚙️ Cuádruplos antes de optimización
🚀 Cuádruplos después de optimización
📉 Porcentaje de reducción de código


🛠️ Tecnologías Utilizadas
Backend

Python 3.8+
Flask - Framework web
PLY (Python Lex-Yacc) - Generador de parsers
Flask-CORS - Manejo de CORS

Frontend

React 18 - Librería UI
Axios - Cliente HTTP
CSS-in-JS - Estilos en línea


📝 Optimizaciones Implementadas
1. Plegado de Constantes
Evalúa expresiones constantes en tiempo de compilación:
Antes:  t1 = 5 + 3
Después: t1 = 8
2. Eliminación de Código Muerto
Remueve variables temporales no utilizadas:
Antes:  t1 = 10    (no se usa)
        t2 = 20
Después: t2 = 20

🐛 Manejo de Errores
El compilador detecta y reporta:

❌ Errores Léxicos: Caracteres no válidos
❌ Errores Sintácticos: Estructura incorrecta
❌ Errores Semánticos:

Variables no declaradas
Incompatibilidad de tipos
Condiciones no booleanas




📦 Dependencias
Backend (requirements.txt)
flask==3.0.0
flask-cors==4.0.0
ply==3.11
Frontend (package.json)
json{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "axios": "^1.6.0"
  }
}

👥 Autor
Proyecto desarrollado para la asignatura Lenguajes y Autómatas II

📄 Licencia
Este proyecto es de uso académico y educativo.

🎓 Notas para el Informe Técnico
Este proyecto cumple con:

✅ Claridad en la Explicación - Documentación completa
✅ Desarrollo Técnico Estructurado - Código modular y comentado
✅ Cumplimiento del Manual Institucional - Formato TECNM
✅ 5 Funcionalidades Avanzadas - Todas implementadas

Funcionalidades Avanzadas Implementadas:

✅ Visualización interactiva del AST
✅ Generación de código paso a paso
✅ Visualizador de optimización
✅ Detección de errores en tiempo real
✅ Dashboard de métricas de compilación


🚀 Próximos Pasos (Mejoras Futuras)

 Soporte para funciones con parámetros
 Arrays y estructuras de datos
 Editor con resaltado de sintaxis (CodeMirror)
 Visualización gráfica del AST con D3.js
 Más optimizaciones (loop unrolling, etc.)
 Generación de código para otros lenguajes


¡Compilador listo para usar! 🎉